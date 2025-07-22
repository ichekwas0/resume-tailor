from pydantic import BaseModel
from agents import Agent
from typing import Optional

EXTRACT_INFO_PROMPT = (
    "You are a helpful assistant that extracts key information from a user's resume"
    "The resume is provided in PDF or DOCX format. The extracted information will be used"
    "to tailor the resume to a specific job role. Use the provided Pydantic model to structure your output."
)

class ResumeInfoOutput(BaseModel):
    experience: list[str]
    education: list[str]
    job_titles: list[str]
    soft_skills: Optional[list[str]]
    hard_skills: Optional[list[str]]
    professional_summary: Optional[str]
    
get_info_agent = Agent(
    name="get info agent",
    instructions=EXTRACT_INFO_PROMPT,
    model='gpt-4o-mini',
    output_type=ResumeInfoOutput
)



