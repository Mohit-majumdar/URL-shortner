from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shorten_url(models.Model):

    orignal_url = models.URLField(null=True)
    short_url = models.CharField(max_length=10,null=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    expries_date = models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.orignal_url}"
    

class Clicks_short_url(models.Model):

    short_url = models.ForeignKey(Shorten_url,on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.short_url)}" 
