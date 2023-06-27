# Django 교안
## 1. Django란?
## 2. 환경 세팅
## 3. 배포 프로세스
1. 내가 window를 사용하고 있더라도 배포 환경과 동일 환경을 하나 구축합니다. (mac은 거의 mac에서 합니다.)
2. Django 코딩을 한 후 Github(GitLab)에 내가 작성한 코드를 업로드 합니다.
3. 업로드한 코드를 서버쪽에서 다운로드하여 실행시킵니다.(python manage.py runserver 0:80)
* 2번과 3번을 통합하는 것을 CI/CD구축이라고 합니다. 그래서 push를하면 자동으로 테스트 서버에 배포되고 실서버에 배포될 수 있도록 하는 편입니다.
## 4. Django Tutorial
1. 어떤 파일이 수정되어야 하는지 아래 이미지를 참고해주세요.
![](%ED%8F%B4%EB%8D%94%ED%8A%B8%EB%A6%AC.png)

2. url을 설계합니다.
```
juntae.com/
juntae.com/about -> about.html
juntae.com/product -> product.html
juntae.com/product/1 -> productdetails.html
juntae.com/a -> a.html
juntae.com/b -> b.html
juntae.com/c -> c.html
```
3. urls.py를 수정합니다. 다만, 지금 Django가 설치되어 있지 않기 때문에 Django를 설치합니다. (설계가 우선이기 때문에 위에서 충분히 기획을 한 다음에 한 번에 개발합니다. 본 교안은 클라우드 환경에서 직접 코딩합니다. AWS cloud9 클라우드 환경에서 직접 코딩할 수 있게 해줍니다.)
```
pip install --upgrade pip
mkdir mysite
cd mysite
python -m venv myvenv
source myvenv/bin/activate
pip install django==3.2
django-admin startproject tutorialdjango .
python manage.py migrate
```
myvenv라는 가상환경 설정하고 그 가상환경 안에 들어가서 django 3.2 version을 설치하는 명령어입니다.
django-admin 명령어를 통하여 tutorialdjango라는 프로젝트를 시작(폴더를 생성하고, 기본적인 파일이 세팅)합니다.

4. 설치가 다 되었으면 `container이름/mysite/tutorialdjango/settings.py`파일을 열고 기본 세팅을 해줍니다. 지금은 tutorial이기 때문에 28번째 줄에 있는 `ALLOWED_HOSTS = ['*']`만 수정을 합니다.

5. `python manage.py runserver 0:80` 명령어로 서버를 구동해봅니다. (실제로 개발할 때에는 이렇게 중간중간 실행하지 않습니다.) 클라우드에서 만들었기 때문에 바로 배포가 된 상태입니다.

6. urls.py를 설계대로 코딩하기 위해 main이라는 앱을 만들고 아래처럼 코딩합니다. 터미널에서 `python manage.py startapp main`를 입력하고 `mysite/tutorialdjango/settings.py`파일에서 `INSTALLED_APPS`에 app을 추가합니다.
```
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    #... 생략 ...
]
```
urls.py 코드입니다.
```
from django.contrib import admin
from django.urls import path
from main.views import index, about, product, productdetails, a, b, c

urlpatterns = [
    path('', index, name='index')
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('product/<int:pk>', productdetails, name='pd_detail'),
    path('a/', a, name='a'),
    path('b/', b, name='b'),
    path('c/', c, name='c'),
]
```

7. views.py파일로 가서 함수를 아래와 같이 모두 만듭니다.
```
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def product(request):
    return render(request, 'main/product.html')

def productdetails(request):
    return render(request, 'main/productdetails.html')

def a(request):
    return render(request, 'main/a.html')

def b(request):
    return render(request, 'main/b.html')

def c(request):
    return render(request, 'main/c.html')
```

8. mysite/main/templates/main와 같은 형식으로 폴더를 만들고 그 안에 index.html을 비롯한 html파일을 모두 생성합니다. 안에는 구분할 수 있는 간단한 텍스만 넣습니다.

9. mysite/로 이동하셔서 python manage.py runserver 0:80을 입력하고 각각 url을 test해봅니다. product/1만 제외하고 작동합니다. 위에 url이 작동하도록 만들어보도록 하겠습니다. /mysite/main/views.py로 들어갑니다.

```
def productdetails(request, pk):
    data = {
        'value': pk + 100
    }
    return render(request, 'main/productdetails.html', data)
```