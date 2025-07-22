from rest_framework import serializers
from .models import AIResumeTailor

class AITailorResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIResumeTailor
        fields = ['job_description']