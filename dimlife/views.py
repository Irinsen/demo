from django.http import HttpResponse 
from django.shortcuts import render_to_response
from dimlife.models import News
from dimlife.models import Category


def hello(request):
    return HttpResponse("HELLO WORD")

def homepage(request):
    pnews=Category.objects.filter(title="Politics")
    fnews=Category.objects.filter(title="Finance")
    snews=Category.objects.filter(title="Science")
    cnews=Category.objects.filter(title="Culture")
    return render_to_response('homepage.html', locals())

def header(request):
    ultimate_news = News.objects.filter(impotant="Ultimate")
    return render_to_response('header.html', {'news': ultimate_news})

def news(request, id):
    try:
        news = News.objects.get(id=id)
        news.rating += 1
        news.save()
        return render_to_response('news.html', {'news': news})
    except:   
        return HttpResponse('News with id=%s not found' % id)