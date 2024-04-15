# 설문 조사 페이지 만들기 Project!

https://www.youtube.com/watch?v=SQ4A7Q6_md8&t=799s 에서 도움을 받아 제작했다.

## 1. General setting

1. 가상환경 설정해주기.

```bash
python -m venv .venv    # 가상환경 폴더 .venv 생성
```
가상 환경 실행하기 위해서는 Window에서는 'cd .venv\Scripts' 해준 뒤 activate 해주면 된다.

2. 프로젝트에 필요한 라이브러리들 설치

'requirements.txt'파일을 생성하여 프로젝트에 필요한 라이브러리들을 적어준다.
```txt
django
pillow
django-cleanup
django-allauth
django-htmx
```
그리고 터미널에서 'pip install -r requirements.txt'로 파일에 적혀있는 라이브러리들을 설치해준다.
필요하다면 'pip install --upgrade pip'를 통해 최신으로 업데이트 해준다.

3. .gitignore 설정

git hub에 commit 할 때 올라가지 않았으면 하는 파일들을 정리해 놓는 파일이다.
나는 기본적으로 가상환경 폴더를 넣어두었다.

## 2. Project start

### 01. `django-admin startproject a_core .`

위 명령어로 새로운 프로젝트를 시작했다.
이 후 `python manage.py migrate`를 해서 migrate를 해줬고,
생성된 기본 django를 실행해 보았다. 실행은 `python manage.py runserver` 명령어로 하면 된다.

### 02. create home page

1) create 'a_home' table

```bash
python manage.py startapp a_home
```
위 명령어를 통해 홈페이지를 위한 a_home이란 테이블을 생성한다.
그리고 해당 폴더를 'a_core/settings.py' 파일에서 INSTALLED_APPS 부분 가장 마지막에 'a_home'을 추가해준다.

2) setting 'a_home' table

'a_home/views.py'파일에서 
```py
def home_view(request):
    return render(request, 'home.html')
```
위 코드를 추가해 주고 'a_core/urls.py'에서 홈페이지 url 주소를 만들어 준다.
```py
from a_home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name='home'),   # 추가
]
```

이 후 기본적인 template들을 모아놓을 'templates'라는 폴더를 만들어준다.
'a_core/settings.py'로 가서 TEMPLATES 중 'DIRS'에 해당 폴더를 추가해 준다.
```py
"DIRS": [ BASE_DIR / 'templates' ],
```
앞으로 우리는 page.html > layout.html > base.html 순으로 레이아웃을 포함할 것이다.

3) template setting

https://www.youtube.com/watch?v=SQ4A7Q6_md8&t=799s
위 영상에서 7:33~10:13를 참고하여 template를 구성해준다.

4) static setting

'static'이라는 폴더를 만들어 주고 'a_core/settings.py'에서 해당 폴더를 아래와 같이 추가해준다.
```py
STATIC_URL = "static/"
STATICFILES_DIRS = [ BASE_DIR / 'static' ]  # 추가
```
그리고 'static' 폴더에 'https://github.com/andyjud/django-starter-assets' 여기 레포지터리에 있는 static 폴더 내 파일을 모두 받아 넣으면 이미지들을 불러올 수 있다.

### 03. Create User's Profile Page

1) create 'a_users' table

```bash
python manage.py startapp a_users
```
위 명령어를 통해 홈페이지를 위한 a_users이란 테이블을 생성한다.
그리고 해당 폴더를 'a_core/settings.py' 파일에서 INSTALLED_APPS 부분 가장 마지막에 'a_users'을 추가해준다.

2) user model setting

유저 모델관련 코드를 작성하고 `python manage.py makemigrations`와 `python manage.py migrate`를 해준다.

3) user admin setting

```py
admin.site.register(Profile)
```
위 코드를 넣어주고 우린 새로운 유저가 등록 될 때마다 시그널을 보낼 것이다.

4) users/signals.py (new file)

5) users/apps.py setting

6) create superuser

```bash
python manage.py createsuperuser
```
명령어 다음 순서대로 Username, Email, 비밀번호를 설정해준다.
(잊어버리면 또 만들면 되서 가볍게 생각하고 만들자!)
이 후 서버를 실행해서 'python manage.py runserver' 'http://127.0.0.1:8000/admin/'에 접속하고
방금 만들었던 super user로 로그인 하면 관리자 페이지를 볼 수 있다.

7) template에 avatar 추가하기.

유튜브 영상 14:48~15:15 참조하여 template를 수정해준다.

### 04. Create user profile page

1) a_users/view.py

2) create users template in a_users folder

```bash
mkdir -p a_users/templates/a_users  # 윈도우에서는 안되는 명령어! ㅠㅠ
```
a_users/templates/a_users/profile.html 파일을 만들고 위에서 본 repository에서 profile.html 코드를 복사해온다.

3) a_users/urls.py (new file)

a_core/urls.py 에 등록해준다.

```py
from django.urls import path, include   # include 추가.
from a_home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name='home'),
    path('profile/', include('a_users.urls')),  # 추가.
]
```
이후 a_users/urls.py 파일을 생성해서 url 관련 코드를 작성한다. 
그리고 header.html에 가서 해당 url을 등록해준다.

