from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Textbook(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='', null=True, blank=True, default='book.png')
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


    @models.permalink
    def get_absolute_url(self):
        return ('textbooks:textbook_detail', (),
                {
                    'id': self.id,
                })

    def save(self, *args, **kwargs):
        super(Textbook, self).save(*args, **kwargs)

    class Meta:
        ordering = ["title"]
        verbose_name = "Учебник"
        verbose_name_plural = "Учебники"

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    text = RichTextUploadingField(blank=True, default='', verbose_name="Текст урока")
    created_on = models.DateTimeField(auto_now_add=True)
    textbook = models.ForeignKey(Textbook, verbose_name="Учебник")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('textbooks:lesson', (),
                {
                    'lesson_id': self.id,
                })

    def save(self, *args, **kwargs):
        super(Lesson, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class Comment(models.Model):
    text = models.TextField()
    lesson = models.ForeignKey(Lesson)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.title