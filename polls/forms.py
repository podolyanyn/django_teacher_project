from django import forms

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='question text', max_length=200, min_length=10)
    pub_date = forms.DateTimeField(label='date  published')