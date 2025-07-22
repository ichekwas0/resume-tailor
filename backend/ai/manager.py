from agents import Runner
from .extractresume import extract
from .getresumeinfo import get_info_agent, ResumeInfoOutput
from .tailorresumeagent import tailor_agent
from .sendmail import send_mail
from .googledoc import create_google_doc_async
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class ResumeManager:
       
    async def run(self, resume, job_description):
        get_resume_str = await sync_to_async(extract)(resume)
        get_resume_info = await self.get_resume_info(get_resume_str)
        tailored_resume = await self.tailor_resume(get_resume_info, job_description)
        google_doc = await create_google_doc_async(tailored_resume)
        await sync_to_async(send_mail)(google_doc['url'])
        return {"result": "email sent"}
    
        
    async def get_resume_info(self, resume_str):
        result = await Runner.run(get_info_agent, resume_str)
        return result.final_output_as(ResumeInfoOutput)
    
    
    async def tailor_resume(self, resume_info:BaseModel, job_description: str):
        resume_info_json = resume_info.model_dump_json()
        user_input = [{"content": resume_info_json, "role": "user"}, {"content": job_description, "role": "user"}]
        result = await Runner.run(tailor_agent, user_input)
        return result.final_output
