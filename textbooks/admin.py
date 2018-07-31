from django.contrib import admin
from .models import *

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class TextbookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Textbook._meta.fields]
    list_filter = ['title',]
    search_fields = ['author',]
    inlines = [LessonInline]
    class Meta:
        model = Textbook

class LessonAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = [field.name for field in Lesson._meta.fields]
    class Meta:
        model = Lesson

admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)