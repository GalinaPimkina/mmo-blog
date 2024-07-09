from django.core.mail import  EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile
from .models import Comment, Post, News


@receiver(post_save, sender=Comment)
def new_comment(sender, instance, created, **kwargs):
    '''будет срабатывать, когда создан новый отклик'''

    post = Post.objects.get(author=instance.destination_user, comment__id=instance.id)

    if created:
        subject = 'У вас новый отклик'
        text = f'У вас новый отклик'
        html = (
            f'Чтобы посмотреть подробнее, перейдите по <a href="http://127.0.0.1:8000/comment/{instance.id}/">ссылке</a>'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[post.author.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()


@receiver(post_save, sender=Comment)
def new_comment(sender, instance, **kwargs):
    '''будет срабатывать, когда получатель отклика на него ответил'''

    if instance.processed: #если отклик обработан
        subject = 'На ваш отклик ответили'
        text = 'На ваш отклик ответили'
        html = (
            f'Проверить статус <a href="http://127.0.0.1:8000/comment/{instance.id}/">отклика</a>'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[instance.author.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()


@receiver(post_save, sender=News)
def new_news(sender, instance, **kwargs):
    '''срабатывает, когда создана новость. рассылается всем пользователям'''

    users = Profile.objects.all()

    for user in users:
        subject = f'{instance.title}'
        text = f'{instance.title}'
        html = (
            f'Новая статья на сайте.  <a href="http://127.0.0.1:8000/news/{instance.news_slug}/">Подробнее</a>...'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()


@receiver(post_save, sender=Post)
def new_news(sender, instance, **kwargs):
    '''срабатывает, когда создано объявление конкретной категории.
    рассылается только подписчикам категории'''

    users = Profile.objects.filter(subscribe__category=instance.category)

    for user in users:
        subject = f'{instance.title}'
        text = f'{instance.title}'
        html = (
            f'На сайте выложили объявление из ваших подписок.  <a href="http://127.0.0.1:8000/post/{instance.post_slug}/">Подробнее</a>...'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()