# import spacy
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import OPENAI_API_KEY
from template import template


# Token limit = 4096 tokens
def question_extraction(blog):
  llm = OpenAI(temperature=0.7, openai_api_key = OPENAI_API_KEY) 
  prompt = PromptTemplate(input_variables = ['blog'], template = template)

  chain = LLMChain(llm=llm, prompt = prompt)
  response = chain.run(blog = blog)

  
  response_list = response.split('\n')

  return response_list



