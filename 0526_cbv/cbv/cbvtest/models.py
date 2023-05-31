from django.db import models

# Create your models here.p
class Test(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
#Username : haejun
#Email addresss : a01027833227@gmail.com
#password : 0000