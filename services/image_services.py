from vertexai.preview.generative_models import GenerativeModel
import vertexai
import base64
import os

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

def generate_image(prompt: str):
    model = GenerativeModel("imagen-3.0-generate-001")

    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0.4}
    )

    image_bytes = response.candidates[0].content.parts[0].inline_data.data
    return base64.b64encode(image_bytes).decode("utf-8")
