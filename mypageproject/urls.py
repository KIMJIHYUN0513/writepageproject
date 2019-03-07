from django.contrib import admin
from django.urls import path
import mypage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mypage.views.home, name="home"),
    path('text/<int:text_id>',mypage.views.detail,name="detail"),
    path('text/new/',mypage.views.new, name="new"),
    path('text/create/',mypage.views.create, name="create"),
]
