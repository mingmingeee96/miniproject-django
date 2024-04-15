from django.shortcuts import render, redirect
from .models import Survey, Question, Answer
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Count
import plotly.express as px
import plotly.io as pio
import pandas as pd

# Create your views here.
def survey_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age_group = request.POST.get('age_group')
        survey = Survey.objects.create(name=name, gender=gender, age_group=age_group)
        request.session['survey_id'] = survey.id
        return redirect('question')
    return render(request, 'survey.html')

def question_view(request):
    if 'survey_id' not in request.session:
        return redirect('survey')
    
    survey_id = request.session['survey_id']
    survey = Survey.objects.get(id=survey_id)
    questions = Question.objects.filter(is_active=True)
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page', 1)

    if request.method == 'POST':
        current_page_number = request.POST.get('page', page_number)
        question_id = request.POST.get('question_id')
        current_question = Question.objects.get(id=question_id)
        response = request.POST.get('response')
        
        Answer.objects.create(survey=survey, question=current_question, chosen_answer=response)

        page_obj = paginator.get_page(current_page_number)
        if page_obj.has_next():
            next_page_number = page_obj.next_page_number()
            return HttpResponseRedirect(f'?page={next_page_number}')
        else:
            del request.session['survey_id']
            return redirect('result')
    else:
        page_obj = paginator.get_page(page_number)

    return render(request, 'question.html', {'questions': page_obj})

def result_view(request):
    age_group_counts = Survey.objects.values('age_group').annotate(count=Count('age_group')).order_by('age_group')

    # Plotly 차트 데이터 생성
    data = {
        'age_group': [item['age_group'] for item in age_group_counts],
        'counts': [item['count'] for item in age_group_counts]
    }

    fig = px.pie(data, values='counts', names='age_group', title='응답자 연령')

    # 차트를 HTML로 변환
    pie_chart_html = pio.to_html(fig, full_html=False, default_height='500px', default_width='500px')

    results = Answer.objects.values('question__content', 'survey__age_group', 'chosen_answer').order_by('question__content', 'survey__age_group', 'chosen_answer')

    charts_html = []

    for question in Question.objects.filter(is_active=True):
        question_results = Answer.objects.filter(question=question).values('survey__age_group', 'chosen_answer', 'survey__gender').annotate(count=Count('id')).order_by('survey__age_group', 'chosen_answer', 'survey__gender')

        if question_results.exists():
            df = pd.DataFrame(list(question_results))

            # 응답 옵션별 총 응답 수 계산
            total_responses = df['count'].sum()
            # 비율 계산
            df['percentage'] = df['count'] / total_responses * 100
            # 비율을 포함한 텍스트 생성
            df['text'] = df['survey__age_group'] + ' (' + df['percentage'].round(1).astype(str) + '%)'
            df['chosen_answer'] = df['chosen_answer'].replace({'0': '아니오', '1': '예'})
            df['survey__gender'] = df['survey__gender'].replace({'male': '남성', 'female': '여성'})
            fig = px.bar(df, x='chosen_answer', y='count', color='survey__gender', barmode='group', text='text', title=f'질문: {question.content}', labels={'count':'응답 수', 'chosen_answer':'응답', 'survey__gender':'성별'})
            chart_html = pio.to_html(fig, full_html=False, default_height='500px', default_width='500px')
            charts_html.append(chart_html)

    return render(request, 'result.html', {'pie_chart_html': pie_chart_html, 'charts_html': charts_html})