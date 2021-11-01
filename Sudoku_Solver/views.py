from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import UploadFileForm
import base64
from io import BytesIO
from .method.main import solver

def home(request):

    if request.method == "POST":
        img = request.FILES.get("image")
       
        file = default_storage.save('file.jpg', img)
        
        solved = solver(file)

        url= solved

        return render(request, "index.html", {"url":url})

    return render(request, "index.html")