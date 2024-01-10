template2 = '''
    Below is a blog that contains information related to coding.
    Your goal is to:
    - Ask coding questions based on the information given in the blog
    - Ask logical questions based on the information given in the blog

    Only use the information from the blog to ask questions.
    
    Do not ask generic questions. The questions should only focus on coding as this isn't an English or History test

    The question type can ONLY be:
    - Multiple-choice
    - True/false
    - Fill-in-the-blank
    - Write a program/function

    Some examples of questions that are approved to ask:
    - Write a program to print first 10 numbers in a fibonacci sequence.
    - What data structure is used to store a collection of key-value pairs with fast retrieval of values based on keys?
    - Write a function to check if two strings are anagrams.
    -

    Some examples of questions you CANNOT ask:
    - How does Python's versatility position it for future challenges and opportunities?
    - What are some key aspects of Python that make it versatile?
    - Can you explain how Python's simplicity and expressiveness make it ideal for prototyping in emerging technologies?
    - What are some of the key features that make Python a popular choice for developers?

    If you feel like you don't have enough information to ask at least one question, say "There are no questions to be asked in this blog".

    
    Below is the blog:
    blog: {blog}
    
    YOUR QUESTIONS:
'''