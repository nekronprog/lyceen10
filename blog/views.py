from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  UpdateView,
  DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class ShowNewsView(ListView):
  model = News
  template_name = 'blog/home.html'
  context_object_name = 'news'
  ordering = ['-date']
  paginate_by = 5

  def get_context_data(self, **kwards):
    ctx = super(ShowNewsView, self).get_context_data(**kwards)

    ctx['title'] = 'Главная страница сайта!'
    return ctx


class UserAllNewsView(ListView):
  model = News
  template_name = 'blog/user_news.html'
  context_object_name = 'news'
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return News.objects.filter(avtor=user).order_by('-date')

  def get_context_data(self, **kwards):
    ctx = super(UserAllNewsView, self).get_context_data(**kwards)

    ctx['title'] = f"Статьи от пользвотеля {self.kwargs.get('username')}"
    return ctx


class NewsDetailView(DetailView):
  model = News
  context_object_name = 'post'

  def get_context_data(self, **kwards):
    ctx = super(NewsDetailView, self).get_context_data(**kwards)  

    ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
    return ctx

class CreateNewsView(LoginRequiredMixin, CreateView):
  model = News
  template_name = 'blog/create_news.html'

  fields = ['title', 'text']

  def form_valid(self, form):
    form.instance.avtor = self.request.user
    return super().form_valid(form)
  
  def get_context_data(self, **kwards):
    ctx = super(CreateNewsView, self).get_context_data(**kwards)  

    ctx['title'] = 'Добовление статьи'
    ctx['btn_text'] = 'Добавить статью'
    return ctx
  
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
  model = News
  template_name = 'blog/create_news.html'

  fields = ['title', 'text']

  def form_valid(self, form):
    form.instance.avtor = self.request.user
    return super().form_valid(form)
  
  
  def test_func(self):
    news = self.get_object()
    if self.request.user == news.avtor:
      return True
    
    return False


  def get_context_data(self, **kwards):
    ctx = super(UpdateNewsView, self).get_context_data(**kwards)  

    ctx['title'] = 'Обновление статьи'
    ctx['btn_text'] = 'Обновить статью'
    return ctx

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = News
  success_url = reverse_lazy('home') 
  template_name = 'blog/delete-news.html'

  def test_func(self):
    news = self.get_object()
    if self.request.user == news.avtor:
      return True
    
    return False


def contact(request):
  return render(request, 'blog/contact.html', {'title': "Страница контакты"})


