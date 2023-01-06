from django.shortcuts import render

# Create your views here.
def cdnmethod(request):
    return render(request,'cdnmethod.html')
def download(request):
    return render(request,'download.html')