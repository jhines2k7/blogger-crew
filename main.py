import os

from crewai import Crew, Process
from langchain_anthropic import ChatAnthropic
from agents import BloggerCrewAgents
from tasks import BloggerTasks
from dotenv import load_dotenv

load_dotenv()

# Initialize the agents and tasks
agents = BloggerCrewAgents()
tasks = BloggerTasks()

claude3 = ChatAnthropic(
    model="claude-3-opus-20240229"
)

# Instantiate the agents
content_strategist = agents.content_strategist()
writer = agents.writer()
editor = agents.editor()
researcher = agents.researcher()
social_media_manager = agents.social_media_manager()
photographer = agents.photographer()
seo_specialist = agents.seo_specialist()

# Instantiate the tasks
content_strategy_task = tasks.content_strategy_task(content_strategist)
research_and_write_task = tasks.research_and_write_task(writer, [content_strategy_task])
edit_post_task = tasks.edit_post_task(editor, [research_and_write_task])
social_media_plan_task = tasks.social_media_plan_task(social_media_manager, [edit_post_task])
photography_task = tasks.photography_task(photographer, [edit_post_task])
seo_optimization_task = tasks.seo_optimization_task(seo_specialist, [edit_post_task])

crew = Crew(
    agents=[content_strategist, writer, researcher, editor, social_media_manager, photographer, seo_specialist],
    tasks=[content_strategy_task, 
           research_and_write_task, 
           edit_post_task, 
           social_media_plan_task, 
           photography_task,
           seo_optimization_task],
    process=Process.hierarchical,
    manager_llm=claude3,
    verbose=2
)

# clear the output_files directory
directory = "output_files"
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
        
# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)

exit()