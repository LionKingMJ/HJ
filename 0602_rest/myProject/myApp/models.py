from django.db import models
from django.conf import settings

# Create your models here.
class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
        #외부에서 키를 가져와 사용
        #회원 삭제 시 회원이 작성한 것들도 다 지우겠다(on_delete)
    title = models.CharField(max_length=200)
    body = models.TextField()

