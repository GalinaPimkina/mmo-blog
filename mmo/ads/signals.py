from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comment, Post


@receiver(post_save, sender=Comment)
def new_comment(sender, instance, created, **kwargs):
    '''будет срабатывать, когда создан новый отклик'''

    post = Post.objects.get(author=instance.destination_user, comment__id=instance.id)

    if created:
        send_mail(
            subject='Новый отклик',
            message=f'У вас новый отклик на сайте к объявлению: {post}',
            from_email=None,
            recipient_list=[post.author.email],
            fail_silently=False,
        )

@receiver(post_save, sender=Comment)
def new_comment(sender, instance, **kwargs):
    '''будет срабатывать, когда получатель отклика на него ответил'''

    post = Post.objects.get(author=instance.destination_user, comment__id=instance.id)

    if instance.processed:
        send_mail(
            subject='You comment was processed',
            message=f'{post.author} processed your comment: {instance}',
            from_email=None,
            recipient_list=[instance.author.email],
            fail_silently=False,
        )


