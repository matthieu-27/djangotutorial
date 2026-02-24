from django.http import HttpRequest, HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request: HttpRequest) -> HttpResponse:
    question_list = Question.objects.order_by("-pub_date")[:3]
    template = loader.get_template("polls/index.html")
    context = {"question_list": question_list}
    return HttpResponse(template.render(context, request))


def all_polls(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")
    template = loader.get_template("polls/all.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = Question.objects.get(id=question_id)
    choices = question.get_choices()
    template = loader.get_template("polls/detail.html")
    context = {"question_id": question_id, "choices": choices}
    return HttpResponse(template.render(context, request))


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
