from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/projects')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Contact (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    image = models.ImageField(upload_to='media/skills/', verbose_name='Imagem', null=True, blank=True)
    percentage = models.IntegerField()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
