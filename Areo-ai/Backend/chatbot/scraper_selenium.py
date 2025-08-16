from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import os

def scrape_faqs_selenium():
    # Headless browser setup
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    print("🔍 Navigating to MOSDAC FAQ page...")
    driver.get("https://www.mosdac.gov.in/faqs")

    try:
        # ⏳ Wait up to 10s for the accordion content to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "accordion-toggle"))
        )
        print("✅ Page content loaded.")
    except Exception as e:
        print("❌ Failed to load content:", e)
        driver.quit()
        return

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # ✅ Extract FAQs
    faq_data = []
    questions = soup.select("a.accordion-toggle")
    answers = soup.select("div.panel-body")

    for q, a in zip(questions, answers):
        question = q.get_text(strip=True)
        answer = a.get_text(strip=True)
        faq_data.append({
            "question": question,
            "answer": answer
        })

    os.makedirs("chatbot/knowledge", exist_ok=True)
    with open("chatbot/knowledge/documents.json", "w", encoding="utf-8") as f:
        json.dump(faq_data, f, indent=2)

    print(f"✅ Scraped {len(faq_data)} FAQs using Selenium.")
    print("📄 Output saved to: chatbot/knowledge/documents.json")

if __name__ == "__main__":
    scrape_faqs_selenium()
