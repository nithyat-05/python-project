from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! This is my first Django web app.")

