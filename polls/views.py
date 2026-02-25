from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse

from .models import Choice, Question


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
    question = get_object_or_404(Question, pk=question_id)
    template = loader.get_template("polls/detail.html")
    context = {"question": question}
    return HttpResponse(template.render(context, request))


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request: HttpRequest, question_id: int) -> HttpResponse | HttpResponseRedirect:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
