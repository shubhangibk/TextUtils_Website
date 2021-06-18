
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    #analyzed = djtext

    if(removepunc =="on" and fullcaps =="on" and newlineremover == "on" and extraspaceremover == "on"):
        return HttpResponse(" Please select only one operation!")

    elif(removepunc =="on"):

        punctuations = '''!()-[]{};:"'"'\,<>.?/@$#%*^~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze1.html',params)
        
    elif(fullcaps =="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed to uppercase','analyzed_text':analyzed}
        return render(request,'analyze1.html',params)

    elif(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'Removed newlines','analyzed_text':analyzed}
        return render(request,'analyze2.html',params)

    elif(extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index-1]==" ":
                pass
            else:
                analyzed = analyzed + char 

        params = {'purpose':'Removed space','analyzed_text':analyzed}
        return render(request,'analyze1.html',params)

    

    else:
        return HttpResponse("Please select any operation to perform!")

    


