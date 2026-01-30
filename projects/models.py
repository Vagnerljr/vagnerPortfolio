from django.db import models

# Create your models here.  

class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Technologies" # Correct plural form


class Project (models.Model): 
    title = models.CharField(max_length= 300)
    link = models.URLField(blank= True)
    code = models.URLField(blank= True)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, blank= True, related_name="projects")
    
    def __str__(self):
        return self.title