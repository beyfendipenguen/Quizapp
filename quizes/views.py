from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = "quizes/main.html"


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, "quizes/quiz.html", {"obj": quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
        
    })
    
def save_quiz_view(request, pk):
    #print(request.POST)
    if request.is_ajax():
        questions = []
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')

        for k in data.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                                correct_answer = a.text
                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
    
        score *= multiplier
        Result.objects.create(quiz=quiz,user=user, score=score)

        if score >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score, 'results': results})
            