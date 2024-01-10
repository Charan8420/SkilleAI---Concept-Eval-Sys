template = '''
    Below is a blog that contains information related to coding.

    Your goal is to:
    - Ask coding or logical questions based on the information given in the blog
    - Make sure to group questions of same type together and in the order
    - Only ask the type of questions mentioned below

    Only use the information from the blog to ask questions.

    Do not ask generic questions. Essay type questions aren't allowed. The questions should only focus on coding as this isn't an English or History test

    The question type can ONLY be (in an order):
    1. Multiple-choice
    2. True/false
    3. Fill-in-the-blank
    4. Write a program/function

    Group questions together based on the question type. Mention question type and all the questions of that type. Then move on to next question type

    Follow the order in which the question types are mentioned above

    Some examples of questions that are approved to ask:
    - Print first 10 numbers in a fibonacci sequence.
    - What data structure is used to store a collection of key-value pairs with fast retrieval of values based on keys?
    a) Linked List
    b) Hash Table
    c) Binary Tree
    d) Stack
    - Check if two strings are anagrams.
    - A __________ is a block of code that performs a specific task and can be reused throughout a program by calling its name.
    a) Function
    b) Class
    c) Variable
    d) Module
    - In Python, a variable can be used to store both numeric values and strings interchangeably without any issues.
    a) True
    b) False


    If you feel like you don't have enough information to ask at least one question, say "There are no questions to be asked in this blog".


    Below is the blog:
    blog: {blog}

    YOUR QUESTIONS:
'''