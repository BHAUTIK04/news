from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from pymongo import MongoClient
import json
import uuid
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

def insertdata(request):
    print "hello"
    return render_to_response('insert.html')


def insertdotas(request):
    print "helloji"
    data = json.loads(request.body)
    uui = uuid.uuid4()
    print str(uui)
    data["nid"] = str(uui)
    print data
    cli = MongoClient()
    db = cli["projectsite"]
    collection = db["news"]
    collection.insert(data)

    return HttpResponse("success")