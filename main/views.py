from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import News, Projects

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Главная',
            'theme' : {
                'one': 'Мы специалисты в области архитектуры',
                'two': 'Дизайн, в котором вы почувствуете себя дома',
                'three' : 'Готовы построить дом вашей мечты'
            },
            'text': {
                'one': 'Мы специалисты в своей области и готовы воплотить ваши идеи в жизнь',
                'two': 'Создаем уютные и функциональные пространства, отражающие вашу индивидуальность',
                'three' : 'Начните путь к идеальному жилью вместе с нашей командой профессионалов'
            }            
        }
        return context
    
class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'О нас',
            'theme' : 'О нас',
            'text': 'Здесь вы сможете узнать о нас', 
        }
        return context

class ContactView(TemplateView):
    template_name = 'main/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Контакты',
            'theme' :'Наши контакты',
            'text': 'здесь вы сможете отправить нам свое письмо',
        }
        return context

class ErrorView(TemplateView,):
    template_name = 'error.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Ошибка',
        }
        return context

class ServicesView(TemplateView):
    template_name = 'main/services.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Сервис',
            'theme' :'Наши услуги',
            'text': 'Здесь вы можете ознакомиться с нашими услугами',
        }
        return context

class ProjectView(ListView):
    template_name = 'main/project.html'
    model = Projects
    context_object_name = 'project'
    aginate_by = 4
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Проекты',
            'theme': 'Наши Проекты',
            'text': 'здесь вы можете ознакомиться с нашими проектами'
            
        }
        return context
    
class BlogView(ListView):
    template_name = 'main/blog.html'
    model = News
    context_object_name = 'News'
    paginate_by = 8 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Блог',
            'theme' :'Наш Блог',
            'text': 'Здесь вы сможете прочитать новости',
        }
        return context
    
class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'main/detail-project.html'
    context_object_name = 'project'
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'main/detail-news.html'
    context_object_name = 'news'
# Create your views here.
