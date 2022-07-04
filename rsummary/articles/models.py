from django.db import models

# model 생성 후 python manage.py makemigrations를 통해 알려주어야한다. model의 변경사항 인식
# python manage.py migrate 을 통해 실제 데이터베이스 적용.

# Create your models here.
# class Menu(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=100)
#     price = models.IntegerField()
    
#     def __str__(self):
#         return self.name