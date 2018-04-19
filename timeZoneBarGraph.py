# for the graph
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np

import tweepy
auth = tweepy.OAuthHandler("iHTvDAptJAx3PwfYfw00Qa6sX", "6Gp8kYPR3kULcPPdW3k1gYopQEi4NBdSfFPP8ifHCE0gwkQWCX")
auth.set_access_token("938932912870658048-ICcR2mOBhIvNtIQmMSVdtuQbUsCxIXL", "QU7ArtcKW1aEQYcf0HlMUpS7m07UtQmUNl42OvAJyZ5SH")
api = tweepy.API(auth)



wordSearch = input("What's input do you want to search for? ")
print("This is your input: " + wordSearch )

#items say number of tweets looked at
def FlaskBarGraph():
    mylist = []
    for tweet in tweepy.Cursor(api.search,q=wordSearch).items(10):
        # just print(tweet.text) for the results (tweet.author or date)
        # just print(tweet) for all the results

        x=tweet.author
        y=x.time_zone
        mylist.append(str(y))
        #print(mylist)
        #print(tweet.text)
        # x.geo_enabled works

        # this bit of code is to get a frequency of mylist
        from collections import Counter
        counts = Counter(mylist)
        #counts= dictionary
        print(counts)
        #this is what is printed out => Counter({'None': 7, 'Central Time (US & Canada)': 1, 'America/Caracas': 1, 'Arizona': 1})

        #count.get is how you get values from the key
        default_value=0 #the default_value gives you a 0 for the time zone,
                        # as sometimes a timezone isn't there and then its value will be none and this mess up the code
        pt=counts.get("Pacific Time (US & Canada)",default_value)
        print(pt)
        et=counts.get("Eastern Time (US & Canada)",default_value)
        print(et)
        mt=counts.get("Mountain Time (US & Canada)",default_value)
        print(mt)
        az=counts.get("Alaska",default_value)
        print(az)
        hz=counts.get("Hawaii",default_value)
        print(hz)
        ct = counts.get("Central Time (US & Canada)", default_value)
        print(ct)
        nz =(10-(pt+et+mt+az+hz+ct))  #to show the other time zone tweets and no timezone tweets

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii','Other')
    y_pos = np.arange(len(objects))
    # to give each bar its value
    performance = [et,pt, mt, az, ct, hz,nz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Time Zones')

    #plt.show()  to display on pycharm
    #savfig= saves graph as png
    plt.savefig('ah.png')

FlaskBarGraph()
