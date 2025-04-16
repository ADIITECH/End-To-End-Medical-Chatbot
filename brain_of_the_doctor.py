#Step1: Setup GROQ API key
from groq import Groq
from dotenv import load_dotenv
import os
from groq import Groq  
load_dotenv()
GROQ_API_KEY = "gsk_FF6KCFxT8s3tnFz87a2aWGdyb3FYlyfdDjS84p8PMExJH5drKkJYpi"  
client = Groq(api_key=GROQ_API_KEY)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ELEVEN_API_KEY")




#Step2: Convert image to required format
import base64


#image_path="acne.jpg"

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM 
from groq import Groq

query="Is there something wrong with my face?"
model="llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content