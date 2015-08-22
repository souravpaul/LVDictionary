from django.shortcuts import render,render_to_response,RequestContext
import requests,string
from django.http import HttpResponse,HttpResponseRedirect
from .models import Dictionary

# Create your views here.


#Imdex page maintaining search,query of words
def index(request):
	query=request.GET.get('query')
	target=request.GET.get('target')
	
	#Show bookmarked words
	if query=="bookmarked": 
		words=Dictionary.objects.all().order_by('-ranking')
		bookmarked=words
		return render_to_response('dictionary.html',{'words': words, "pages":list(string.ascii_uppercase),"query": "bookmarked" ,"bookmarked":bookmarked[:5],"bookmarked_count":len(bookmarked)})
	
	#targated words for searching operation
	if target != None:
	    query=target[0]
	else:
	    target=""
	if query != None:			
		json_response=requests.get('http://letsventure.0x10.info/api/dictionary.php?type=json&query=' + query)
		words = json_response.json()
		bookmarked=Dictionary.objects.all().order_by('-ranking')
		return render_to_response('dictionary.html',{'words': words, "pages":list(string.ascii_uppercase),"query":query.upper(),"bookmarked":bookmarked[:5],"target":target,"bookmarked_count":len(bookmarked)})
	
	#Cover page without any word query
	else:
	    bookmarked=Dictionary.objects.all().order_by('-ranking')
	    return render_to_response('index.html',{"pages":list(string.ascii_uppercase),"bookmarked":bookmarked[:15],"bookmarked_count":len(bookmarked)})



#crating bookmark and retun response as a json data
def bookmark(request):
	word=request.GET.get('word').strip()
	description=request.GET.get('description').strip()
	audio_url=request.GET.get('audio_url').strip()
	#checking if the word already exists
	data=Dictionary.objects.filter(word=word)
	if len(data)==0:
		Dictionary(word=word,description=description,audio_url=audio_url).save()
		return HttpResponse('{"status_type":"OK"}', content_type="application/json")
	else:
		return HttpResponse('{"status_type":"CONFLICT"}', content_type="application/json")


#Check if a word is bookmarked or not and sending response as a json data
def bookmarkCheck(request):
    word=request.GET.get('word').strip()
    data=Dictionary.objects.filter(word=word)
    if len(data)==0:
        return HttpResponse('{"status_type":"NO"}', content_type="application/json")
    else:
        #Increasing the hit count for word  
        data[0].ranking=data[0].ranking+1
        data[0].save()
        return HttpResponse('{"status_type":"YES"}', content_type="application/json")


#Clearing all mookmark
def bookmarkremove(request):	
	if Dictionary.objects.all().delete():
		return HttpResponse('{"status_type":"OK"}', content_type="application/json")
	else:
		return HttpResponse('{"status_type":"FAILED"}', content_type="application/json")