from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dimlife.views.home', name='home'),
    url(r'^archive$', 'blog.views.archive'),

)
