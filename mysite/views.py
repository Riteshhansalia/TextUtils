# I have created this website

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    # Get the Text
    djtext=(request.POST.get("text", "default"))

    # Check checkbox value
    removepunc=(request.POST.get("removepunc", "off"))
    fullcaps=(request.POST.get("fullcaps", "off"))
    newlineremover=(request.POST.get("newlineremover", "off"))
    extraspaceremover=(request.POST.get("extraspaceremover", "off"))
   
    # Check with checkbox is ON
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)    

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
              analyzed = analyzed + char
        params = {'purpose':'Remove NewLine', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
              analyzed = analyzed + char
        params = {'purpose':'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else: 
        return HttpResponse('Error')

def about(request):
    return HttpResponse("About")