import os
import yaml
import editor
	
class DataManager:
	def __init__(self):
		self.rootLevels = ['796', '798']
		self.__data = self.__load()
		self.__newData = []
		
	def __load(self):
		file = editor.get_path()
		dir = os.path.dirname(file)
		if not os.path.exists("%s/objetivoData.yml" % dir):
			print("setting up new file")
			self.__data = {}
			for level in self.rootLevels:
				self.__data[level] = []
			self.save()
			
		with open("objetivoData.yml") as file:
			try:
				return yaml.load(file)
			except yaml.YAMLError as exc:
				print(exc)
				
	def getNewData(self):
		return self.__newData
			
	def save(self):
		with open("objetivoData.yml", 'w') as outfile:
			yaml.dump(self.__data, outfile, default_flow_style=False)
		
	def addFolder(self, folderID):
		data = self.__data
		
		print("new folder")
		if folderID not in data.keys():
			data[folderID] = []
				
		self.__data = data
		
	def addLinkToFolder(self, link, folderID):
		data = self.__data
		
		print("new link")
		if link not in data[folderID]:
			data[folderID].append(link)
			self.__newData.append(link)	
			
		self.__data = data
				
	def checkForChanges(self, link, folderID):
		data = self.__data
		hasChanges = False

		if folderID not in data.keys():
			self.addFolder(folderID)
			hasChanges = True

		if link not in data[folderID]:
			self.addLinkToFolder(link, folderID)
			hasChanges = True
			
		return hasChanges
				
				
