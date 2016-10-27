#Reference-https://marcobonzanini.com/2015/02/02/how-to-query-elasticsearch-with-python/
from elasticsearch import Elasticsearch
import json
def search(term):
	elasticcollect = Elasticsearch()
	locations = []
	query = json.dumps({
		"query": {
			"match": {
				"text": term
			}
		}
	})
	queryresult = elasticcollect.search(index="data", doc_type="tweets", body=query)
	for doc in queryresult['hits']['hits']:
		coordinates = doc['_source']['coordinates']
		location = doc['_source']['user']['location']
		if coordinates is not None:
			print(" %s" % (coordinates))
			locations.append()
		elif location is not None:
			print(" %s" % (location))
			locations.append(location)
	return locations
if __name__ == "__main__":
	search("#AskNiall")