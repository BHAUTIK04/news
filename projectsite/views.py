from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from pymongo import MongoClient
import json
import uuid
from .forms import newsForm
from django.conf import settings
import os
# Create your views here.
def testFunction(request):
    cli = MongoClient()
    db = cli["projectsite"]
    cursor = db.news.find()
    news_list = []
    for i in cursor:
        news_list.append(i)
        print i
    return render_to_response("test.html", {"news":news_list})
    #return render_to_response("test.html")

def page1(request, nid):
    cli = MongoClient()
    db = cli["projectsite"]
    cursor = db.news.find({"nid":nid})
    news_list = []
    for i in cursor:
        news_list.append(i)
        print i
    return render_to_response("detail_list.html", {"news":news_list})
    #return render_to_response("detail_list.html")

def page2(request):
    return render_to_response("detail_list1.html")

def page3(request):
    return render_to_response("detail_list2.html")

def page4(request):
    return render_to_response("detail_list3.html")

def page5(request):
    return render_to_response("detail_list4.html")

# def insertdata(request):
#     print "hello"
#     return render_to_response('insert.html')


def insertdotas(request):
    if request.method == "POST":
        form = newsForm(request.POST, request.FILES)
        heading = request.POST.get("heading")
        desc = request.POST.get("description")
        uui = uuid.uuid4()
        data = {'heading':heading, 'description':desc, 'newsid':str(uui)}
        if form.is_valid():
            print "hello"
            f = request.FILES['fileform']
            print f.name
            filename = f.name
            ext = filename.split(".")[-1]
            
            filename = str(uui)+"."+ext
            with open(settings.IMAGE_URL+filename,"w") as fr:
                for i in f.chunks():
                    fr.writelines(i)
            data['photo'] = filename
            cli = MongoClient()
            db = cli["projectsite"]
            collection = db["news"]
            collection.insert(data)
            
            return HttpResponse("Success")
    
    else:
        form = newsForm()
        
    return render(request,"insert.html", {"forms":form})
    
  