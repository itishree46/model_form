from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name
class Student(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    number=models.IntegerField()
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    email=models.EmailField()
    #password=models.CharField(max_length=100)
    #add=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Subject(models.Model):
    #name=models.ForeignKey(Student,on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=100)

    