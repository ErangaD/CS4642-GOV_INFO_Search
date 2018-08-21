from urllib.request import urlopen
from urllib.parse import urlencode
import simplejson

# print (response['response']['numFound'], "documents found.")

def getSearchResults(searchField):
    solr_url = 'http://localhost:8983/solr/gic/select?df=text&'
    solr_tuples = [
        # text in search box
        ('q', searchField),
        # format response as JSON
        ('wt', 'json')
    ]
    encoded_solr_tuples = urlencode(solr_tuples)
    complete_url = solr_url + encoded_solr_tuples
    print('--------------------------------------------------------------------------------------',complete_url)
    connection = urlopen(complete_url)
    response = simplejson.load(connection)
    return response['response']['docs']


# Print the name of each document.
# for document in response['response']['docs']:
#   print ("  Name =", document['text'])