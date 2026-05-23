from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('error/', views.ErrorView.as_view(), name='error'),
    path('project/<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news-detail')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)