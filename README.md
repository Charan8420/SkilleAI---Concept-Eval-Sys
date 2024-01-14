# Concept Evaluation System

Note: Currently, this only produces questions based on the uploaded blog. Working on automating evaluation of answers.

### Table of Contents

-   [Description](#description)
-   [Tech Stack](#tech-stack)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)

## Description

CES(Concept Evaluation System) is a system that can evaluate the answers of students automatically, after they have read a blog and answered the questions based on the blog. The system will generate questions based on the blog, and the answers will be evaluated based on the concepts that the question is based on.

Uses **OpenAI's default(GPT-3.5-turbo-instruct) model** to generate the questions.

## Tech Stack

-   Flask
-   Langchain
-   OpenAI API

## Installation

1. Clone the repository

```bash
git clone https://github.com/Charan8420/Concept-Evaluation-System.git
```

2. Create a virtual environment

```bash
python -m venv ces
```

3. Activate the virtual environment

```bash
source ces/bin/activate
```

4. Install the required packages

```bash
pip install -r requirements.txt
```

5. Create a file called config.py in the application folder and add the OPENAI_API_KEY. The key is in the mail.

```python
OPENAI_API_KEY = "YOUR_API_KEY"
```

6. Run the server

```bash
flask run
```

7. Optional: Instead of Step-5, you can also run the example1.py or example2.py file with a preloaded blog to save time. Note: You must be in the root folder to run the example files.

```bash
python example1.py
```

## Usage

1. Upload a coding blog (.txt file)
2. Answer the questions based on the blog

## Project Structure

```bash
SkilleAI - Concept Eval Sys (root folder)
├── app.py
├── blog1.txt
├── example1.py
├── example2.py
├── README.md
├── requirements.txt
├── application
│   ├── __init__.py
│   ├── config.py (contains the secret key. Not uploaded to github)
│   ├── llm.py
│   ├── template.py
│   ├── views.py
│   ├── templates
│   │   ├── index.html
```
