from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import base64
from io import BytesIO

def home(request):

    if request.method == "POST":
        buffer = BytesIO()
        img = request.FILES.get("image")
        

        
        url = base64.b64encode(img.read())
        url = graph.decode('utf-8')
        
        buffer.close()
        return render(request, "index.html", {"url":graph})
        # return HttpResponse(graph)

    return render(request, "index.html")