from django.db import models

# Create your models here.

class Dictionary(models.Model):
	word=models.CharField(max_length=30,null=False,blank=False,unique=True)
	description=models.TextField(null=False,blank=False)
	audio_url=models.URLField(null=False,blank=False)
	ranking=models.IntegerField(default=1)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)