from django.shortcuts import render
from django.http import HttpResponse,HttpRequest, request 
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
import os
from matplotlib import pyplot as plt
from .predictions import plot_image

from imutils import paths
import cv2

import base64
from io import BytesIO 

from .models import InputImg


def allowed_image(filename):
    if not '.' in filename:
        return False
    
    ext = filename.rsplit('.',1)[1]

    if ext.upper() in settings.ALLOWED_EXTENSIONS:
        return True
    else:
        return False

# Create your views here.
url=["url"]
def index(request):
      
    if request.method == 'POST' and request.FILES['img']:

        dir = settings.MEDIA_ROOT
        for f in os.listdir(dir):
            os.remove(os.path.join(dir,f))

        file = request.FILES['img']
        if file.name =="":
            print("File Must have name")
            messages.warning(request,'Invalid Input File Has No Name')
            return render(request, 'skin_tone/index.html', {})

        if not allowed_image(file.name):
            print("File format is not allowed")
            messages.warning(request,'File format is not supported')
            return render(request, 'skin_tone/index.html', {})

        else:
            
            dir = settings.MEDIA_ROOT
            for f in os.listdir(dir):
                os.remove(os.path.join(dir,f))

            img = request.FILES['img']
           # fs = FileSystemStorage()
            #filename = fs.save(img.name,img)
            #url.clear()
            #url.append( fs.url(filename))
            #print(url)
            InputImg.objects.all().delete()
            image = InputImg()
            image.image = img
            image.save()
            print('Image Uploaded succesfully')
            print(image.image.url)
            messages.success(request,'File is successfuly submmited')
            return render(request, 'skin_tone/index.html', {'image':image})  

    return render(request, 'skin_tone/index.html', {})        






def output(request):

    if request.method == 'POST':
        #print(url)
        #img = url[0]
        img =  InputImg.objects.all().first()
      
        img_list=list(paths.list_images('skin_tone/input/'))
        print(img_list)
        image = cv2.imread(img_list[0])

        plt,skinTone = plot_image(image)

        print(skinTone)
        return render(request, 'skin_tone/output.html', {'img':img, 'skinTone':skinTone, 'plt':plt})