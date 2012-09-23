#coding: utf-8

from django.db import models
from dimlife.utils import ACCESS_MASKS, NEWS_STATUS

class News(models.Model):
    slug        = models.SlugField(max_length=100)
    title       = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    text        = models.TextField()
    access_mask = models.CharField(max_length=100, choices=ACCESS_MASKS, default='All', blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    date_show   = models.DateTimeField(blank=True,null=True)
    status      = models.CharField(max_length=100, choices=NEWS_STATUS, default='NOT_ACTIVE')
    impotant    = models.CharField(max_length=100, choices=[('Important','Important'), ('Unimportant','Unimportant')], default='Unimportant')
    rating      = models.IntegerField(blank=True, null=True)    
    
    def __unicode__(self):
        return self.title

class Category(models.Model):
    title       = models.CharField(max_length=100)
    news        = models.ForeignKey('News', blank=True, null=True) 
    
    def __unicode__(self):
        return self.title

class Keywords(models.Model):
    word        = models.CharField(max_length=100)
    news        = models.ManyToManyField(to='News', blank=True, null=True, verbose_name='keywords')

    def __unicode__(self):
        return self.word
    