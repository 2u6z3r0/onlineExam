from rest_framework import serializers
from .models import Question,Exam

class ExamSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name']

class QuestionSerialzer(serializers.ModelSerializer):
    # Exam = ExamSerialzer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
        # fields = ('id','question_text','option1','option2','option3','option4','correct_option')

