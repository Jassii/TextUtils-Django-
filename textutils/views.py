#This file is made by me (Jasjeet Singh)

#Function "index"
           # def index():
           #     return "Hello Jasjeet !"

#In the above function if you are not providing the "request" argument..that it will definitely
#give you error.. 

#In order to resolve this..
           # def index(request):
           #     return "Hello Jasjeet !"

#This will again give the error..(something related to the string..)
#So inorder to use "views file" you must import "HttpResponse"


from django.http import HttpResponse

#the below process was done to learn about function and tags of the HTML..

# def index(request):
#     return HttpResponse("<h1>Hello Jasjeet Bhai ! </h1>")  #You can also insert the HTML tag..

# #You can aslo use the "anchor" tags of HTML in the function..Inorder to access some other sites..
# def about(request):
#     return HttpResponse('<h1>About Jasjeet Bhai </h1> In free time Jasjeet wants to watch Anime.<br> If you want you can also watch from <a href="https://www.netflix.com/in/">Netflix</a> ')


# def index(request):
#     return HttpResponse(' Home' )


#In the below example you can see that if you click on the "Back" ..then it will automatically
#switch you to the home page..
#So similarly you can do this with the rest of the buttons..

#Will be removing Punctuation..
def analyze(request):

    #If i have to get the text..
    djtext = request.POST.get('text','default')  #text which i input in the box..

    #Check checkbox values..
    removepunc = request.POST.get('removepunc','OFF') #this will tell whether checkbox is ON or not
    fullcaps = request.POST.get('fullcaps','OFF') #this will tell whether checkbox is ON or not
    newlineremove = request.POST.get('newlineremove','OFF')
    extraspaceremover = request.POST.get('extraspaceremover','OFF')
    charcount = request.POST.get('charcount','OFF')


    #Now i have to analyze the text..
    # return HttpResponse("Remove punc <a href ='/'>Back</a>")

    # analyzed = djtext

    
    #Check which checkbox is on

    #Will remove punctuations.
    if removepunc=='on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        #the below portion will remove the punctuation and will return the normal string.
        for char in djtext:
            if char not in punctuations:    
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations' ,'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    #this will convert the sentence into upper case.    
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Changed to UPPER CASE' ,'analyzed_text':analyzed} 
        djtext = analyzed
        # return render(request,'analyze.html',params)   

    #this will remove new line.
    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":  #if character is not the new line character..(we have to check both)
                analyzed = analyzed + char

        params = {'purpose':'Removed New Lines' ,'analyzed_text':analyzed}
        djtext = analyzed 
        # return render(request,'analyze.html',params) 
    
    #this will remove the extra spaces present in the line
    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):  
                analyzed = analyzed + char

        params = {'purpose':'Extra Space Remover' ,'analyzed_text':analyzed}
         
        # return render(request,'analyze.html',params)
    
    #this will count the character present in the text which user inserted.
    if charcount=="on":
        count=0
        for char in djtext:
            if char!=" ":
                count = count+1

        params = {'purpose':'Character Count' ,'analyzed_text':count} 
        # djtext = analyzed
        # return render(request,'analyze.html',params)    

    if(removepunc!='on' and fullcaps!='on' and newlineremove!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Plese select the operation")        
    
    return render(request,'analyze.html',params)    


# def capfirst(request):
#     return HttpResponse("Capitalize First")  

# def newlineremove(request):
#     return HttpResponse("New Line Remove")           

# def spaceremover(request):
#     return HttpResponse("Space Remove")   

# def charcount(request):
#     return HttpResponse("Character Count")   


#Now as you know..you were trying to pass the HTML codes in the HttpResponse in the form of
#the string...
#So inorder to avoid this..You can simply use templates...for better usage of HTML..

from django.shortcuts import render

# def index(request):
#     params = {'name':' Singh ','place':'USA'}
#     return render(request,'index.html',params)

#We won't be using params..

def index(request):
    return render(request,'index2.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')



