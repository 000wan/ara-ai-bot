# ara-ai-bot

## Project Description
The "ara-ai-bot" is a comment bot designed for the KAIST community Ara. It uses a Large Language Model (LLM) to generate relevant and context-aware comments on posts within the Ara community.

## Features
- Automated comment generation using LLM (Google Gemini Pro)
- Integration with the Ara api for fetching and posting comments
- Customizable prompts for comment generation

## Project Architecture
![Flowchart](https://github.com/000wan/ara-ai-bot/assets/87213416/acbe6897-e292-4601-92b9-147fbc55cef8)

## Prerequisites
- Python 3.10
- Pipenv for dependency management
- [Google AI API Key](https://makersuite.google.com/app/apikey)
- Ara API Host and Session ID

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/000wan/ara-ai-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ara-ai-bot
   ```
3. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```

## Configuration
1. Create a `.env` file in the project root.
2. Add the following environment variables:
  ```sh
  GOOGLE_API_KEY= # Google AI API Key
  ARA_API_HOST= # ARA API Host (ex: https://newara.dev.sparcs.org)
  ARA_API_SESSION= # ARA API Session ID
  ```
3. Modify `prompt.txt` to customize the comment generation prompt.

## Running the Bot
1. Activate the Pipenv shell:
   ```bash
   pipenv shell
   ```
2. Run the bot:
   ```bash
   make run <article_id>
   ```

## Testing
- Run `test.py` to test the comment generation for a specific article:
  ```bash
  make test <article_id>
  ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
