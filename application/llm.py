from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from .template import template

load_dotenv()


# Token limit = 4096 tokens
def question_extraction(blog):
  llm = OpenAI(temperature=0.7, openai_api_key = os.getenv('OPENAI_API_KEY')) #GPT-3.5-turbo-instruct 
  prompt = PromptTemplate(input_variables = ['blog'], template = template)

  chain = LLMChain(llm=llm, prompt = prompt)
  response = chain.run(blog = blog)

  
  response_list = response.split('\n')[1:-1]

  return response_list



