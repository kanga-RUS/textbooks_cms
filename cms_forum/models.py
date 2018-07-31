from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class Forum(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название форума")
    description = models.TextField(blank=True, default='')
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    creator = models.ForeignKey(User, blank=True, null=True, verbose_name="Автор форума")

    def __unicode__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.topic_set.all()])

    def last_post(self):
        if self.topic_set.count():
            last = None
            for t in self.topic_set.all():
                l = t.last_post()
                if l:
                    if not last: last = l
                    elif l.created > last.created: last = l
            return last

class Topic(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название топика")
    description = models.TextField(max_length=10000, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    created = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    creator = models.ForeignKey(User, blank=True, null=True, verbose_name="Автор топика")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    closed = models.BooleanField(blank=True, default=False)

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return max(0, self.post_set.count() - 1)

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название поста")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    creator = models.ForeignKey(User, blank=True, null=True, verbose_name="Автор поста")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    topic = models.ForeignKey(Topic)
    body = models.TextField(max_length=10000, verbose_name="Текст поста")
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.topic, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True


class ProfaneWord(models.Model):
    word = models.CharField(max_length=60)

    def __unicode__(self):
        return self.word