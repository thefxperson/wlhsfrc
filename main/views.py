from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'nbar': 'index'})

def about(request):
    return render(request, 'main/about.html', {'nbar': 'about'})

def aboutfirst(request):
    return render(request, 'main/aboutfirst.html', {'nbar': 'about'})

def aboutrobot(request):
    return render(request, 'main/aboutrobot.html', {'nbar': 'about'})

def outreach(request):
    return render(request, 'main/outreach.html', {'nbar': 'about'})

def contact(request):
    return render(request, 'main/contact.html', {'nbar': 'about'})