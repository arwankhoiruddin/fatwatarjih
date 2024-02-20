from bs4 import BeautifulSoup
import requests

tarjih_posts_sitemap = 'https://fatwatarjih.or.id/post-sitemap.xml'

posts_sitemap = requests.get(tarjih_posts_sitemap)
soup = BeautifulSoup(posts_sitemap.text, 'xml')
links = soup.find_all('loc')

urls = [link.text for link in links if '<image:loc>' not in str(link)]

fatwa = []

for url in urls:
    print(f'Getting fatwa from {url}')
    web = requests.get(url)
    post_soup = BeautifulSoup(web.text, 'html.parser')

    paragraphs = post_soup.find_all('p')
    pertanyaan = ''
    jawaban = ''
    collect_paragraphs = False

    for paragraph in paragraphs:
        if "Pertanyaan:" in paragraph.text:
            collect_paragraphs = True
        elif "Jawaban:" in paragraph.text:
            collect_paragraphs = False
        elif 'email' in paragraph.text:
            break
        elif collect_paragraphs:
            pertanyaan += paragraph.text
        elif not collect_paragraphs:
            jawaban += paragraph.text
        if pertanyaan and jawaban:
            fatwa.append(f'Pertanyaan: {pertanyaan} \n Jawaban: {jawaban}')

# Specify the file path
file_path = "fatwa.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Iterate over the array of strings
    for string in fatwa:
        # Write each string to the file
        file.write(string + "\n")
