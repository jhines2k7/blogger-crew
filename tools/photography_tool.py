from openai import OpenAI
from langchain.tools import tool

client = OpenAI()

class PhotographyTool():
    @tool("Creates professional photographic images for a blog post.")
    def generate_image(prompt):
        """Useful for creating professional photographic images for a blog post"""
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        return response.data[0].url
