from django.urls import path
from .views import survey_view, question_view, result_view

urlpatterns = [
    path('', survey_view, name='survey'),
    # path('survey/', question_view, name='question'),
    path('question/', question_view, name='question'),
    path('result/', result_view, name='result'),
]