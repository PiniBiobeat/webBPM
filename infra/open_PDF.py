import requests
import pdfplumber
import os
import time

pdf_path = r"C:\Users\tester\PycharmProjects\pytest-lupa\tests\TestAdmin\invoice.pdf"
target_amount = "163.00"
MAX_RETRIES = 10 # Limit the number of retries


def download_pdf(order_id, invoice, get_total_pay_sql, attempt=1):
    """Download the PDF using the extracted order_id and invoice."""
    id = str(order_id)
    inv = str(invoice)
    pdf_url = f"https://admin.lupa.co.il/admin_online/Invoice.aspx?orderId={id}&masterId=3657774&invoice={inv}&trans=1"

    print(f"📥 Attempt {attempt}: Downloading PDF from: {pdf_url}")

    response = requests.get(pdf_url)

    if response.status_code == 200:
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"✅ PDF downloaded successfully: {pdf_path}")

        return extract_and_search_text(get_total_pay_sql, attempt,order_id, invoice,)
    else:
        print(f"❌ Failed to download PDF. Status code: {response.status_code}")

        if attempt < MAX_RETRIES:
            print("🔄 Retrying PDF download...")
            time.sleep(2)  # Wait before retrying
            return download_pdf(order_id, invoice, get_total_pay_sql, attempt + 1)

        print("❌ Maximum retries reached. Exiting.")
        return False


def extract_and_search_text(get_total_pay_sql, attempt=1,order_id=None, invoice=None):
    """Extract text from the PDF and check for the target amount."""

    if not os.path.exists(pdf_path):
        print("❌ PDF file not found. Retrying download...")
        if attempt < MAX_RETRIES:
            return download_pdf(order_id, invoice, get_total_pay_sql, attempt + 1)
        return False

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()

                if text:
                    print(f"🔍 Scanning Page {page_num}...")

                    if str(get_total_pay_sql) in text:
                        print(f"✅ Found '{get_total_pay_sql}' on Page {page_num}!")
                        return str(get_total_pay_sql)

                else:
                    print(f"⚠️ No text found on Page {page_num}.")

        print(f"❌ '{get_total_pay_sql}' NOT found in the PDF.")
        return False

    except Exception as e:
        print(f"❌ Error while extracting text: {e}")

        if attempt < MAX_RETRIES:
            print("🔄 Retrying PDF download...")
            time.sleep(30)  # Wait before retrying
            return download_pdf(order_id, invoice, get_total_pay_sql, attempt + 1)

        print("❌ Maximum retries reached. Exiting.")
        return False
