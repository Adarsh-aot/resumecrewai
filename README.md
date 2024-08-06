# Crewai Resume Builder

This code creates a Crew of two agents, a Research Specialist and a Resume Writer, to automate the process of researching job requirements and writing a tailored resume based on the provided information.

## Features

1. **Job Research**: The Research Specialist agent gathers comprehensive information about job skills, projects, and requirements based on the provided job title, location, and education.

2. **Resume Writing**: The Resume Writer agent crafts a compelling and tailored resume using the research findings and the employee's name, job title, location, and education.

3. **Output**: The final resume is saved in Markdown format (`resume.md`).

## Usage

1. Install the required dependencies:
   - `crewai`
   - `langchain_groq`
   - `langchain.tools`

2. Set your API key for the language model (`ChatGroq`).

3. Customize the job details and employee information as needed:
   ```python
   result = resume_crew.kickoff({
       'job_title': 'Software Engineer',
       'name' : 'John Doe',
       'location' : 'San Francisco, CA' ,
       'education' : 'University of California, Berkeley'
   })
   ```

4. Run the code to generate the resume.

5. The generated resume will be saved in `resume.md` file.

## Customization

You can customize the behavior of the agents by modifying the following parameters:

- `role`: The role of the agent.
- `goal`: The goal or purpose of the agent.
- `backstory`: The background story or context of the agent.
- `verbose`: Determines the verbosity of the agent's output.
- `allow_delegation`: Specifies whether the agent can delegate tasks to other agents.
- `tools`: The tools available to the agent for performing tasks.
- `llm`: The language model used by the agent.
- `output_file`: The file where the agent's output will be saved.

You can also modify the task descriptions and expected outputs to suit your specific needs.

## Dependencies

- `crewai`
- `langchain_groq`
- `langchain.tools`

## License

This project is licensed under the [MIT License](LICENSE).
