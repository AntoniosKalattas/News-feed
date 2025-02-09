import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
import sys
from openai import OpenAI
from datetime import datetime
import os
import json

# Load API key from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

# news links
cnn = "https://edition.cnn.com"
bbc = "https://www.bbc.com"

# open router api set up
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = config['api_key']
)

# ask chat for paraphrasing.
def askChat(question, content):
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<>",  # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<>",  # Optional. Site title for rankings on openrouter.ai.
        },
        model="google/gemini-2.0-flash-thinking-exp:free",
        messages=[
            {
                "role": "user",
                "content": question + " " + content  # prompt
            }
        ]
    )
    return completion.choices[0].message.content

def extract_content(url, clas, com, get_link):
    response = requests.get(url)
    response.encoding = 'utf-8'  # Ensure the response is decoded using UTF-8
    soup = bsoup(response.content, "html.parser")
    find_it = soup.find(com, {"class": clas})
    if get_link:
        result = find_it.find("a").get("href")
    else:
        result = find_it.text.strip()
    return result

# will return the class of the passed element type.
def get_class(url, element, sub_element=0):
    response = requests.get(url)
    if response.status_code != 200:  # unable to fetch URL
        print("Error: " + response.status_code)
        return None
    soup = bsoup(response.content, "html.parser")  # returns html code.
    Class = soup.find(element).get("class")  # get only the specified element class.
    return Class

# return current Day, Month, DD, YY
def get_formatted_date():
    today = datetime.today()

    # Get the day of the week
    day_of_week = today.strftime("%A")  # e.g., "Tuesday"

    # Get the month
    month = today.strftime("%B")  # e.g., "September"

    # Get the day with ordinal suffix
    day = today.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    day_with_suffix = f"{day}{suffix}"  # e.g., "17th"

    # Get the year
    year = today.year  # e.g., "2020"

    return str(f"{day_of_week}, {month}, {day_with_suffix}, {year}")

# split the single chatGPT output in 4 chatGPT stories.
def getStories(data):
    start_index = data.find("1: ")
    if start_index != -1:
        data = data[start_index:]

    data = data.replace("#", "").replace("*", "")
    return data.split("Story ")

def generateHTML(stories):
    with open("./web/main.html", "w", encoding='utf-8') as file:
        file.write('<!DOCTYPE html> \n<html lang="en"> \n<head>\n<meta charset="UTF-8">\n<title>NewsFeed</title>\n<link rel="stylesheet" href="./style.css"> \n</head>\n')

        file.write("<body>\n<link href='https://fonts.googleapis.com/css?family=PT+Sans+Narrow:400,700|PT+Serif+Caption|PT+Serif:400,700,400italic,700italic|Oswald:400,700' rel='stylesheet' type='text/css'>\n<article>\n")

        file.write("<h1>" + title + "</h1>")

        file.write(f'<div class="time"><time>{get_formatted_date()}</time></div>\n')

        # file.write(f'<h2>{title1}</h2>\n')

        for i in range(len(stories)):
            if stories[i].strip():
                file.write(f'<p>{stories[i]}</p>')

        file.write('</article>\n<script src="https://cdn.jsdelivr.net/npm/darkmode-js@1.5.5/lib/darkmode-js.min.js"></script>\n<script  src="script.js"></script>\n</body>\n<script  src="./script.js"></script>\n</body>\n</html>')

bbc_output = extract_content(bbc, get_class(bbc, "article"), "article", False)

cnn_output = extract_content(cnn, "scope", "div", False).replace("\n", " ")

# print(cnn_output)

title = askChat("based on the given content, could you just give me a single title that will summarise the contains please? Just give me the title", bbc_output + " " + cnn_output)
print(title)

out = askChat("with the given content could you give me 4 stories that will summarise the content I gave you, with 400 words each?. Give me each story with a header Story \n", bbc_output + cnn_output)
stories = getStories(out)

generateHTML(stories)