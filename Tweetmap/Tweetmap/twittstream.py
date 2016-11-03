#Reference - http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
import tweepy
import json
from flask import Flask
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from elasticsearch import Elasticsearch
application = Flask(__name__)
@application.route("/")
class twittListener(StreamListener):
	elasticcollect = Elasticsearch()
	def on_data(self, raw_data):
		json_data = json.loads(raw_data)
		if json_data.get("text", None) is not None:
			coordinates = json_data["coordinates"]
			location = json_data["user"]["location"]
			text = json_data['text']
			if location is not None or coordinates is not None:
				self.elasticcollect.index(index="data", doc_type="tweets", body=raw_data)
				print (text)
		return True
	def on_error(self, status_code):
		print(status_code)
	def on_disconnect(self, notice):
		print (self.notice)
def main():
	consumerkey = ""
	consumersecret = ""
	accesstoken = ""
	accesstokensecret = ""
	authhandler = OAuthHandler(consumerkey, consumersecret)
	authhandler.set_access_token(accesstoken, accesstokensecret)
	tweets = tweepy.Stream(authhandler, twittListener())
	tweets.filter(track=["#AskNiall", "#NationalPumpkinDay", "Joe Walsh", "Trump", "Hillary"],async=True)
if __name__ == "__main__":
	main()
