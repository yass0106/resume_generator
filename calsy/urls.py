from django.urls import  path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('calculator/', calculator, name='calculator'),
    path('form/',form,name="form"),
    path('',login_page,name='login'),
    path('log_out/',log_out,name='log_out'),
    path('register/',register_page,name='register'),
    path('homepage/',homepage,name= 'homepage'),
    # path('translate/', translate, name='translate'),
    path('welcome/', welcome, name='welcome'),
    path('restemp/', restemp, name='restemp'),
    path('resumeM1/',resumeM1,name='resumeM1'),
    path('resumeM2/',resumeM2,name='resumeM2'),
    path('resumeM3/',resumeM3,name='resumeM3'),
    path('resumeM4/',resumeM4,name='resumeM4'),
    path('todo/',todos,name='todo'),
    #  path('email/',email,name='email'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)