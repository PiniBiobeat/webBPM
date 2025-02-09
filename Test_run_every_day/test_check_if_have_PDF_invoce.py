import requests
import pdfplumber
import os
import time
from infra.generic_helpers import find_order_with_invoice
import pytest

pdf_path = r".\invoice.pdf"
text_in_pdf = "סמ תינובשח"
MAX_RETRIES = 5  # Limit the number of retries
slack_webhook_url = "https://hooks.slack.com/services/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"

class TestCheckInvoice:
    def __init__(self):
        order_data = find_order_with_invoice()
        self.order_id = order_data[0] if order_data else None
        self.invoice = order_data[1] if order_data else None
        self.master_id = order_data[2] if order_data else None
        self.textPDF = text_in_pdf

    def send_to_slack(self, message):
        payload = {"text": message}
        response = requests.post(slack_webhook_url, json=payload)
        if response.status_code != 200:
            print(f"❌ Failed to send message to Slack. Status code: {response.status_code}")

    def download_pdf(self, attempt=1):
        pdf_url = f"https://admin.lupa.co.il/admin_online/Invoice.aspx?orderId={self.order_id}&masterId={self.master_id}&invoice={self.invoice}&trans=0"

        print(f"📥 Attempt {attempt}: Downloading PDF from: {pdf_url}")

        response = requests.get(pdf_url)

        if response.status_code == 200:
            with open(pdf_path, "wb") as f:
                f.write(response.content)
            print(f"✅ PDF downloaded successfully: {pdf_path}")

            return self.extract_and_search_text(attempt)
        else:
            print(f"❌ Failed to download PDF. Status code: {response.status_code}")

            if attempt < MAX_RETRIES:
                print("🔄 Retrying PDF download...")
                time.sleep(2)  # Wait before retrying
                return self.download_pdf(attempt + 1)

            print("❌ Maximum retries reached. Exiting.")
            return False

    def extract_and_search_text(self, attempt=1):
        """Extract text from the PDF and check for the target amount."""

        if not os.path.exists(pdf_path):
            print("❌ PDF file not found. Retrying download...")
            if attempt < MAX_RETRIES:
                return self.download_pdf()
            return False

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()

                    if text:
                        print(f"🔍 Scanning Page {page_num}...")

                        if str(self.textPDF) in text:
                            print(f"✅ Found '{self.textPDF}' on Page {page_num}!")
                            self.send_to_slack(f"✅ Found '{self.textPDF}' on Page {page_num} in the PDF.")
                            return True

                    else:
                        print(f"⚠️ No text found on Page {page_num}.")

            print(f"❌ '{self.textPDF}' NOT found in the PDF.")
            self.send_to_slack(f"❌ '{self.textPDF}' חשבוניות לא מוצגות בהזמנה יש להפעיל חתימת חשבוניות ")
            return False

        except Exception as e:
            print(f"❌ Error while extracting text: {e}")


            if attempt < MAX_RETRIES:
                print("🔄 Retrying PDF download...")
                time.sleep(30)  # Wait before retrying
                return self.download_pdf(attempt+1)

            print("❌ Maximum retries reached. Exiting.")
            self.send_to_slack(f"❌ חשבוניות לא מוצגות בהזמנה ,יש להפעיל חתימת חשבוניות, מספר ההזמנה הוא :{self.order_id}")
            return False

@pytest.fixture
def test_check_invoice():
    return TestCheckInvoice()

def test_download_pdf(test_check_invoice):
    assert test_check_invoice.download_pdf(attempt=1), f"'{test_check_invoice.textPDF}' found in the PDF."