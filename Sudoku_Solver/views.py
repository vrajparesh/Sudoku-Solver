from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import UploadFileForm
import base64
from io import BytesIO
from .method.main import solver

def home(request):

    if request.method == "POST":
        # buffer = BytesIO()
        img = request.FILES.get("image")
       
        file = default_storage.save(img.name, img)
        
        solved = solver(file)

        # url = base64.b64encode(solved)
        # url = url.decode('utf-8')
        url= ''

        # buffer.close()
        return render(request, "index.html", {"url":url})
        # return HttpResponse(graph)

    return render(request, "index.html")