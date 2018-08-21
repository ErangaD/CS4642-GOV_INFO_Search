from urllib.request import urlopen
import simplejson
connection = urlopen('http://localhost:8983/solr/gic/select?q=text:*&wt=json')
response = simplejson.load(connection)
print (response['response']['numFound'], "documents found.")

# Print the name of each document.

for document in response['response']['docs']:
  print ("  Name =", document['text'])