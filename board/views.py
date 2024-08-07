from django.shortcuts import render
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-created_date')
    
    context = {
        'question_list': question_list
    }

    return render(request, 'board/question_list.html', context)