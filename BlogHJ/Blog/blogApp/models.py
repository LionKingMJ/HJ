from django.db import models

class Blog(models.Model): #폼을 만드는 과정 -> 이걸로 글을쓰게 만듦
                        #이렇게 model에서 폼을 만든 후 migrate로 연결
    title = models.CharField(max_length=200)
    # CharField는 주로 제목(title), 이름(name), 설명(description) 등과 같은 짧은 문자열 데이터를 저장하기 위해 사용
    pub_date = models.DateTimeField('date published')
    body = models.TextField(blank=True, null=True)
    #필드(틀)를 생성한 것으로, 내용을 넣는것은 아님
    # img = models.ImageField(blank=True, null=True)
        #이미지 받아주는 ImageField, 크기조절은 css로?
            #pillow라이브러리를 설치해야 사진을 처리할 수 있다고한다

    def __str__(self): #게시글제목(postname)이 Post Object(views에 있음)을 대신하게 함
        return self.title