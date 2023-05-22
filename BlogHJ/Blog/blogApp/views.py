from django.shortcuts import render, redirect
from .models import Blog
 #models.py에서 적었던 Blog를 import해주기
from django.utils import timezone

def lion(request):
    blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'lion.html', {'blogs':blogs})
                                   
def lionPosting(request, pk):
    #pk로 개별 게시글을 검색
    blog = Blog.objects.get(pk=pk)
    return render(request, 'lionPosting.html', {'blog':blog})

def lionNewPost(request):
    if request.method == 'POST':
        newLion=Blog.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
            pub_date = timezone.now()
        )
        return redirect('/lion', {'nweLion':newLion})
    return render(request, 'lionNewPost.html')

def lionEdit(request, pk): 
    update = Blog.objects.get(pk=pk) 
    if request.method == 'POST':
        update.title = request.POST['title']
        update.body = request.POST['body']
        update.pub_date = timezone.now()
        update.save()
        return redirect('/lion/' + str(pk))
    else:
        form = {
            'title' : update.title,
            'body' : update.body,
        }
    return render(request, 'lionEdit.html', {'update': update, 'form':form})


def lionUpdate(request, pk):
    update = Blog.objects.get(pk=pk)
    update.title=request.POST['title']
    update.body=request.POST['body']
    update.pub_date = timezone.now()
    update.save()
    return redirect('/lion', pk=update.pk)

def lionDel(request, pk):
    lionDel = Blog.objects.get(pk=pk)
    lionDel.delete()
    return redirect('/lion')