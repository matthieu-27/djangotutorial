from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all/", views.all_polls, name="all"),
    path("<int:question_id>/", views.detail, name="details"),
]
