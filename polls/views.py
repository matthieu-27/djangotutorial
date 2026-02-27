from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import F, Sum, Avg
from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "question_list"

    def get_queryset(self) -> list[Question]:
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :3
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class AllPollsView(generic.ListView):
    template_name = "polls/all.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> list[Question]:
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.order_by("-pub_date")
    

def frequency(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    choices = question.get_choices()
    total = sum([x.votes for x in choices])
    frequency = [x.votes * 100 / total for x in choices]
    return render(
        request, "polls/frequency.html", {"question": question, "frequency": frequency}
    )


def statistics(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    choices = question.get_choices()
    total_questions = len(Question.objects.all())
    total_votes = Choice.objects.aggregate(Sum("votes", default=0))
    total_choices = len(Choice.objects.all())
    average_vote = Choice.objects.aggregate(Avg("votes", default=0))
    most_popular = question.get_most_popular()
    most_popular_question = Question.objects.get(pk=most_popular['question_id'])

    last_total = 0
    all_values = []
    for i in range(1, total_questions + 1):
        q = Question.objects.get(pk=i)
        cs = q.get_choices()
        total = sum([c.votes for c in cs])
        if total > last_total:
            last_total = total
            most_popular['votes__max'] = total
        all_values.append(total)

    
    return render(
        request,
        "polls/statistics.html",
        {
            "question": question,
            "choices": choices,
            "total_questions": total_questions,
            "total_votes": total_votes['votes__sum'],
            "total_choices": total_choices,
            "average_vote": average_vote['votes__avg'],
            "most_popular": most_popular['votes__max'],
            "most_popular_question": most_popular_question,
            "least_popular": min(all_values)
        },
    )


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
