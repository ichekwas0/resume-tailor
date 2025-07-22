from django.db import models
from users.models import MyUser


# Create your models here.
class AIResumeTailor(models.Model):
    my_user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='ai_resume_tailor')
    job_description = models.TextField()
    