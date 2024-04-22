from crewai import Task
from file_io import save_markdown

class BloggerTasks():
    # def content_strategy_task(self, agent, topic):    
    def content_strategy_task(self, agent):
        return Task(
            description="""Work with the researcher to find a trending topic for a blog post and develop a content strategy.""",
            agent=agent,            
            expected_output="""A markdown-formatted content strategy, including target audience, key themes, and messages. 
                Example Output:
                '## Content Strategy for "{topic}"\\n\\n
                **Target Audience:** ...\\n\\n
                **Key Themes:**\\n
                - Theme 1...\\n
                - Theme 2...\\n\\n
                **Key Messages:**\\n
                - Message 1...\\n
                - Message 2...\\n\\n'
            """,
            callback=save_markdown
        )

    def research_and_write_task(self, agent, context):
        return Task(
            description='Research and write the blog post based on the content strategy.',
            agent=agent,
            context=context,
            expected_output="""A well-researched and engaging blog post in simple markdown format, following the content strategy.
                Example Output:
                '# {Blog Post Title}\\n\\n
                {Blog post content...}\\n\\n
                ## {Subheading 1}\\n\\n
                {Content for subheading 1...}\\n\\n
                ## {Subheading 2}\\n\\n
                {Content for subheading 2...}\\n\\n'
            """
        )

    def edit_post_task(self, agent, context):
        return Task(
            description='Edit the blog post for clarity, grammar, style, and coherence',
            agent=agent,
            context=context,
            expected_output="""An edited version of the blog post in markdown format, with improvements in clarity, grammar, style, and coherence.
                Example Output:
                '# {Updated Blog Post Title}\\n\\n
                {Updated blog post content...}\\n\\n
                ## {Updated Subheading 1}\\n\\n
                {Updated content for subheading 1...}\\n\\n
                ## {Updated Subheading 2}\\n\\n
                {Updated content for subheading 2...}\\n\\n'
            """,
            callback=save_markdown
        )

    def build_blog_post_task(self, agent, context):
        return Task(
            description='Build the blog post in the content management system',
            agent=agent,
            context=context,
            expected_output="""A blog post built in the content management system, including text, images, links, and formatting.
                Example Output:
                '## {Blog Post Title}\\n\\n
                {Blog post content...}\\n\\n
                ![Image 1](https://example.com/image1.jpg)\\n\\n
                [Link 1](https://example.com/link1)\\n\\n'
            """
        )

    def publish_post_task(self, agent, context):
        return Task(
            description='Publish the blog post on the website',
            agent=agent,
            context=context,
            expected_output="""A published blog post on the website, with a URL and metadata for search engines.
                Example Output:
                'Published: {Blog Post Title}\\n
                URL: https://example.com/blog-post\\n
                Meta Description: {Meta description for search engines}\\n'
            """
        )

    def optimize_post_task(self, agent, context):
        return Task(
            description='Optimize the blog post for search engines',
            agent=agent,
            context=context,
            expected_output="""An SEO-optimized version of the blog post in markdown format, with suggested keywords and meta descriptions.
                Example Output:
                '# {SEO-Optimized Blog Post Title}\\n\\n
                {SEO-optimized blog post content...}\\n\\n
                **Suggested Keywords:** keyword1, keyword2, keyword3\\n\\n
                **Meta Description:** {SEO-optimized meta description}\\n\\n'
            """
        )

    def provide_visuals_task(self, agent, context):
        return Task(
            description="""Provide 3 original photographs or illustrations for the blog post. 
                The style should be consistent across all images generated for the blog post""",
            agent=agent,
            context=context,
            expected_output="""A list of image URLs or base64-encoded images that are relevant to the blog post content.
                Example Output:
                [
                    'https://example.com/image1.jpg',
                    'https://example.com/image2.png',
                    'data:image/jpeg;base64,...'
                ]
            """
        )

    def plan_social_media_promotion_task(self, agent, context):
        return Task(
            description='Plan the promotion of the blog post on social media',
            agent=agent,
            context=context,
            expected_output="""A markdown-formatted social media promotion plan, including platform-specific post content and hashtags.
                Example Output:
                '## Social Media Promotion Plan\\n\\n
                **Twitter:**\\n
                - Tweet 1: {Tweet content} #hashtag1 #hashtag2\\n
                - Tweet 2: {Tweet content} #hashtag1 #hashtag3\\n\\n
                **Facebook:**\\n
                - Post 1: {Facebook post content}\\n
                - Post 2: {Facebook post content}\\n\\n
                **LinkedIn:**\\n
                - Post 1: {LinkedIn post content}\\n
                - Post 2: {LinkedIn post content}\\n\\n'
            """
        )