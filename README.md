# Reuters-21578 Text Categorization
The Reuters-21578 data is one of the most widely used test collections for text categorization, which is contained in the reuters21578 folder. This collection is distributed in 22 SGML files, each containing 1000 documents, with the last containing 578 documents. The files were taken from teh UCI Machine Learning Repository located at https://archive.ics.uci.edu/ml/datasets/Reuters-21578+Text+Categorization+Collection.

The files are organized with the following tags. Each individual article in the corpus starts with a "REUTERS" tag that contains information about the "TOPICS" and the document "ID" present in that file and ends with the closing "/REUTERS" tag. Each article also has a "LEWISSPLIT" tag with the possible values of "TRAINING" or "TEST", indicating whether it was used in the training or test set reported in LEWIS91d, LEWIS92b, LEWIS92e, and LEWIS94b experiments, which are detailed in teh TOIS paper located in the Resources folder. Each article additionally has a "DATE", list of "TOPICS" and "PLACES", "ORGS", "EXCHANGES", "COMPANIES", "TEXT", "TITLE", and "DATELINE". Because of the large quntity of information, the files are stored locally.

## References
Various approaches have been attempted to best categorize large amounts of text. SInce the goal of this project is to use machine generated decision rules to categorize the text, "Automated Learning of Decision Rules for Text Categorization" explains methods to approach ist effectively. Taken from ACM Transactions on Information Systems (TOIS) this paper details the results of optimized rule-based induction methods that discover general classification patterns. The most effective method begins with prepocessing the data into a dictionary to represent individual documents. This approach then employs representation to isolate each document to a training sample and associates it with a label that identifies its category. Induction is used to find patterns that distinguish cateogries until minimal classifcation error is achieved.

This paper is located in the Resources folder.

## Loading Data
The goal of this section was to load the data into a manageable DataFrame. The external script is reuters_loader.py.

This script loops through the 22 files and uses the SAX xml parser to isolate xml tags and corresponding values. Certain parsing that the SAX parser cannot handle is specifically manipulated, as detailed below. An object is created for each article with values for each tag. The objects are then placed in a dictionary which is transformed into a DataFrame of all the files. The individual parsing is as follows:
-since the parser interprets a newline character ('\n') as the indication of a new element, the text of the "BODY" and "TITLE" have to be individually grouped for each article
-each element of a list is intepreted as a new tag, so the tags with lists, such as "PLACES", append elements to their respective overall list
