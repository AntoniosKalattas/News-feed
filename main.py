import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
import sys
from openai import OpenAI
import os


# news links
cnn = "https://edition.cnn.com"
bbc ="https://www.bbc.com" 

# open router api set up
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
# ask chat for paraphrasing.
def askChat(question,content):
  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "<>",     # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": "<>",          # Optional. Site title for rankings on openrouter.ai.
    },
    model="openai/gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": question+" "+content     # prompt
      }
    ]
  )
  return completion.choices[0].message.content

def extract_content(url, clas, com, get_link):  
    response = requests.get(url)
    soup = bsoup(response.content, "html.parser")
    find_it=soup.find(com, {"class": clas})
    if(get_link == True):
        result = find_it.find("a").get("href")
    else:
        result = find_it.text.strip()   
    return result

# will return the class of the passed element type.
def get_class(url, element, sub_element=0):
    response = requests.get(url)
    if(response.status_code !=200):                # unable to fetch URL
        print("Error: " + response.status_code)
        return None
    soup = bsoup(response.content, "html.parser")  # returns html code.
    Class = soup.find(element).get("class")        # get only the specified element class.
    return Class
    


bbc_output = extract_content(bbc, get_class(bbc, "article"), "article", False)

cnn_output = extract_content(cnn, "scope", "div", False).replace("\n", " ")

#print(cnn_output)

title = askChat("what title would you give for this?", bbc_output + " " + cnn_output)
print(title)

