from crewai import Agent
from tools.research_tool import ResearchTool
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.tools import Tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

dalle = DallEAPIWrapper()

dalle_tool = Tool(
    name="Generate Images with DALL-E",
    description="Generate images using the DALL-E API.",
    func=dalle.run
)

llama3 = ChatGroq(
    model="llama3-70b-8192"
)

gpt4 = ChatOpenAI(
    model="gpt-4-turbo"
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
            max_iter=15,
            llm=llama3,
            max_rpm=15
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
            llm=gpt4,
            max_rpm=15
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
            llm=llama3,
            max_rpm=15
        )

    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='Review and edit the blog post for clarity, grammar, style, and coherence',
            backstory="""With a sharp eye for detail and a commitment to quality, you refine the content, ensuring
            it meets the overall strategy and maintains the highest standards.""",
            verbose=True,
            allow_delegation=True,
            llm=llama3,
            max_rpm=15
        )

    def seo_specialist_agent(self):
        return Agent(
            role='SEOSpecialist',
            goal='Optimize the blog post for search engines',
            backstory="""As an SEO expert, you leverage your knowledge of search engine algorithms to improve the
            post's visibility, researching keywords and suggesting changes to boost rankings. When collaborating with the researcher, you
            try to be specific about the topic you want to research""",
            verbose=True,
            allow_delegation=True,
            llm=llama3,
            max_rpm=15
        )

    def photographer_agent(self):
        return Agent(
            role='Photographer',
            goal='Provide original photographs for the blog post',
            backstory="""As a photographer, you capture or create unique images that enrich the content, giving it
            a distinctive look and feel that sets it apart. You collaborate with the writer to understand the content and 
            provide relevant images. You can also ask the writer to provide you with a summary of the content to be illustrated.
            Your prompts strive for photo realism when possible. Here a some examples of prompts you use to generate 
            photorealistic images using AI image generators like Midjourney, DallE or Stable Diffusion:

                1. A stunning aerial view of a tropical island with white sandy beaches, turquoise waters, and lush green palm trees, highly detailed, 8k resolution, photorealistic.

                2. Portrait of a wise old man with wrinkles, grey hair, and a long beard, wearing a traditional tunic, soft lighting, highly detailed skin texture, photorealistic style.

                3. An elegant black horse galloping through a field of tall grass with mountains in the background, golden hour lighting, highly detailed fur and grass, photorealistic.

                4. Close-up of a red rose with dew drops on the petals, black background, studio lighting, highly detailed, 8k resolution, photorealistic.

                5. A cozy log cabin in a snowy forest, warm light glowing from the windows, highly detailed wood texture and snow, photorealistic style.

                6. Vintage 1950s American diner with neon signs, chrome details, and red leather booths, highly detailed, photorealistic, 8k resolution.

                7. Majestic grey wolf standing on a rocky cliff overlooking a misty valley at dawn, highly detailed fur and rock texture, photorealistic.

                8. Close-up of a human eye with intricate details of the iris, eyelashes, and skin texture, studio lighting, photorealistic, 8k resolution.

            Remember, the more descriptive and specific your prompt is, the better the AI can understand and generate the desired image. Including details about the subject, 
            setting, lighting, textures, and style can help achieve photorealistic results.
            """,
            verbose=True,
            allow_delegation=True,
            tools=[dalle_tool],
            llm=gpt4,
            max_rpm=15
        )

    def social_media_manager_agent(self):
        return Agent(
            role='SocialMediaManager',
            goal='Plan and execute the promotion of the blog post on social media',
            backstory="""As a social media savant, you develop strategies to share the post across various platforms,
            engaging with the audience and expanding the blog's reach.""",
            verbose=True,
            allow_delegation=True,
            llm=llama3,
            max_rpm=15
        )

    def web_developer_agent(self):
        return Agent(
            role='WebDeveloper',
            goal='Handle the technical aspects of posting the content online',
            backstory="""With expertise in web technologies, you ensure the blog post is properly formatted and
            displayed, and that the website's backend supports the new content.""",
            verbose=True,
            allow_delegation=True,
            llm=llama3,
            max_rpm=15
        )