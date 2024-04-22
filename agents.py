from crewai import Agent
from tools.research_tool import ResearchTool
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.tools import Tool

dalle = DallEAPIWrapper()

dalle_tool = Tool(
    name="Generate Images with DALL-E",
    description="Generate images using the DALL-E API.",
    func=dalle.run
)

class BloggerCrewAgents():
    def content_strategist_agent(self):
        return Agent(
            role='ContentStrategist',
            goal='Plan the overall content strategy for the blog post',
            backstory="""With a deep understanding of the target audience and a keen sense of what resonates, you
            develop themes and messages that engage and inform readers. When collaborating with the researcher, you
            try to be specific about the topic you want to research""",
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )

    def researcher_agent(self):
        return Agent(
            role='Researcher',
            goal='Conduct in-depth research on the blog post topic',
            backstory="""As a skilled researcher, you dive deep into the subject matter, gathering facts, statistics, and
            expert opinions to provide a solid foundation for the blog post.""",
            tools=[ResearchTool.perform_research],
            verbose=True,
            allow_delegation=True,
        )

    def writer_agent(self):
        return Agent(
            role='Writer',
            goal='Research and write the blog post',
            backstory="""As a skilled wordsmith, you craft compelling narratives that captivate readers, ensuring
            the content is well-researched, engaging, and tailored to the audience. When collaborating with the researcher, you
            try to be specific about the topic you want to research. You can also ask the researcher to provide you with a 
            summary of the research done so far.""",
            verbose=True,
            allow_delegation=True,
        )

    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Review and edit the blog post for clarity, grammar, style, and coherence',
            backstory="""With a sharp eye for detail and a commitment to quality, you refine the content, ensuring
            it meets the overall strategy and maintains the highest standards.""",
            verbose=True,
            allow_delegation=True,
        )

    def seo_specialist_agent(self):
        return Agent(
            role='SEOSpecialist',
            goal='Optimize the blog post for search engines',
            backstory="""As an SEO expert, you leverage your knowledge of search engine algorithms to improve the
            post's visibility, researching keywords and suggesting changes to boost rankings. When collaborating with the researcher, you
            try to be specific about the topic you want to research""",
            tools=[],
            verbose=True,
            allow_delegation=True,
        )

    def visual_media_agent(self):
        return Agent(
            role='VisualMediaArtist',
            goal='Provide original photographs or illustrations for the blog post',
            backstory="""As a visual artist, you capture or create unique images that enrich the content, giving it
            a distinctive look and feel that sets it apart. You collaborate with the writer to understand the content and 
            provide relevant images. You can also ask the writer to provide you with a summary of the content to be illustrated.
            Your prompts strive for photo realism when possible.""",
            verbose=True,
            allow_delegation=True,
            tools=[dalle_tool]
        )

    def social_media_manager_agent(self):
        return Agent(
            role='SocialMediaManager',
            goal='Plan and execute the promotion of the blog post on social media',
            backstory="""As a social media savant, you develop strategies to share the post across various platforms,
            engaging with the audience and expanding the blog's reach.""",
            verbose=True,
            allow_delegation=True,
        )

    def web_developer_agent(self):
        return Agent(
            role='WebDeveloper',
            goal='Handle the technical aspects of posting the content online',
            backstory="""With expertise in web technologies, you ensure the blog post is properly formatted and
            displayed, and that the website's backend supports the new content.""",
            verbose=True,
            allow_delegation=True,
        )