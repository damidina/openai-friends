# OpenAI Chat Application

This is a simple web application that interacts with the OpenAI API to generate responses based on user prompts.

## Prerequisites

- Python 3.6 or higher
- zsh shell (for running the setup script)

## Setup and Running the Application

1. Clone this repository or download the files to your local machine.

2. Open a terminal and navigate to the directory containing the application files.

3. Make the setup script executable by running:
   ```
   chmod +x setup.sh
   ```

4. Run the setup script:
   ```
   ./setup.sh
   ```
   This script will:
   - Create a Python virtual environment
   - Set up the necessary files (app.py and index.html)
   - Start the Python server

5. Once the server is running, you should see a message like:
   ```
   Server running on port 8900
   ```

6. Open a web browser and go to:
   ```
   http://localhost:8900
   ```

7. You should now see the OpenAI Chat interface. Enter a prompt in the text area and click "Send" to get a response from the AI.

## Note

The API key is currently hardcoded in the `app.py` file. For security reasons, it's recommended to use environment variables or a secure key management system in a production environment.

## Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where the server is running.

