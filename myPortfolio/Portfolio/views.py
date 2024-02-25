from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'image_url': '/static/images/Myimage.jpg'}
    return render(request , 'index.html' , context)
