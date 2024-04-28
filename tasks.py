from crewai import Task
from crewai_tools import FileReadTool

import datetime
import textwrap

class BloggerTasks():
    def develop_content_strategy(self, agent):
        content_strategy_file = f"output_files/content_strategy.md"

        return Task(
            description=textwrap.dedent(
                """
                    Work with the researcher to find a trending topic in the video game industry 
                    for a blog post and develop a content strategy.
                """),
            agent=agent,            
            expected_output=textwrap.dedent(
                """
                    A markdown-formatted content strategy, including target audience, key themes, and messages. 
                    Example Output:
                    '## Content Strategy for "{topic}"\\n\\n
                    **Target Audience:** ...\\n\\n
                    **Key Themes:**\\n
                    - Theme 1...\\n
                    - Theme 2...\\n\\n
                    **Key Messages:**\\n
                    - Message 1...\\n
                    - Message 2...\\n\\n'
                """),
            output_file=content_strategy_file
        )

    def write_blog_post(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                    Research and write the blog post based on the content strategy.The expected wordcount for
                    this blog post is between 1000-1200 words. Remember to follow the content strategy and make 
                    the blog post engaging and informative.
                """),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                    A well-researched and engaging blog post following the content strategy in plain text format.
                """),
            tools=[
                FileReadTool(file_path='output_files/keyword_targeting_report.md'),
                FileReadTool(file_path='output_files/seo_content_brief.md')
            ],
            output_file='output_files/blog_post_draft.txt'
        )

    def edit_blog_post(self, agent, context):
        final_draft_file = f"output_files/final_draft.txt"

        return Task(
            description="""Edit the blog post for clarity, grammar, style, and coherence""",
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                    An edited version of the blog post in plain text format, with improvements in clarity, grammar, style, and coherence.
                """),
            output_file=final_draft_file,
            tools=[FileReadTool(file_path='output_files/blog_post_draft.txt')]
        )    

    def convert_to_html(self, agent, context):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        blog_post_html_file = f"output_files/blog_post-{timestamp}.html"

        return Task(
            description=textwrap.dedent(
                """
                    Take the content from the final draft of the blog post, and use it to the build the 
                    markup for the blog post including text, images, links, and formatting.
                    Do not attempt to reconstruct an entire index.html page. The resulting HTML should 
                    be a fragment that can be inserted into an existing page. The image urls will be
                    be available to you in a text file called cropped_image_urls.txt. There should be 
                    5 images in total. Don't forget to grab some text from the draft to use in the 
                    blockquote. Follow the example output very closely as a template for the HTML you 
                    generate. Do not refactor the markup. The names of the classes and html elements 
                    are necessary to ensure the blog post will be rendered properly in the browser and 
                    should not be changed.
                """),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                    The markup for the blog post, including text, images, links, and formatting.
                    The resulting HTML should be a fragment that can be inserted into an existing page.
                    Example Output:
                    <figure class="post-thumb">
                        <img width="1141px" height="723px" src="assets/images/post/single/one/single1.jpg" alt="Blog Image" />
                    </figure><!-- /.post-thumb -->
                    <div class="entry-content">
                        <p>Adipiscing elit com-modo ligula eget dolor Morlem ipsuim dolor sit amiet nec, isc
                            thua sdfk onsec tetuer adipi scing elit. Aenean commeod ligula eget dolor Cuem
                            sociis thena toquhte thigp enatibus et magnis dis partu rient montes. Morlem ipsum
                            doelor sit amet nec penatib et thjem agnis dis part urient montes. Morlem ipsum
                            dolor sit amet nerc, conseec tetuer adipiscing elit. Aenean commodo ligulaits eget
                            dolior. Aenean type massa. Cum sociis nato que pena tibus et magnis dis partu rient
                            moentes. Morlm ipsum dolor tibushrde set amet nec, consec tetuer adipiscing elit.
                            Aenean commodo ligula eget dolor.</p>
                        <p>Enatibus et magnis dis partu rient montes. Morlem ipsum doelor sit amet nec penatib
                            et thjem agnis dis part uriet montes. Morlem ipsium dolor sit amet nerc, conseec
                            tetuer adipi scing elit. Aenean commodo ligulaits eget doilior. Aenean type massa.
                            Cum sociis nato que pena tibus et magns dihtres partu rient moentes. Morlm ipsum
                            dolor set amet nec, consec tetuer adipiscing elit. Aenean comiodo ligula eget dolor.
                            magnis dis partu rient moentes. Morlm ipsum dolor set am nec, consec tetuer
                            adipiscing elit</p>
                        <div class="row image-group gutters-20">
                            <div class="col-lg-6 col-md-6">
                                <figure class="thumb">
                                    <img height="401px" width="440px" src="assets/images/post/single/one/1.jpg" alt="Img">
                                </figure>
                            </div>
                            <div class="col-lg-6 col-md-6">
                                <figure class="thumb">
                                    <img height="401px" width="440px" src="assets/images/post/single/one/2.jpg" alt="Img">
                                </figure>
                            </div>
                        </div>
                        <!--~./ end image group ~-->
                        <p>Enatibus et magnis dis partu rient montes. Morlem ipsum doelor sit amet nec penatib
                            et thjem agnis dis part uriet montes. Morlem ipsium dolor sit amet nerc, conseec
                            tetuer adipi scing elit. Aenean commodo ligulaits eget doilior. Aenean type massa.
                            Cum sociis nato que pena tibus et magns dihtres partu rient moentes. Morlm ipsum
                            dolor set amet nec, consec tetuer adipiscing elit. Aenean comiodo ligula eget dolor.
                            magnis dis partu rient moentes. Morlm ipsum dolor set am nec, consec tetuer
                            adipiscing elit</p>
                        <figure class="thumb full-image">
                            <img width="1141px" height="440px" src="assets/images/post/single/one/3.jpg" alt="Img">
                        </figure>
                        <p>Enatibus et magnis dis partu rient montes. Morlem ipsum doelor sit amet nec penatib
                            et thjem agnis dis part uriet montes. Morlem ipsium dolor sit amet nerc, conseec
                            tetuer adipi scing elit. Aenean commodo ligulaits eget doilior. Aenean type massa.
                            Cum sociis nato que pena tibus et magns dihtres partu rient moentes. Morlm ipsum
                            dolor set amet nec, consec tetuer adipiscing elit. Aenean comiodo ligula eget dolor.
                            magnis dis partu rient moentes. Morlm ipsum dolor set am nec, consec tetuer
                            adipiscing elit</p>
                        <div class="left-thumb">
                            <img height="401px" width="440px" class="alignleft" src="assets/images/post/single/one/4.jpg" alt="Img">
                            <p>Enatibus et magnis dis partu rient montes. Morlem ipsum doelor sit amet nec
                                penatib
                                et thjem agnis dis part uriet montes. Morlem ipsium dolor sit amet nerc, conseec
                                tetuer adipi scing elit. Aenean commodo ligulaits eget doilior. Aenean type
                                massa.
                                Cum sociis nato que pena tibus et magns dihtres partu rient moentes. Morlm ipsum
                                dolor set amet nec, consec tetuer adipiscing elit. Aenean comiodo ligula eget
                                dolor.
                                magnis dis partu rient moentes. Morlm ipsum dolor set am nec, consec tetuer
                                adipiscing elit</p>
                        </div>

                        <blockquote>
                            <div class="quote"><img src="assets/images/icon/quote.png" alt="Quote"></div>
                            <p>Enatibus et magnis dis partu rient montes. Morlem ipsum doelor sit amet nec
                                penatib et thjem agnis dis part uriet montes. Morlem ipsium dolor sit amet nerc,
                                conseec tetuer adipi scing elit. Aenean commodo ligulaits</p>
                        </blockquote>

                        <p>Enatibus et magnis dis partu rient montes. Morlem ipsum doelor sit amet nec penatib
                            et thjem agnis dis part uriet montes. Morlem ipsium dolor sit amet nerc, conseec
                            tetuer adipi scing elit. Aenean commodo ligulaits eget doilior. Aenean type massa.
                            Cum sociis nato que pena tibus et magns dihtres partu rient moentes. Morlm ipsum
                            dolor set amet nec, consec tetuer adipiscing elit. Aenean comiodo ligula eget dolor.
                            magnis dis partu rient moentes. Morlm ipsum dolor set am nec, consec tetuer
                            adipiscing elit</p>
                    </div>
                """),
            output_file=blog_post_html_file,
            tools=[
                FileReadTool(file_path='output_files/cropped_image_urls.txt'), 
                FileReadTool(file_path='output_files/final_draft.txt')
            ]
        )

    def source_photographs(self, agent, context):        
        return Task(
            description=textwrap.dedent(
                """
                    Provide 5 original photographs for the blog post. 
                    The style should be consistent across all images generated for the blog post
                    and one of the images will be used as the featured image. Take 
                    care to pass a descriptive and unique file name along with the prompt when you use 
                    the tool to upload the base64 encoded image to Google Cloud Storage. All files should 
                    be jpeg. These images should tell the story of the event or subject, focusing on 
                    emotional impact and aesthetic appeal. Once you have the public urls from the Google Cloud 
                    Storage bucket, provide a list of the image URLs in a text file. When writing the public 
                    urls to file use the value exactly as it is provided to you by the tool.
                """),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent("""A line separated list of image URLs for the blog post.
                Example Output:
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_1]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_2]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_3]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_4]            
            """),
            async_execution=True,
            output_file='output_files/image_urls.txt'
        )

    def crop_images(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                    You will be given a list of image URLs in a text 
                    file. Crop three of the images to a height of 
                    401px and a width of 440px, one of the images 
                    to a width of 1141px and a height of 440px and
                    one of the images should have a width of 
                    1141px and a height of 723px. 
                """),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent("""A line separated list of image URLs for the blog post.
                Example Output:
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_1]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_2]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_3]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_4]            
            """),
            tools=[FileReadTool(file_path='output_files/image_urls.txt')],
            output_file='output_files/cropped_image_urls.txt'
        )

    def develop_social_media_plan(self, agent, context):
        social_media_plan_file = f"output_files/social_media_plan.md"

        return Task(
            description="""Plan the promotion of the blog post on social media""",
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """A markdown-formatted social media promotion plan, including platform-specific post content and hashtags.
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
                """),
            async_execution=True,
            output_file=social_media_plan_file
        )

    def create_keyword_targeting_report(self, agent, context):
        return Task(
            description="""Create a keyword targeting report for the blog post""",
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """ This report should include the primary and secondary keywords that the blog post should target. 
                It provides the author with crucial insights into the focus topics and phrases that are expected to drive traffic..
                Example Output:
                '## Keyword Targeting Report for "{Blog Post Title}"\\n\\n
                **Suggested Keywords:** keyword1, keyword2, keyword3\\n\\n
                **Search Volume:** {Search volume for suggested keywords}\\n\\n'
                """),
            aysnc_execution=True,
            output_file='output_files/keyword_targeting_report.md'
        )

    def create_seo_content_brief(self, agent, context):
        return Task(
            description="""Create an SEO content brief for the blog post""",
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """ This is a comprehensive guide for the author that outlines the structure of the blog post, including 
                suggested headings, subheadings, keyword placement, recommended word count, and any specific SEO elements 
                that need to be integrated into the content. It may also include audience insights to help tailor the 
                content appropriately.
                Example Output:
                '## SEO Content Brief for "{Blog Post Title}"\\n\\n
                **Target Keywords:** keyword1, keyword2, keyword3\\n\\n
                **Meta Description:** {SEO-optimized meta description}\\n\\n'
                """),
            async_execution=True,
            output_file='output_files/seo_content_brief.md'
        )

    