from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import StudentExam, Exam, Question

# Create your views here.
@login_required
def home_page(request):
    user = request.user
    active_exams = Exam.objects.filter(studentexam__student__id=user.id)
    context = {
        "exam_list": active_exams
    }
    return render(request, "index.html", context)

def exam_page(request, id):
    questions=Question.objects.filter(exam__id=id)
    context={
        "question_list" : questions
    }
    print(questions)
    return render(request, "exam.html", context)
