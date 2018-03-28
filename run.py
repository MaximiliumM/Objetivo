from dataManager import DataManager
from objetivoScrapper import Scrapper

scrapper = Scrapper()
manager = DataManager()

forbiddenLinks = ['843', '835', '818']

def removeForbiddenLink(links):
	for link in forbiddenLinks:
		if link in links:
			links.remove(link)
	return links
	
def checkForUpdatesForContentID(contentID):
	links = scrapper.getLinksFromContentID(contentID)
	links = removeForbiddenLink(links)
	
	for link in links:
		print("current level: %s, current link: %s" % (contentID, link))
		manager.checkForChanges(link, contentID)

def checkForUpdates(levels):
	
	for level in levels:
		links = scrapper.getLinksFromContentID(level)
		links = removeForbiddenLink(links)
		
		for link in links:
			print("current level: %s, current link: %s" % (level, link))
			if manager.checkForChanges(link, level) and 'pdf' in link:
				print('dowloading new link')
				#download(link)
				
			if 'pdf' not in link:
				checkForUpdates(links)
				



#checkForUpdatesForContentID('796')	
checkForUpdates(manager.rootLevels)
#manager.save()
