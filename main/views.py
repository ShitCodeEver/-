from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import News, Projects
from .forms import FormLatter
from django.core.mail import EmailMessage
from django.urls import reverse_lazy

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

"""class ContactView(TemplateView):
    template_name = 'main/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Контакты',
            'theme' :'Наши контакты',
            'text': 'здесь вы сможете отправить нам свое письмо',
        }
        return context"""
    
class ContactView(FormView):
    template_name = 'main/contact.html'
    form_class = FormLatter
    success_url = reverse_lazy('success.html')
    
    def form_valid(self, form):
        subname = form.cleaned_data.get('name')
        subsurname = form.cleaned_data.get('surname')
        subemail = form.cleaned_data.get('email')
        subtext = form.cleaned_data.get('text')
        
        subfullname = f"{subname} {subsurname}"
        emailsubject = f"Обратная связь: письмо от {subfullname}"
        emailmessage = (
            f"Вам пришло новое сообщение с сайта!\n\n"
            f"Отправитель: {subfullname}\n"
            f"Email для связи: {subemail}\n\n"
            f"Текст сообщения:\n{subtext}"
        )
        
        mail = EmailMessage(
            subject=emailsubject,
            body=emailmessage,
            from_email='noreply@mysite.com', # Технический email вашего сайта (из settings.py)
            to=['my-email@example.com'],      # Ваша личная/рабочая почта, куда придет письмо
            reply_to=[subemail],              # СЮДА передаем почту пользователя!
        )
        
        mail.send(fail_silently=False)
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = {
            'title':'Контакты',
            'theme':'Наши контакты',
            'text':'Здесь вы можете отправить нам свое письмо'
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
    
class SuccessView(TemplateView):
    template_name = 'success.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['settings'] = {
            'title' : 'Успех',
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
    paginate_by = 4
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
