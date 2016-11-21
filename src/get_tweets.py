from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#use tweepy library to get tweets from twitter

#use access token and keys which were obtained after registering with twitter API
access_token = "292971987-CvyN0MRLrWc2r9TObCV4gioWEy6dNbCu9t66cec6"
access_token_secret = "NxYQ3MvNCwEtHtqrypyt8BxKZP66wiS198jNP0u7nDcdk"
consumer_key = "AHqe3VkwGjXzVYykuy1lO2ZT6"
consumer_secret = "9oaMwpcRG35NbcRJM1p1hCxSQKwRzKomUdmLiiUMGNDl5iRMVc"



class listener(StreamListener):

    def __init__(self):
	super(listener,self).__init__()

#initialize number of tweets to be obtained
	self.counter = 0
	self.limit = 50000

    def on_data(self, data):
#open file a and write the json to the file
        print(data)
        try:
            with open('cars.json','a') as f:
                f.write(data)
        except BaseException as e:
            print ('danger')
 #check if count is reached      
        if self.counter < self.limit:
            self.counter = self.counter+1
            return True
        else:
        	return False 


    def on_error(self, status):
        print(status)

#authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
#set the keyword and start the listener to download tweets
twitterStream.filter(track=['cars'])