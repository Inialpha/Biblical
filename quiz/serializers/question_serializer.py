from rest_framework import serializers
from ..models import Question  # Adjust the import based on your project structure

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'category', 'difficulty']
