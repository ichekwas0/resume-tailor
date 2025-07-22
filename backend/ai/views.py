from django.shortcuts import render
from rest_framework.views import APIView
from .main import main_function
from .serializers import AITailorResumeSerializer
from users.models import MyUser
from rest_framework.response import Response
from asgiref.sync import async_to_sync


class AITailorResumeView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = self.kwargs['id']
        user = MyUser.objects.get(id=user_id)
        
        resume = user.resume
        job_description = request.data['job_description']
        
        async_to_sync(main_function)(resume, job_description)
        data = {
            "resume": resume,
            "job_description": job_description
        }
        
        serializer = AITailorResumeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(my_user=user)
        return Response({"message": "Tailored resume sent successfully."}, status=200)
