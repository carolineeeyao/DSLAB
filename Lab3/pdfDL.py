import urllib2
from bs4 import BeautifulSoup

url = "http://proceedings.mlr.press/v70/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

aTags = soup.find_all('a',text="Download PDF")
links = [link['href'] for link in aTags]

for i,link in enumerate(links):
    fileName = link.split('/')[-1]
    print 'saving file {}'.format(fileName)
    response = urllib2.urlopen(link)
    data = response.read()
    pdfFile = open('pdfs/{}'.format(fileName),'wb')
    pdfFile.write(data)
    pdfFile.close()
