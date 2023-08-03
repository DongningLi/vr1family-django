from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender="app.DonorInformation")
def on_donor_created(sender, instance, created, **kwargs):
    if created:
        msg_plain = render_to_string('email/donor_registration.txt', {
                                     'name': instance.full_name, 'donor_id': instance.pk})
        send_mail(
            "Your donor registration is confirmed!",
            msg_plain,
            "noreply@vr1family.org.au",
            [instance.email],
            fail_silently=False,
        )


@receiver(post_save, sender="app.RecipientInformation")
def on_recipient_created(sender, instance, created, **kwargs):
    if created:
        msg_plain = render_to_string('email/recipient_registration.txt', {
                                     'name': instance.full_name, 'recipient_id': instance.pk})
        send_mail(
            "Your recipient registration is confirmed!",
            msg_plain,
            "noreply@vr1family.org.au",
            [instance.email],
            fail_silently=False,
        )
