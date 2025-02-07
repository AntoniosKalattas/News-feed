# **NewsFeed Scraper & Summarizer**

## **Overview**
This project is a Python-based web scraper that extracts news headlines from **BBC** and **CNN**, summarizes them using OpenAI's API, and generates a formatted HTML page displaying the summarized stories.

## **Features**
- Scrapes news content from **CNN** and **BBC**.
- Uses **OpenAI API (via OpenRouter)** for **text summarization**.
- Generates an **HTML file** with formatted news stories.
- Retrieves **dynamic class names** for articles using BeautifulSoup.
- Supports **parsing and splitting** AI-generated summaries into multiple stories.

## **Installation**
### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/news-feed.git
cd news-feed
```

### **2. Install Dependencies**
Ensure you have **Python 3.11+** installed. Then, install required packages:
```sh
pip install -r requirements.txt
```

If you encounter a `ModuleNotFoundError`, install missing dependencies manually:
```sh
pip install beautifulsoup4 requests openai
```

### **3. Set Up OpenAI API**
The script uses **OpenRouter API** for paraphrasing and summarization. Set up your API key:

1. Create an account on [OpenRouter](https://openrouter.ai).
2. Replace `api_key="sk-or-..."` in `main.py` with your own API key.

## **Usage**
### **Run the Script**
```sh
python3 main.py
```
This will:
- Scrape **CNN** and **BBC** for headlines.
- Use **OpenAI** to generate a **summary title**.
- Extract **4 summarized stories** from the news content.
- Generate an **HTML file** (`web/main.html`) containing the summarized news.

### **Expected Output**
- **Terminal Output**: A summary title.
- **Generated HTML File**: `web/main.html` displaying the summarized news.

## **Project Structure**
```
📂 News-feed
 ├── main.py              # Main script
 ├── requirements.txt      # Dependencies list
 ├── web/
 │   ├── main.html        # Generated HTML file
 │   ├── style.css        # CSS for styling (optional)
 │   ├── script.js        # JS for additional functionality (optional)
 ├── README.md            # Documentation
```

## **Functions Overview**
| Function | Description |
|----------|------------|
| `askChat(question, content)` | Sends a request to OpenAI for summarization. |
| `extract_content(url, class_name, tag, get_link)` | Extracts text or links from the given webpage. |
| `get_class(url, element, sub_element=0)` | Retrieves the class name of an HTML element. |
| `get_formatted_date()` | Returns the formatted date in `Day, Month, DD, YYYY` format. |
| `getStories(data)` | Splits AI-generated output into multiple stories. |
| `generateHTML(stories)` | Generates an HTML file with summarized news content. |

## **Dependencies**
- `beautifulsoup4`
- `requests`
- `openai`
- `datetime`
- `os`
- `sys`

## **Notes**
- Ensure your API key is **valid** and **active**.
- If the scraping fails, check the **class names** of elements on **CNN/BBC** (they may change over time).
- The script **overwrites** `web/main.html` each time it's executed.

## **Future Improvements**
- Add support for **more news sources**.
- Implement **error handling** for missing elements.
- Improve **formatting** and UI of the generated HTML.

---



# UI
https://codepen.io/saiphanindra1010/pen/wvKMrqL
