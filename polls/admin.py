from django.contrib import admin

from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["pub_date", "question_text"]
    list_display = ["question_text", "pub_date"]
    ordering = ["pub_date"]
    search_fields = ["question_text"]


class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ["question", "choice_text", "votes"]
    list_display = ["choice_text"]
    ordering = ["votes"]
    search_fields = ["choice_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
