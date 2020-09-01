from django.http import HttpResponse

def home(request):
  return HttpResponse("Homepage")

def about(request):
  return HttpResponse("About")

