from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()

#Username : haejun
#Email addresss : a01027833227@gmail.com
#password : 0000