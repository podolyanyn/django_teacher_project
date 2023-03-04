from django import forms
from .models import Question

# class QuestionForm(forms.Form):
#     question_text = forms.CharField(label='question text', max_length=200, min_length=10, widget=forms.Textarea(attrs={"cols": "10", "rows": "10"}))
#     pub_date = forms.DateTimeField(label='date  published')

class QuestionForm(forms.ModelForm):
        class Meta:
            model = Question
            fields = '__all__'

