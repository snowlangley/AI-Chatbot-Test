# Flask OpenAI Interaction App

This is a simple Flask web application that takes user input through a web form, sends it to the OpenAI API (specifically, the Chat Completions endpoint), and displays the AI's response back on the web page.

## Setup

1. **Clone or download the code.**
2. **Create and activate a virtual environment (recommended):**
    Using a virtual environment isolates project dependencies.

    ```bash
    # On Windows (cmd.exe or PowerShell)
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux (bash or zsh)
    # python3 -m venv venv
    # source venv/bin/activate
    ```

    (Your terminal prompt might change to indicate the environment is active, e.g., showing `(venv)`)

3. **Install dependencies (inside the activated environment):**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API Key:**
    - Create a file named `.env` in the project root directory (`c:\Users\username\Documents\projectfolder`).
    - Add your OpenAI API key to the `.env` file like this:

        ```env
        OPENAI_API_KEY="your_actual_api_key_here"
        ```

    - Replace "your_actual_api_key_here" with your real API key (keeping the quotes).
    - **Save the `.env` file.**

    **Important:** Ensure you have created the `.env` file with your valid OpenAI API key before running the app. The application needs this key to communicate with OpenAI.

## Running the App

1. **Make sure your virtual environment is activated.** (See step 2 in Setup).

2. **Run the Flask development server (inside the activated environment):**

    ```bash
    python app.py
    ```

    Or, using the Flask CLI:

    ```bash
    flask run
    ```

3. **Open your web browser** and navigate to `http://127.0.0.1:5000` (or the address provided in the terminal).

4. **Enter your prompt** in the text area and click "Submit" to get a response from the AI.
