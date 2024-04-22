import os
import json
import pandas as pd
import langchain
import ollama
from langchain.llms import Ollama
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from data.template import *
import data
with open(r"C:\Users\vk\mcqgeneratorproject\data\sample.json", "r") as f:
    response_json = json.load(f)
template1=template1()
template2=template2()    
llm = Ollama(model="orca-mini", temperature=0.2)
quiz_prompt=PromptTemplate(template=template1,input_variables=["text","number","subject","tone","response_json"])
quiz_chain=LLMChain(llm=llm,prompt=quiz_prompt,output_key="quiz",verbose=True)
quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=template2)
review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True,)
