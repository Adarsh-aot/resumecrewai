from crewai import Agent, Task, Crew
import os
from langchain_groq import ChatGroq
from langchain.tools import DuckDuckGoSearchRun

# Initialize the language model and search tool
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key="",
)
search_tool = DuckDuckGoSearchRun()

# Create the Research Agent
research_agent = Agent(
    role='Research Specialist',
    goal='Gather comprehensive information about job skills, projects, and requirements from {job_title} {location} {education}',
    backstory='You are an expert in job market research and skill analysis.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# Create the Resume Writing Agent
writing_agent = Agent(
    role='Resume Writer',
    goal='Craft a compelling and tailored resume based on research and name of the employee {name} {job_title} {location} {education}',
    backstory='You are a professional resume writer with years of experience in creating impactful resumes.',
    verbose=True,
    allow_delegation=False,
    llm=llm ,
    output_file = "resume.docx"
)

# Define the research task
research_task = Task(
    description='''
    Research the following:
    1. Key skills required for the job role
    2. Common projects or achievements in the field
    3. Industry-specific keywords and buzzwords
    4. Current trends in the job market for this role
    Compile your findings in a structured format.
    ''',
    expected_output='skills : python , ...',
    agent=research_agent
)

# Define the resume writing task
writing_task = Task(
    description='''
    dont genrate data that not needed
    Using the research provided, create a tailored resume:
    1. Organize information into standard resume sections (Summary, Experience, Skills, Education , projects , certifications , hobbies , and awards) 
    2. Highlight key achievements and skills relevant to the job
    3. Use industry-specific language and keywords
    4. Ensure the resume is concise, impactful, and ATS-friendly
    5. Save the final resume as 'resume.md'
    Provide a summary of the resume structure and content.
    ''',
    expected_output = "must be in markdown format",
    agent=writing_agent ,
    output_file = "resume.md"
)

# Create the crew
resume_crew = Crew(
    agents=[research_agent, writing_agent],
    tasks=[research_task, writing_task],
    verbose=2
)

# Run the crew
result = resume_crew.kickoff({
    'job_title': 'Software Engineer',
    'name' : 'John Doe',
    'location' : 'San Francisco, CA' ,
    'education' : 'University of California, Berkeley'})

print(result)