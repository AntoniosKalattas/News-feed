import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
import sys
import openai
import os

def extract_content(url, clas, com, get_link):  
    response = requests.get(url)
    soup = bsoup(response.content, "html.parser")
    find_it=soup.find(com, {"class": clas})
    if(get_link == True):
        result = find_it.find("a").get("href")
    else:
        result = find_it.text.strip()
    return result

def get_class(url, element, sub_element=0):
    response = requests.get(url)
    soup = bsoup(response.content, "html.parser")
    class1 = soup.find(element).get("class")
    return class1
    



# For BBC
url = "https://www.bbc.com/news"
clas = "gel-wrap gs-u-pt+"
url_of_latest ="https://www.bbc.com" + extract_content(url, clas, "div", True)
print("link is: "+url_of_latest)

clas = get_class(url_of_latest, "article")
print(extract_content(url_of_latest, clas, "article", False))   
#End of bbc process

#ChatGPT

openai.api_key = "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"
prompt = "hello there"
model = "text-davinci-003"
temperature =0.2
max_tokens = 10
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

print(response.choices[0].text.strip())