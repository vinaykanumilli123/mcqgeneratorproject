import data
with open("C:/Users/vk/mcqgeneratorproject/data/sample.json","r") as f:
    file=f.read()
print(file)
from data.template import *
print(template1())