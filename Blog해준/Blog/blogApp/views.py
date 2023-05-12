from django.shortcuts import render
from .models import Blog
 #models.py에서 적었던 Blog를 import해주기

def lion(request): #lion이라는 함수는 서버에 요청이 들어왔을 때 lion.html을 렌더링해서 우리에게 보여줌
    blogs = Blog.objects #Blog.objects는 admin페이지에서 확인했던 blog 안의 데이터들을 말함    #Blog는 models에 있는걸 말함
    return render(request, 'lion.html', {'blogs':blogs})
                                        #blogs라는 변수를 template에서 쓸 떄 blogs라는 이름으로 가져오겠다

def lionPosting(request, pk):
    #pk로 개별 게시글을 검색
    blog = Blog.objects.get(pk=pk)
    return render(request, 'lionPosting.html', {'blog':blog})

def lionNewPost(request):
    if request.method == 'POST':
        newLion=Blog.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
            pub_date = request.POST['pub_date']
            # img=request.POST['img'],
        )
        return render(request, 'lionNewPost.html', {'newLion': newLion})
    return render(request, 'lionNewPost.html')

def lionEdit(request, pk): 
    #세부화면에서 수정하는것이기에 pk값을 안받아도 되나?
    edit = Blog.objects.get(pk=pk) #edit이란 변수에는 그 pk페이지에 맞는 정보들이 들어있다.
        #node에서 data = req.body로 받아왔던 것과 유사
    if request.method == 'POST':
        edit.title=request.POST['title'][0],
        edit.body=request.POST['body'][0],
        edit.pub_date = request.POST['pub_date'][0]
        edit.save()
    return render(request, 'lionEdit.html', {'edit':edit})
        #request가 있는 경우 edit값과 함께 lionEdit을 렌더링한다
        #request가 없는 경우는 edit값이 없기에 페이지이동역할로만 작동된다