from crewai import Crew, Process
from langchain_anthropic import ChatAnthropic
from agents import BloggerCrewAgents
from tasks import BloggerTasks

from dotenv import load_dotenv
load_dotenv()

# Initialize the agents and tasks
agents = BloggerCrewAgents()
tasks = BloggerTasks()

llm = ChatAnthropic(
    model="claude-3-opus-20240229"
)

# Instantiate the agents
content_strategist = agents.content_strategist_agent()
writer = agents.writer_agent()
editor = agents.editor_agent()
researcher = agents.researcher_agent()
# project_manager_agent = agents.project_manager_agent()

# Instantiate the tasks
content_strategy_task = tasks.content_strategy_task(content_strategist)
research_and_write_task = tasks.research_and_write_task(writer, [content_strategy_task])
edit_post_task = tasks.edit_post_task(editor, [research_and_write_task])

crew = Crew(
    agents=[content_strategist, writer, researcher, editor],
    tasks=[content_strategy_task, research_and_write_task, edit_post_task],
    process=Process.hierarchical,
    manager_llm=llm,
    verbose=2
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)