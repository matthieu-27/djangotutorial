from django import forms  # type: ignore


class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Question", max_length=200)
    choice_1 = forms.CharField(label="Choice 1", max_length=200)
    choice_2 = forms.CharField(label="Choice 2", max_length=200)
    choice_3 = forms.CharField(label="Choice 3", max_length=200, required=False)
    choice_4 = forms.CharField(label="Choice 4", max_length=200, required=False)
    choice_5 = forms.CharField(label="Choice 5", max_length=200, required=False)
