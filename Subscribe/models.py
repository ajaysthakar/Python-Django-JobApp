from django.db import models


NEWSLETTER_OPTION =[
    ('W','WEEKLY'),
    ('M','MONTHLY')
]
# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=False)
    last_modified = models.DateTimeField(auto_now_add=True)
    notif = models.CharField(max_length=2,choices=NEWSLETTER_OPTION, default='M')
