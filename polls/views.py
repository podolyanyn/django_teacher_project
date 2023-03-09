from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .forms import QuestionForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def hello(request):
    return HttpResponse("Hello, world !")

# class IndexView(LoginRequiredMixin, generic.ListView):
# class IndexView(PermissionRequiredMixin, generic.ListView):
#     permission_required = 'polls.view_question'
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'polls/question.html', {'form': form})
    else:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            question = Question(question_text=form.cleaned_data['question_text'],
                                pub_date=form.cleaned_data['pub_date'],
                                user=form.cleaned_data['user'])
            question.save()

            # redirect to a new URL:
            return render(request, 'polls/text.html', {'text': 'Thanks for new question !'})
            # return HttpResponse('Thanks for new question !')


def update_question(request, question_id):
    question=Question.objects.get(id=question_id)
    if request.user.id != question.user_id:
        return render(request, 'polls/text.html', {'text': 'This question is not your !'})

    if request.method == 'GET':
        form = QuestionForm(instance=question)
        return render(request, 'polls/question.html', {'form': form})
    else:
        form = QuestionForm(request.POST, instance=question)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return render(request, 'polls/text.html', {'text': 'Thanks for update question !'})
            # return HttpResponse('Thanks for new question !')