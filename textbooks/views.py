from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import DeleteView, UpdateView, ListView
from .models import Textbook, Lesson
from .forms import *


class TextbookListView(ListView):
    template_name = 'textbooks/catalog.html'
    context_object_name = 'textbooks_list'

    def get_queryset(self):
        return Textbook.objects.all()

def textbook_detail(request, textbook_id):
    textbook = get_object_or_404(Textbook, id=textbook_id)
    return render(request, 'textbooks/textbook_detail.html', {'textbook': textbook})

def lesson(request, textbook_id, lesson_id):
    textbook = get_object_or_404(Textbook, id=textbook_id)
    lesson = Lesson.objects.get(id=lesson_id)
    lessons = Lesson.objects.all().filter(textbook_id=textbook_id, id=lesson_id)
    return render(request, 'textbooks/lesson.html', {'textbook': textbook, 'lesson': lesson, 'lessons': lessons})

@login_required
def add_textbook(request):
    form = TextbookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.author = request.user
        book.title = form.cleaned_data['title']
        book.text = form.cleaned_data['text']
        book.save()
        return redirect('textbooks:textbook_detail', book.id)
    return render(request, 'textbooks/add_textbook.html', {'form': form})

@login_required
def add_lesson(request, textbook_id):
    textbook = get_object_or_404(Textbook, id=textbook_id)
    form = LessonForm(request.POST or None)
    if form.is_valid():
        lesson = form.save(commit=False)
        lesson.textbook = textbook
        lesson.save()
        request.session["title"] = lesson.title
        request.session["text"] = lesson.text
        return redirect('textbooks:textbook_detail', textbook.id)
    form.initial['title'] = request.session.get('title')
    form.initial['text'] = request.session.get('text')
    return render(request, 'textbooks/add_lesson.html', {'textbook': textbook, 'form': form})

@login_required
def lesson_delete(request, textbook_id, lesson_id=None):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    lesson.delete()
    return redirect('textbooks:textbook_detail', textbook_id)

@login_required
def lesson_update(request, textbook_id, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    textbook = get_object_or_404(Textbook, id=textbook_id)
    form = LessonUpdateForm(request.POST or None, instance=lesson)
    if form.is_valid():
        lesson_form = form.save(commit=False)
        lesson_form.save()
        return redirect('textbooks:lesson', textbook_id, lesson_id)
    return render(request, 'textbooks/lesson_update.html', {'form': form, 'lesson': lesson})


