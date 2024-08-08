from django.shortcuts import render
from .models import Question, Choice
from django.http import HttpResponse


def index(request):
    # questions = Question.objects.all()
    # return HttpResponse(question.question_text for question in questions)
    return render(request, 'polls/index.html')

def choice_view(request):
    choices = Choice.objects.all()
    return HttpResponse(choice.choice_text for choice in choices)

