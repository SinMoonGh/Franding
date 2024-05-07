from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from item.models import Item
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import UserAddInfoForm, UserCreateForm, CustomAuthenticationForm
# Create your views here.

def index(request):
    objects = Item.objects.all().order_by('-id')
    
    context = {
        'item_list' : objects
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        add_info_form = UserAddInfoForm(request.POST)
        
        if user_form.is_valid() and add_info_form.is_valid():
            # User 모델 저장
            user = user_form.save()

            # UserAddInfo 모델 저장 
            add_info = add_info_form.save(commit=False)
            # UserAddinfo 에 user, 주소 정보 추가
            add_info.user = user
            add_info.postcode = request.POST.get('postcode')  
            add_info.address = request.POST.get('address')   
            add_info.detailAddress = request.POST.get('detailAddress')  
            add_info.extraAddress = request.POST.get('extraAddress')    
            add_info.save()

            return redirect('register_done')
        else:
            # 유효성 검사에 실패한 경우
            context = {
                'user_form': user_form,
                'add_info_form': add_info_form
            }
            return render(request, 'registration/register.html', context)
    else:
        user_form = UserCreateForm()
        add_info_form = UserAddInfoForm()
        
        context = {
            'user_form': user_form,
            'add_info_form': add_info_form
        }

        return render(request, 'registration/register.html', context)

    
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
    
def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # 성공적으로 로그인 후 리다이렉트할 페이지
            return redirect('home')
    else:
        context = {
            'form' : CustomAuthenticationForm()
        }
    return render(request, 'registration/login.html', context)
    
def searchItem(request):
    search_word = request.POST.get('search_word', '')
    select_option = request.POST.get('select_option', '')
    objects = None
    
    if select_option == '':
        objects = Item.objects.filter(Q(name__icontains=search_word)| Q(summary__icontains=search_word)|Q(description__icontains=search_word)
                                  |Q(cat1__name__icontains=search_word)|Q(cat2__name__icontains=search_word)|Q(item_type__name__icontains=search_word)
                                  |Q(brand__name__icontains=search_word))
    elif select_option == 'cat1':
        objects = Item.objects.filter(Q(cat1__name__icontains=search_word))
    elif select_option == 'cat2':
        objects = Item.objects.filter(Q(cat2__name__icontains=search_word))
    elif select_option == 'name':
        objects = Item.objects.filter(Q(name__icontains=search_word))
    elif select_option == 'item_type':
        objects = Item.objects.filter(Q(item_type__name__icontains=search_word))
    elif select_option == 'brand':
        objects = Item.objects.filter(Q(brand__name__icontains=search_word))
    elif select_option == 'desc':
        objects = Item.objects.filter(Q(summary__icontains=search_word)|Q(description__icontains=search_word))
        
    paginator = Paginator(objects, 16) 

    page_number = request.GET.get('page', 1) 
    page_obj = paginator.get_page(page_number) 

    context = {
        'select_option':select_option,
        'search_word':search_word,
        'page_obj': page_obj
    }
    
    return render(request, 'search.html', context)

def about(request):
    return render(request, 'about.html')