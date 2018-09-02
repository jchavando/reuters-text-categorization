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
