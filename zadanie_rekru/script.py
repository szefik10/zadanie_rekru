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
            "content": f" ARTICLE CONTENT: {text} use appropriate tags to structure the content of the article. Find places where you can place different graphics mark these places with the <img> tag and add the src="'image_placeholder.jpg'" attribute to each image add the alt attribute where you propose a prompt that can be used to generate this graphic. No CSS or JavaScript code. The returned code should contain only content to be inserted between the <body> and </body> tags. Do not include <html>,<head> or <body> tags.",
        }
    ],
    model="gpt-4o",
)

res = response.choices[0].message.content
cleaned_response = res.strip("```html\n").rstrip("```")


article = open("artykul.html","w")
article.write(cleaned_response) 
article.close()



