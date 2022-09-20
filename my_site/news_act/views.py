from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from news_act.forms import NewsForm, UserRegisterForm, UserLoginForm
from news_act.models import News, Category
from news_act.utils import MyMixin


class HomeNews(MyMixin, ListView):
    """Главная страница с новостями"""
    model = News
    template_name = 'news_act/home_news.html'
    context_object_name = 'news'
    paginate_by = 5

    # extra_context = {'title_page': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = self.get_upper('Главные новости')
        return context

    def get_queryset(self):
        return News.objects.filter(is_pub=True).select_related('category')
        # Гит тест


class NewsCategory(ListView):
    """Новости по категориям"""
    model = News
    template_name = "news_act/category.html"
    context_object_name = 'news'
    allow_empty = False  # При отсутсвии категории с какойто айди, вывод ошибки 404
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        category = Category.objects.get(pk=self.kwargs['category_id'])
        context = super().get_context_data(**kwargs)
        context['category'] = category.title
        context['title_page'] = context['category']
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_pub=True)


class ViewNews(DetailView):
    """Полная новость"""
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news_act/news_detail.html


class CreateNews(LoginRequiredMixin, CreateView):
    """Создание новости"""
    LoginRequiredMixin.login_url = '/admin/'
    # login_url = reverse_lazy('home')

    form_class = NewsForm
    template_name = 'news_act/add_news.html'
    # success_url = reverse_lazy('home') or get_absolute_url


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Успешно')
            login(request, user)
            return redirect('add_news')
        else:
            messages.error(request, 'Ошибка!')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }

    return render(request, 'news_act/register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_news')
        else:
            messages.warning(request, 'НЕ успешно!')
    else:
        form = UserLoginForm()

    return render(request, 'news_act/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# NOT USE
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'news': news,
        'category': category,
        'title_page': category.title
    }

    return render(request, 'news_act/category.html', context)


# NOT USE
def view_news(request, news_id: int):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news_act/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            # return redirect(news)
            new_news = form.save()
            return redirect(new_news)
    else:
        form = NewsForm()
    return render(request, 'news_act/add_news.html', {'form': form})

