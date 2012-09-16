from blog.models import BlogPost
from django.template import loader
from django.template.context import Context
from django.http import HttpResponse

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))