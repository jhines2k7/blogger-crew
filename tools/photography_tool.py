from openai import OpenAI
from langchain.tools import tool
from google.cloud import storage

import base64
import re

client = OpenAI()

class PhotographyTool():
    @tool("Creates professional photographic images for a blog post.")
    def generate_image(prompt, filename):
        """ 
            Useful for creating professional photographic images for a blog post
            Uploads an image to Google Cloud Storage from a base64 encoded string and filename.
        """
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            response_format="b64_json"
        )

        bucket_name = 'blogger-crew-images'

        # Initialize the GCS client
        storage_client = storage.Client.from_service_account_json('blogger-crew-google-drive-api.json')
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(filename)

        base64_image_data = response.data[0].b64_json

        # Decode the base64 image data
        image_data = base64.b64decode(base64_image_data)

        # Upload the decoded image data to GCS
        blob.upload_from_string(image_data, content_type='image/jpeg')
        
        print(f"Uploaded {filename} to {bucket_name}.")
        print(f"Public URL: {blob.public_url}")

        return blob.public_url