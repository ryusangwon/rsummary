from django.db import models

# model 생성 후 python manage.py makemigrations를 통해 알려주어야한다. model의 변경사항 인식
# python manage.py migrate 을 통해 실제 데이터베이스 적용.

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
    
    def __str__(self):
        return self.title