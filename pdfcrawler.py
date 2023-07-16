import requests
import pdfplumber
import os

def pdf_to_text_url(url):
    # Download the PDF file from the URL
    response = requests.get(url)
    with open("temp.pdf", "wb") as file:
        file.write(response.content)

    # Extract text from the PDF
    with pdfplumber.open("temp.pdf") as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Clean up the temporary PDF file
    file.close()
    os.remove("temp.pdf")

    return text