### 05. Create user Edit profile page

1) a_users/forms.py (new file)

2) a_users/views.py 추가.

3) a_users/templates/a_users/profile_edit.html (new file)

4) a_users/urls.py 추가.

5) header.html에 등록.

6) templates/layouts/box.html (new file)

파일을 새로 생성한 뒤 profile_edit.html에 가서 최상단에 layouts/blank.html 을 불러오던 것을 box.html로 변경해준다.

7) a_users/views.py 코드 추가.

변경된 프로필 정보를 데이터에 반영할 수 있도록 코드를 추가해 준다.
```py
if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
```

8) media 폴더 추가.

media라는 폴더를 만들어주고 'a_core/settings.py'에서 해당 폴더를 추가해준다.
```py
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / 'media'
```

그리고 'a_core/urls.py'에도 해당 path를 추가해준다.
```py
from django.conf.urls.static import static
from django.conf import settings

# Only used in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

그리고 django.cleanup 라이브러리를 사용하기 위해 settings.py에서 INSTALLED_APPS 부분 가장 마지막에 'django_cleanup.apps.CleanupConfig'를 추가해준다.

### 06. create log out page

1) 'a_core/settings.py'에 auth 관련 추가.

```py
INSTALLED_APPS = [
    ...,
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    ...,
]

MIDDLEWARE = [
    ...,
    'allauth.account.middleware.AccountMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
```

2) 'a_core/urls.py' 추가.

```py
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')), # 추가
    path("", home_view, name='home'),
    path('profile/', include('a_users.urls')),
]
```

그런 다음 migrate를 해준다.

3) header.html에 logout 페이지 등록.

4) logout 관련 html 생성.

templates/allauth/layouts/base.html 파일을 생성해준다.

### 07. create log in page

1) header.html에 login 페이지 등록.

2) 'a_core/settings.py'에 login 관련 setting 추가.

```py
LOGIN_REDIRECT_URL = "/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
```

3) 알림창 삭제.

로그인 하고 로그아웃 할 때마다 알림창 뜨는 것을 삭제하기 위해서 template를 하나 더 만들거다.
'templates/account/messages/logged_in.txt'과 같은 폴더 안에 'logged_out.txt' 파일을 만들고 공란으로 둔다.

### 08. create sign in page

1) header.html에 sign in page 등록.

2) 'a_users/urls.py' 추가.

3) 'a_users/views.py' 수정.

```py
from django.urls import reverse

...
    if request.path == reverse('profile-onboarding'):
            onboarding = True
        else:
            onboarding = False

return render(request, 'a_users/profile_edit.html', {'form': form, 'onboarding': onboarding})    # form 뒤에 추가.
```

4) profile_edit.html 코드 일부 수정.

```html
{% if onboarding %}
<h1 class="mb-4">Complete your Profile</h1>
{% else %}
<h1 class="mb-4">Edit your Profile</h1>
{% endif %}

<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" >Submit</button>
    {% if onboarding %}
    <a class="button button-gray ml-1" href="{% url 'home' %}">Skip</a>
    {% else %}
    <a class="button button-gray ml-1" href="{{request.META.HTTP_REFERER}}">Cancel</a>
    {% endif %}
</form>
```

5) 'a_users/signals.py' 추가

### 09. create user page

1) 'a_core/urls.py' 추가.

```py
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path("", home_view, name='home'),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name='profile'), # 추가
]
```

2) 'a_users/views.py' 수정.

```py
from django.shortcuts import render, redirect, get_object_or_404    # 마지막 모듈 추가
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User # 추가
from .forms import *

# Create your views here.
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:   # else 부분 추가
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    return render(request, 'a_users/profile.html', {'profile': profile})
```

### 10. create user settings page

1) 'a_users/views.py' 코드 추가.

2) 'a_users/templates/a_users/profile_settings.html' 추가  (new file)

3) 'a_users/urls.py' path 코드 추가.

```py
path('settings/', profile_settings_view, name='profile-settings'),
```

4) 'templates/includes/header.html' 코드 수정.

5) 'a_core/settings.py'에 django-htmx 관련 코드 추가.

### 11. email update setting code

1) 'a_users/forms.py' email 관련 form 추가.

2) 'a_users/views.py'에서 login_required관련 코드 추가.

3) 'templates/partials/email_form.html' 추가. (new file)
그리고 '/a_users/templates/a_users/profile_settings.html' 에서 코드 추가.

4) 'a_users/urls.py' path 코드 추가.

5) 'a_users/signals.py' 코드 추가.

6) 'a_users/views.py' 코드 추가.

7) 'a_users/urls.py' path 코드 추가.

### 12. profile delete setting

1) 'a_users/views.py' 코드 추가.

2) 'a_users/templates/a_users/profile_delete.html' 추가  (new file)

3) 'a_users/urls.py' path 코드 추가.

4) '/a_users/templates/a_users/profile_settings.html' 코드 추가.

### 13. 404 page setting

1) 'templates\404.html' 추가  (new file)

2) 'a_core/settings.py'에 코드 수정 및 추가.


여기까지가 기본 page setting이다. 이제 설문조사 페이지를 만들어보자!! (본격적)

