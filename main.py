import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileMerger

"""
Security engineering third edition, available for free
until november broken up into chapters, this downloads
all the individuals chapters and joins them together
https://www.cl.cam.ac.uk/~rja14/book.html
"""

# scrape links
response = requests.get(url='https://www.cl.cam.ac.uk/~rja14/book.html')
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find('ul', recursive=True).find_all('a')
download_urls = [f'https://www.cl.cam.ac.uk/~rja14/{link.get("href")}' for link in links]

# save all the files
file_names = []
for index, pdf_url in enumerate(download_urls):
    pdf_file = requests.get(pdf_url, allow_redirects=True).content
    file_name = f'file_{index}.pdf'
    file_names.append(file_name)
    with open(file_name, 'wb') as file:
        file.write(pdf_file)

# join files to single pdf
merger = PdfFileMerger()

for pdf in file_names:
    merger.append(pdf)

merger.write("se3e.pdf")
merger.close()
