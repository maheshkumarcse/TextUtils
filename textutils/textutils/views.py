# # this is my first file
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>hello mahesh kumar bro</h1> <a href="https://github.com/maheshkumaecseb">Visit my github</a>''')

# # def first(request):
# #     return HttpResponse('''<h1>hello youtube</h1> <a href="https://github.com/maheshkumaecseb">Visit my youtube</a>''')

# # def index(request):
# #     return HttpResponse('''<h1>hello mahesh kumar bro</h1> <a href="https://github.com/maheshkumaecseb">Visit my github</a>''')

# # def index(request):
# #     return HttpResponse('''<h1>hello mahesh kumar bro</h1> <a href="https://github.com/maheshkumaecseb">Visit my github</a>''')

# def about(request):
#     return HttpResponse("about mahesh kumar bro")

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
      return render(request,'index.html')
    # return HttpResponse("HOME")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # check box value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
    if(newlineremover == "off" and  extraspaceremover=="off" and fullcaps=="on" and removepunc == "on"):
        return HttpResponse("please select any operations and try again")
        # return render(request, 'analyze.html', params)
    
    
    
    # else:
    #     return HttpResponse('Error')
    return render(request, 'analyze.html', params)
# def capfirst(request):
#      return HttpResponse("capitalize first <a href='/' > back </a>")
# def newlineremove(request):
#      return HttpResponse(" newlineremove <a href='/' > back </a> ")
# def spaceremove(request):
#      return HttpResponse(" spaceremove <a href='/' > back </a>")
# def charcount(request):
#      return HttpResponse("charcount <a href='/' > back </a> ")
