# Reuters is a dirty data set and requires sanitation. This script completes the necessary clean up and loads it into a DataFrame.
# The following clean up steps are performed:
# -prints the id for each article and whether it is a training/test set
# -creates an object for each article to store appropriate values
# -creates a dictionary with key (tag), value (contents) pairs using the article object
# -XML lists are surrounded by the "D" tag so the SAX parser interprets all tags with lists as the same value. Therefore, if a tag has a list,
# the overall tag for the section is distinguished and the value is placed with an overall tag in the dictionary.
# -cleans up the values of the BODY and TITLE tags since SAX parses the content according to the '\n' character
# -loads CSVs for the BODY and TITLE of each document ID, which will be used as features
# -creates a third CSV for teh most relevant TOPIC corresponding to each doc ID because multiple topics for each doc ID lead to a mismatch in
# labels and features. The most relevant TOPIC is isolated by determining the most frequent topics in the entire corpus. The most frequent of 
# the TOPICS in each document, according to the dictionary of most frequent topics of the corpus, is then used.
# -the csv also indicates whether the document was used as a training/test in the LEWISSPLIT separation.
# The path starts from the current root and accesses the 22 sgml files stored locally in reuters21578
#
# To run the script:
# 	$ python reuters_loader.py

#common packes for extracting and transforming Machine Learning data
from collections import defaultdict
import csv
import json
import numpy as np
import os
import pandas as pd
import xml.sax #for markup language transformation
from xml.sax.handler import ContentHandler
 
# object that holds all values for each individual article
class Article(object):
	#each value is initialized to an empty value because not every article has each tag/content present
	def __init__(self):
		self.body = ""
		self.data = ""
		self.title = ""
		self.topics = []
		self.places = []
		self.people = []
		self.author = ""
		self.dateline = ""
		self.exchanges = []
		self.companies = []
		self.orgs = []
		self.mknote = ""

class MyHandler(ContentHandler):
	def __init__(self):
		self.count = 1
		self.tag = ''
		self.defaultdict = defaultdict(list)
		self.topdict = defaultdict(list)
		self.boddict = defaultdict(list)
		self.titledict = defaultdict(list)
		self.lewissplit = list()
		self.article = Article()
		self.df = pd.DataFrame()
		self.in_d = False
		self.docID = 0
		self.lewis = "train"
		self.freqDict = defaultdict(int)
		#get frequency count of most popular topics
		file = open("all_topics.csv")
		for word in file.read().split():
			self.freqDict[word] += 1

	#booleans that keep track of the tags that SAX does not parse correctly and therefore need to be cleaned
	def _reset(self):
		self.in_places = False
		self.in_topics = False
		self.in_people = False
		self.in_exchanges = False
		self.in_companies = False
		self.in_orgs = False
	
