from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Lion(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField('date published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank = True, upload_to = "image")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Extra(models.Model):
    
# mixins
# generic cbv
# viewset
# as.view()
