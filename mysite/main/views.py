from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import base64
from .models import *
from .forms import ImageUploadForm
from .age_gender_predict.age_gender_prediction import detect_face
import numpy as np

#Homepage
def homepage(request):
    return render(request=request,
                  template_name='main\categories.html',
                  context={'categories':TutorialCategory.objects.all})

# Views when u navigate in website
def single_slug(request,single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if(single_slug in categories):
        #get list of series in category by filtering from single_slug -->category_slug---(foreign key)--->series_category
        matching_series=TutorialSeries.objects.filter(series_category__category_slug=single_slug)

        series_urls={}
        for item in matching_series.all():
            #take the first tutorial[part 1] in series by filtering from series_title ---(foreign key)--->tutorial_series
            tutorial_first=Tutorial.objects.filter(tutorial_series__series_title=item.series_title).earliest("tutorial_published")
            series_urls[item]=tutorial_first.tutorial_slug
        return render(request,
                      "main\series.html",
                      {"series_urls":series_urls})

    tutorials= [t.tutorial_slug for t in Tutorial.objects.all()]
    if(single_slug in tutorials):
        this_tutorial=Tutorial.objects.get(tutorial_slug=single_slug)
        list_tutorials_from_series=Tutorial.objects.filter(tutorial_series__series_title=this_tutorial.tutorial_series).order_by("tutorial_published")
        this_tutorial_idx=list(list_tutorials_from_series).index(this_tutorial)

        return render(request,
                      "main/tutorial.html",
                      {"tutorial":this_tutorial,
                       "sidebar":list_tutorials_from_series,
                       "this_tutorial_idx":this_tutorial_idx})

    return HttpResponse(f"{single_slug} does not correspond to anything")

def uploadImageView(request):
    if request.method=='POST':
        form=ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            imageUploaded=request.FILES['imageFile']
            imageData=imageUploaded.read()
            #image_to_string=base64.b64encode(imageData).decode('ascii')
            '''Here to process image'''
            image_to_numpy = np.fromstring(imageData,np.uint8)
            print(np.shape(image_to_numpy))
            #print(np.shape(image_to_numpy))
            image_result = detect_face(image_to_numpy)
            #result_to_string=image_result.tostring()
            result_to_string = base64.b64encode(image_result).decode('ascii')
            mime = "image/jpg"
            mime = mime + ";" if mime else ";"
            f = {"upFile": "data:%sbase64,%s" % (mime, result_to_string)}
            return render(request, 'main/previewImage.html', f)
    else:
        form=ImageUploadForm()
    return render(request,'main/previewImage.html',{'form':form})

def displayResult(request):
    if request.method=='GET':
        images= ImageUpload.objects.all()
        print(images)
        return render(request, 'main/result_age_predict.html', {'images_results': images})
