from django.shortcuts import render,redirect, get_object_or_404  # detail 을 위한 import
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Text
from .models import Comment

# Create your views here.

def home(request):
    texts=Text.objects
    text_list=Text.objects.all()    # 모든 글들을 대상
    paginator=Paginator(text_list, 3)   # 세 개를 한 페이지로 자르기
    page=request.GET.get('page')    # request 된 페이지가 뭔지 알아내고 (request 페이지를 변수에 담아내고)
    posts=paginator.get_page(page)  # request 된 페이지를 얻어온 뒤 return 해 준다
    return render(request, 'home.html', {'texts':texts, 'posts':posts})

def detail(request, text_id):
    details=get_object_or_404(Text, pk=text_id)
    return render(request, 'detail.html',{'details':details})

def new(request):
    return render(request,'new.html')

def create(request):
    text = Text()
    text.title = request.GET['title']
    text.body = request.GET['body']
    text.pub_date = timezone.datetime.now()
    text.save()
    return redirect('/text/' + str(text.id))

