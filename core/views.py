from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)

def resume(request):
    context = {'resume': 'active'}
    return render(request, 'core/resume.html', context)

def project(request):
    context = {'project': 'active'}
    return render(request, 'core/project.html', context)
    