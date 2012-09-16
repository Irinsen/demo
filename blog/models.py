from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateField()
    
    class Meta:
        ordering = ('-timestamp',)
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')    
    
admin.site.register(BlogPost, BlogPostAdmin)
