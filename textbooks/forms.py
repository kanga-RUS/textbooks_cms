from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        exclude = ['author']

    def clean(self):
        return self.cleaned_data

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['created_on', 'textbook']

class LessonUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lesson
        fields = ['title', 'text']