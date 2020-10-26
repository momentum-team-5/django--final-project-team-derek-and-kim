from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import QuestionBox, AnswerBox
from .forms import QuestionForm, AnswerForm, SearchForm


def question_list(request):
    question = QuestionBox.objects.all()

    return render(request, "question_list.html", {"question": question})


def question_details(request, pk):
    question = get_object_or_404(QuestionBox, pk=pk)
    answers = question.answers.all()

    if request.method == 'GET':
        form = AnswerForm()

    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            success(request, "Answer saved!")

            return redirect(to="question_details", pk=question.pk)

        else:
            error(request, "Couldn't save your answer")

    return render(request, "question_details.html", {"question": question, "answers": answers, "form": form})


@login_required
def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()

    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            form.save()
            return redirect(to='question_list')

        else:
            error(request, "Problem with your submission.")

    return render(request, "add_question.html", {"form": form})


@login_required
def add_answer(request, pk):
    question = get_object_or_404(QuestionBox, pk=pk)

    if request.method == 'GET':
        form = AnswerForm()
        
    else:
        form = AnswerForm(data=request.POST)
    
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            form.save()
            return redirect(to='question_list')

        else:
            error(request, "Problem with your submission.")

    return render(request, "add_answer.html", {"form": form, "question": question})


@login_required
def edit_question(request, pk):
    question = get_object_or_404(QuestionBox, pk=pk)
    if request.method == 'GET':
        form = QuestionForm(instance=question)

    else:
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect(to='question_list')

    return render(request, "edit_question.html", {"form": form, "question": question})


@login_required
def delete_question(request, pk):
    question = get_object_or_404(QuestionBox, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect(to='question_list')

    return render(request, "delete_question.html", {"question": question})


def search(request):
    if request.method == "GET":
        form = SearchForm()

    elif request.method == "POST":
        form = SearchForm(data=request.POST)

    if form.is_valid():
        question = form.cleaned_data['question']
        question = QuestionBox.objects.filter(question__contains=question)

        return render(request, "search_results.html", {"question": question})

    return render(request, "search.html", {"form": form})


def add_favorite(request, pk):
    question = get_object_or_404(AnswerBox, id=pk)

    if request.user.is_authenticated:
        if question.favorites.filter(id=request.user.pk).count() == 0:
            question.favorites.add(request.user)
            success(request, "Favorite added!")

        else:
            error(request, "Only signed in users can favorite answers.")

        return redirect(to="question_list")