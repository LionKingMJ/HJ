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
