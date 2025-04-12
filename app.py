import os
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
print(f"Attempting to load key from environment...") # DEBUG PRINT 1
loaded_key = os.getenv("OPENAI_API_KEY")
print(f"Key loaded from os.getenv: {'Found key' if loaded_key else 'Not found'}") # DEBUG PRINT 2
# Optionally print a few chars of the key if found, BUT BE CAREFUL NOT TO EXPOSE THE WHOLE KEY
# if loaded_key:
#     print(f"First few chars of key: {loaded_key[:5]}...")

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = loaded_key # Use the variable we already checked
print(f"openai.api_key is set to: {'Set' if openai.api_key else 'Not set'}") # DEBUG PRINT 3

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = None
    error_text = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        if not openai.api_key:
            error_text = "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable. (Checked inside route)"
        elif not user_input:
            error_text = "Please enter some text."
        else:
            try:
                # Using the newer OpenAI client structure (v1.0.0+)
                # Ensure the client uses the key set globally or pass it explicitly
                client = openai.OpenAI(api_key=openai.api_key) # Explicitly pass key
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Or your preferred model
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input}
                    ]
                )
                response_text = response.choices[0].message.content.strip()
            except openai.AuthenticationError:
                 error_text = "Authentication Error: Check if your API key is correct and active."
            except Exception as e:
                error_text = f"An error occurred: {e}"

    return render_template('index.html', response_text=response_text, error_text=error_text)

if __name__ == '__main__':
    app.run(debug=True)
