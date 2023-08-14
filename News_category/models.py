from django.db import models

# Create your models here.

class News_category(models.Model):
    objects = models.Model
    name = models.CharField(max_length=150)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class New(models.Model):
    objects = models.Model
    name = models.CharField(max_length=150)
    news_category = models.ForeignKey(News_category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

