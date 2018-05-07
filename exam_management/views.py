from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import StudentExam, Exam, Question
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import generics
from .serializer import QuestionSerialzer

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
    questions=Question.objects.filter(exam__id=id).values_list('question_text', 'option1', 'option2', 'option3', 'option4','correct_option')
    question_jason = json.dumps(list(questions), cls=DjangoJSONEncoder)
    context={
        "question_list" : question_jason,
        "exam_id": id,
    }
    return render(request, "exam.html", context)

class QuestionAPIView(generics.ListAPIView):
    # lookup_field = 'exam_id'
    serializer_class = QuestionSerialzer
    def get_queryset(self):
        qs = Question.objects.all()
        exam_id = self.request.GET.get("id")
        if exam_id is not None:
            qs = Question.objects.filter(exam__id=exam_id)
        return qs
    

# def question_list(request, id):
#     if request.method == 'GET':
#         questions_list = Question.objects.filter(id=1)
#         serializer = QuestionSerialzer(question_list)
#         return JsonResponse(serializer.data)
