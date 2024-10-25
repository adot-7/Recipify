from django.shortcuts import render

# Create your views here.
def land(request):
    return render(request, 'landingPage.html')