from django.shortcuts import render

def index(request):
    """The home page for my resume site."""
    return render(request, 'resume_app/index.html')


