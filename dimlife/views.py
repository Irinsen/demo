from django.http import HttpResponse
from django.shortcuts import render_to_response
from dimlife.models import News

def hello(request):
    return HttpResponse("HELLO WORD")

def homepage(request):
    return render_to_response('homepage.html', {'news_list': News.objects.all()})

def news(request, id):
    try:
        news = News.objects.get(id=id)
        news.rating += 1
        news.save()
        return render_to_response('news.html', {'news': news})
    except:   
        return HttpResponse('News with id=%s not found' % id)