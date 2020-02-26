# searchProduct.py
'''
   If your bot need a way to search products or any items, one can make use of
   ElasticSearch Engine, for local testing, ElasticSearch needs to be installed

   One example of such a bot is a bot that searches books or music on your server or cloud storage, or any related
   where you need to have your own custom search engine for your bot e.g your bot might be handling user queries like: search book Alice In Wonderland
'''
from os import path
from csv import reader
from random import randint
#from elasticsearch import ElasticsearchException

# can be database, doc, excel, pandas DF etc
_searchable_items = path.join(RESOURCES, 'your-items.csv')     # this is an example of having a csv file containing your items, e.g books / music tracks

class Search:
   def __init__(self, es, product=None):
      self.es           = es        # Connect to the elasticsearch server, pass ES object | create it
      self.product      = product   # can be product/item/music-track/books/any item you can search in your collection / inventory

   def searchResult(self):
      ret_data = ""
      # TODO: search item in your item index and return result
      search_result_ = "<result>"
      return search_result_

   def readProductList(self):
      # read items in the csv file and get ready to populate in ES index
      line = 0
      with open(products) as f:
         CSVreader = reader(f)         # can use DictReader()
         for row in CSVreader:
            if line == 0:  # in case they are just headers
               pass

            else:
               # flag to create new index
               self.createDB(row)

            line += 1

      print("[INFO] Processed %d lines" %line)

   def createIndex(self):
      # delete old and create new index
      if self.es.indices.exists(index=INDEX_DB):
         print("[WARN] Index exists. Deleting..")
         es.indices.delete(index=INDEX_DB)

      self.es.indices.create(index=INDEX_DB)

      print("[INFO] New index created!")

   def createDB(self, row_data, create_new=False):
      # get data to fill in ES index | get data from online of products list
      print("[INFO] Creating index..")
      if create_new:
         self.createIndex()

      # row_data contains your items info in rows from the csv file

      body_  = {} # a dict containing your items info to populate the ES index
      '''
      dummy example
      body_ = {
         'artist': 'NF',
         'track':  'when i grow up',
         'size': '3.4mb',
         'url': 'https://your-music-library-site.com/nf/new/music.mp3',
         'price': '$5.00'
      }
      '''

      resp = es.index(index=INDEX_DB, doc_type=DOCTYPE, id="random-id", body=body_)
      print("[INFO] ES responce: ", resp)

   def searchDB(self):
      # search for the item in the elasticsearch index
      body = {
        "query": {
            "multi_match": {
                "query": self.product
            }
        }
      }

      res       = self.es.search(index=INDEX_DB, body=body)
      response  = res.get('hits').get('hits')
      max_score = res.get('hits').get('max_score')  # returns None if not found

      if len(response) > 0 and max_score != None:
         data = {}
         # result is found, format the result and return to user
         return True, data

      else:
         # no results found
         return False, f"No results found: {self.product.upper()}"

   def checkExist(self):
      if path.isfile(products):
         return True

   def quotation(self):
      # return a quatation to user if needed
      quotation_ = "<do-quatation>"
      return quotation_