from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.conf import settings
from rest_framework.response import Response
from joblib import load 
from django.shortcuts import render
import os
from django.http import JsonResponse
import numpy as np
import cv2

# Create your views here.
def index(request):
    return render(request, 'mlapp/index.html')

def output(request, result):
    return render(request, 'mlapp/output.html', {'prediction': result})

def aboutus(request):
    return render(request,'mlapp/about.html')


@api_view(['POST'])
def predict_covid(request):
    print("Request received")
    if request.method == 'POST':
        print("Receiving....")
        scaler_path = os.path.join(settings.BASE_DIR, 'mlapp', 'scaler.pkl')
        svm_model_path = os.path.join(settings.BASE_DIR, 'mlapp', 'svm_model.pkl')
        scaler = load(scaler_path)
        model = load(svm_model_path)
        
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        file_path = os.path.join(default_storage.location, file_name)
        image = cv2.imread(file_path)
        image = cv2.resize(image, (500, 500))
        image = image / 255.0  # Normalize the image
        image = image.flatten().reshape(1, -1)
        image = scaler.transform(image)  
        prediction = model.predict(image)
        print(prediction)
        if prediction[0] == 1:
            result = "Covid Negative"
        else:
            result = "Covid Positive"

        os.remove(file_path)
        return redirect('output', result=result)

