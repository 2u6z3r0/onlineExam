from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    total_marks = models.IntegerField()
    duration = models.IntegerField(default=60)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.exam_name

    def get_absolute_url(self):
        return 'exam/%d' % self.id

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text[:15]

class StudentExam(models.Model):
    exam = models.ManyToManyField(Exam)
    student = models.ManyToManyField(User)
    completed = models.BooleanField(default=False)


class StudentExamQA(models.Model):
    exam = models.ManyToManyField(Exam)
    student = models.ManyToManyField(User)
    student_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.exam

class Result(models.Model):
    exam = models.ManyToManyField(Exam)
    student = models.ManyToManyField(User)
    score = models.IntegerField()
    percentage = models.FloatField()
