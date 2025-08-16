import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_faqs():
    url = "https://www.mosdac.gov.in/faqs"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    faq_data = []
    faqs = soup.find_all("div", class_="panel")  # Based on site's FAQ format

    for item in faqs:
        question = item.find("h4")
        answer = item.find("div", class_="panel-body")
        if question and answer:
            faq_data.append({
                "question": question.text.strip(),
                "answer": answer.text.strip()
            })

    os.makedirs("chatbot/knowledge", exist_ok=True)
    with open("chatbot/knowledge/documents.json", "w", encoding="utf-8") as f:
        json.dump(faq_data, f, indent=2)

    print(f"✅ Scraped {len(faq_data)} FAQs.")

# Run directly
if __name__ == "__main__":
    scrape_faqs()
