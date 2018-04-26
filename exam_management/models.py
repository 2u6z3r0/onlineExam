from django.db import models

# Create your models here.

class Exam(models.Model):
    exam_name = models.Charfield(max_lenght=100)

class Question(models.Model):
    question_text = models.Charfield(max_lenght=600)
    option1 = models.Charfield(max_lenght=200)
    option2 = models.Charfield(max_lenght=200)
    option3 = models.Charfield(max_lenght=200)
    option4 = models.Charfield(max_lenght=200)
class Answer(models.Model):


