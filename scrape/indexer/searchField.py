from urllib.request import urlopen
from urllib.parse import urlencode
import simplejson

# print (response['response']['numFound'], "documents found.")

def getSearchResults(searchField):
    solr_url = 'http://localhost:8983/solr/gic/select?defType=dismax&qf=topic^20.0+text^0.3&'
    solr_tuples = [
        # text in search box         http://localhost:8983/solr/gic/select?defType=dismax&q=children&qf=topic^20.0+text^0.3
        ('q', searchField),
        # format response as JSON    http://localhost:8983/solr/gic/select?df=text&qf=topic^10.0+text^1&
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