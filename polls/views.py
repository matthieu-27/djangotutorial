from django.http import HttpRequest, HttpResponse
from .models import Question
from django.template import loader


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def all_polls(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/all.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))
