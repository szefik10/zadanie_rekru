import os
from dotenv import load_dotenv
import io
import openai
from openai import OpenAI


load_dotenv('api_key.env')
chat_api_key = os.getenv("OPENAI_API_KEY")


text = open('tekst.txt','r').readlines()
text = [x.strip() for x in text if len(x) > 1]

client = OpenAI(
    api_key=chat_api_key,
)
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Generate an HTML template for the article preview. To do this, you can develop styles and JS code that will allow you to visualize the text after pasting its code into the <body> section. The <body> section should be empty and ready for the article to be pasted. void adding any explanations or comments in your response. Just provide the code",
        }
    ],
    model="gpt-4o",
)


res = response.choices[0].message.content
cleaned_response = res.strip("```html\n").rstrip("```")


template = open("szablon.html","w")
template.write(cleaned_response) 
template.close()




