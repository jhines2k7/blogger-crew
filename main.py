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
content_strategist = agents.content_strategist_agent()
writer = agents.writer_agent()
editor = agents.editor_agent()
researcher = agents.researcher_agent()
social_media_manager = agents.social_media_manager_agent()
visual_media_agent = agents.visual_media_agent()

# Instantiate the tasks
content_strategy_task = tasks.content_strategy_task(content_strategist)
research_and_write_task = tasks.research_and_write_task(writer, [content_strategy_task])
edit_post_task = tasks.edit_post_task(editor, [research_and_write_task])
plan_social_media_promotion_task = tasks.plan_social_media_promotion_task(social_media_manager, [edit_post_task])
photography_task = tasks.photography_task(visual_media_agent, [edit_post_task])

crew = Crew(
    agents=[content_strategist, writer, researcher, editor, social_media_manager, visual_media_agent],
    tasks=[content_strategy_task, 
           research_and_write_task, 
           edit_post_task, 
           plan_social_media_promotion_task, 
           photography_task],
    process=Process.hierarchical,
    manager_llm=gpt4,
    verbose=2
)

# clear the output_files directory


# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)

exit()