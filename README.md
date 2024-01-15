# Concept Evaluation System

Note: Currently, this only produces questions based on the uploaded blog. Working on automating evaluation of answers.

You can find the deployed version of the app here: [https://evalsystem.onrender.com](https://evalsystem.onrender.com).

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

5. Create a .env file and add the OPENAI_API_KEY. The key is in the mail.

```python
OPENAI_API_KEY = "YOUR_API_KEY"
```

6. Run the server

```bash
flask run
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
