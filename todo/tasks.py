import logging
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from list_tasks.celery import app

@app.task
def send_performend_mail(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
                    'Test', 
                    'test',
                    'from@gmail.com', 
                    [user.email],
                    fail_silently=False,
                )
    except UserModel.DoesNotExist:
        logging.warning("Can't find user")