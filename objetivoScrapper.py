from bs4 import BeautifulSoup 
import requests

class Scrapper(object):	
	def __init__(self):
		self.__session = self.__login()
		
	def __login(self):
		url = "http://www.objetivo.br/conteudo.asp"
		payload = {'matricula': '12540009107', 'senha': 'fe9107'}
		s = requests.Session()
		s.post(url, data=payload)
		return s
	
	def getLinksFromContentID(self, contentID):
		html = self.getHTMLFromContentID(contentID)
		return self.getAllContentIDsFromHTML(html)
	
	def getHTMLFromContentID(self, contentID):
		content_url = "http://www.objetivo.br/conteudo.asp?ref=cont&id=%s" % contentID 
		return self.__session.get(content_url)

	def getAllContentIDsFromHTML(self, html):
		soup = BeautifulSoup(html.text, "html5lib")
		contentIDs = []
	
		for link in soup.find_all('a'):
			href = link.get('href')
			
			if type(href) is str:
				if 'pdf' in html.text:
					if 'pdf' in href:
						contentIDs.append(href)
				else:
					if "conteudo" in href:
						contentIDs.append(href.split("id=")[1])
						
		return contentIDs
