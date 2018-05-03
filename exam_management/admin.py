from django.contrib import admin
from .models import Exam, Question, StudentExam, StudentExamQA, Result

class ExamAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class StudentExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(StudentExam, StudentExamAdmin)

