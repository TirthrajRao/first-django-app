from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='uploads')
    content = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


class Feedback(models.Model):
    
    email = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120)
    message = models.CharField(max_length=150)
    createdAt = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Feedbacks"



