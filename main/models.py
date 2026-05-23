from django.db import models
from django.utils.text import slugify

class News(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, unique=True)
    anons = models.CharField(max_length=100)
    full_text = models.TextField()
    date = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class Projects(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=100)
    full_text = models.TextField()
    MainImage = models.ImageField(upload_to='media/project')
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class ImageProject(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/other')
    
# Create your models here.
