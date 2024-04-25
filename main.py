import os

from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import BloggerCrewAgents
from tasks import BloggerTasks
from dotenv import load_dotenv

load_dotenv()

# Initialize the agents and tasks
agents = BloggerCrewAgents()
tasks = BloggerTasks()

gpt4 = ChatOpenAI(
    model="gpt-4-turbo"
)

# Instantiate the agents
content_strategist = agents.content_strategist()
writer = agents.writer()
editor = agents.editor()
researcher = agents.researcher()
social_media_manager = agents.social_media_manager()
photographer = agents.photographer()
seo_specialist = agents.seo_specialist()
web_developer = agents.web_developer()

# Instantiate the tasks
develop_content_strategy = tasks.develop_content_strategy(content_strategist)
write_blog_post = tasks.write_blog_post(writer, [develop_content_strategy])
edit_blog_post = tasks.edit_blog_post(editor, [write_blog_post])
develop_social_media_plan = tasks.develop_social_media_plan(social_media_manager, [edit_blog_post, develop_content_strategy])
source_photographs = tasks.source_photographs(photographer, [edit_blog_post])
optimize_for_search = tasks.optimize_for_search(seo_specialist, [edit_blog_post, develop_content_strategy])
convert_to_html = tasks.convert_to_html(web_developer, [optimize_for_search, source_photographs])

crew = Crew(
    agents=[
        content_strategist, 
        writer, 
        researcher, 
        editor, 
        social_media_manager, 
        photographer,
        web_developer,
        seo_specialist],
    tasks=[develop_content_strategy, 
           write_blog_post, 
           edit_blog_post,
           develop_social_media_plan,
           source_photographs,
           optimize_for_search,
           convert_to_html
           ],
    process=Process.hierarchical,
    manager_llm=gpt4,
    verbose=2,
    max_rpm=10000
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