from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ads, Category
from .forms import AdsForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


class HomeAds(ListView):
    model = Ads
    template_name = 'ads/list_of_ads.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class AdsByCategory(ListView):
    model = Ads
    template_name = 'ads/list_of_ads.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Ads.objects.filter(category_id=self.kwargs['category_id'])


class ViewAds(DetailView):
    model = Ads
    context_object_name = 'ads_item'


class CreateAds(LoginRequiredMixin, CreateView):
    form_class = AdsForm
    template_name = 'ads/add_ads.html'
    success_url = reverse_lazy('home')
    raise_exception = True


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            mail = send_mail('Регистрация', 'Вы успешно зарегистрировались', 'test_for_skills@mail.ru', [user.email], fail_silently=True)
            if not mail:
                messages.error(request, 'Ошибка отправки')
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'ads/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'ads/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')