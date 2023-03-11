from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hello/', views.hello, name='hello'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add/', views.add_question, name='add_question'),
    path('update/<int:question_id>/', views.update_question, name='update_question'),
]
# async
urlpatterns += [
    # path('async/add/', views.add_question_async, name='add_question_async'),
    path('async/', views.index_async, name='index_sync'),
    path('async/hello/', views.hello_async, name='hello_async'),
]