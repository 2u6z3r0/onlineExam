# Generated by Django 2.0.4 on 2018-04-26 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=100)),
                ('total_marks', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=600)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('correct_option', models.CharField(max_length=200)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('exam', models.ManyToManyField(to='exam_management.Exam')),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('exam', models.ManyToManyField(to='exam_management.Exam')),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExamQA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ManyToManyField(to='exam_management.Question')),
                ('student_exam', models.ManyToManyField(to='exam_management.StudentExam')),
            ],
        ),
    ]
