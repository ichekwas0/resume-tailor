from .manager import ResumeManager
import asyncio

async def main_function(resume, job_desc):
    mgr = ResumeManager()
    await mgr.run(resume, job_desc) 
