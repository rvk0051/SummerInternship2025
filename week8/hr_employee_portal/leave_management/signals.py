from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Leave
from django.conf import settings

@receiver(post_save, sender=Leave)
def send_leave_status_email(sender, instance, created, **kwargs):
    """
    This signal gets triggered whenever a Leave object is saved.

    If the Leave was just created (i.e. `created=True`), we skip sending email.
    If the Leave is updated and status becomes APPROVED or REJECTED,
       then we send an email to the employee.
    """

    if created:
        return  # Skip email on creation; send only on status change

    if instance.status in ['APPROVED', 'REJECTED']:
        try:
            send_mail(
                subject=f"Your leave has been {instance.status.lower()}",
                message=(
                    f"Hello {instance.employee.username},\n\n"
                    f"Your leave request from {instance.start_date} to {instance.end_date} "
                    f"has been {instance.status.lower()} by your senior or admin.\n\n"
                    f"Regards,\nHR Team"
                ),
                from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings.py
                recipient_list=[instance.employee.email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"[Signal Error] Email sending failed: {str(e)}")
