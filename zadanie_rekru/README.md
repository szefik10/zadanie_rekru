# AI-Powered HTML Article Generator

This project is a Python script that generates structured HTML content for an article using OpenAI's GPT-4 model. The script reads text from a file, sends it to the OpenAI API for formatting into HTML with appropriate tags and placeholders for images, and saves the formatted HTML content to a new file.

## Features

- Reads raw article content from a text file (`tekst.txt`).
- Uses OpenAI's GPT-4 to structure the content as HTML, adding tags and placeholders for images.
- Saves the generated HTML content into a new file (`artykul.html`).

## Prerequisites

- Python 3.x
- OpenAI API Key (stored in an environment file called `api_key.env`)

### Required Libraries

- `openai`
- `dotenv`

You can install the necessary libraries using:

```bash
pip install openai python-dotenv
```

## Setup Instructions

1. **Environment Variables**: Create a file named `api_key.env` in the project directory and add your OpenAI API key to it:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Input File**: Make sure the text you want to process is saved in `tekst.txt` in the same directory as the script.

## Usage

1. Run the script using:

   ```bash
   python script.py
   ```

   This will:

   - Load your OpenAI API key from `api_key.env`.
   - Read the content from `tekst.txt`.
   - Send the content to OpenAI’s GPT-4 to generate structured HTML with tags and image placeholders.
   - Save the formatted HTML output to `artykul.html`.

2. Open `artykul.html` to view the generated HTML structure of your article.

## Code Overview

- **Loading the API Key**: The script uses `dotenv` to load the OpenAI API key stored in `api_key.env`.
- **Text Processing**: It reads the content from `tekst.txt` and removes any empty lines.
- **API Request**: Sends the processed text to the OpenAI API with a prompt to structure it into HTML.
- **Saving Output**: Writes the API's response into `artykul.html`.

## Example

If the content of `tekst.txt` is:

```
This is a sample article about AI and machine learning.
It discusses various applications of AI in modern industries.
```

The output in `artykul.html` might look like:

```html
<h1>AI and Machine Learning</h1>
<p>This is a sample article about AI and machine learning...</p>
<img src="image_placeholder.png" alt="AI in industries" />
...
```

## Notes

- **Model**: The script uses the `gpt-4` model for generating the HTML.
- **Environment Variables**: Remember to secure your API key and avoid sharing it publicly.
