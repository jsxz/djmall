from djmall.urls import path
from . import views
app_name='news'
urlpatterns=[
    path('index/',views.index,name='index')
]