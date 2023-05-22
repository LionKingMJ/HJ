from django.contrib import admin
from .models import Blog
from django.shortcuts import render

# Register your models here.
admin.site.register(Blog) #admin.py에 model을 등록하는 명령어
                        #admin이 게시글에 접근 가능하게 해 줌