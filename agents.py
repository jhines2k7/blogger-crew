from crewai import Agent
from tools.search_tools import SearchTools


class BloggerCrewAgents():
    def content_strategist_agent(self):
        return Agent(
            role='ContentStrategist',
            goal='Plan the overall content strategy for the blog post',
            backstory="""With a deep understanding of the target audience and a keen sense of what resonates, you
            develop themes and messages that engage and inform readers.""",
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )

    def writer_agent(self):
        return Agent(
            role='Writer',
            goal='Research and write the blog post',
            backstory="""As a skilled wordsmith, you craft compelling narratives that captivate readers, ensuring
            the content is well-researched, engaging, and tailored to the audience.""",
            tools=[SearchTools.search_internet],
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
            post's visibility, researching keywords and suggesting changes to boost rankings.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def photographer_illustrator_agent(self):
        return Agent(
            role='PhotographerIllustrator',
            goal='Provide original photographs or illustrations for the blog post',
            backstory="""As a visual artist, you capture or create unique images that enrich the content, giving it
            a distinctive look and feel that sets it apart.""",
            verbose=True,
            allow_delegation=True,
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

    def project_manager_agent(self):
        return Agent(
            role='ProjectManager',
            goal='Oversee the blog post project and ensure smooth collaboration',
            backstory="""As a skilled coordinator, you manage the workflow, keep the team on track, and solve any
            issues that arise, ensuring the project is completed successfully.""",
            verbose=True,
        )