from django.db import models

# Create your models here.p
class ClassBlog(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
#Username : haejun
#Email addresss : a01027833227@gmail.com
#password : 0000