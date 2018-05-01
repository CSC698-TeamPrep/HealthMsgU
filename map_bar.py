# line means plt= matplotlib.pyplor
import matplotlib.animation as animation

import matplotlib.pyplot as plt

#This is for the map plotv
import mpl_toolkits
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex, Normalize
from matplotlib.patches import Polygon
from matplotlib.colorbar import ColorbarBase
from matplotlib.lines import Line2D
from matplotlib.font_manager import FontProperties
import numpy as np
import random
from collections import Counter

#For wordcloud
from os import path
from wordcloud import WordCloud, STOPWORDS

def data_vis(tweets, ptweets, ntweets, term):
    strOfAllTweet = " "
    strOfPosTweet = " "
    strOfNegTweet = " "
    strOfNeuTweet = " "

    # This removes the // from http
    remove_back = lambda s: ' '.join(i for i in s.split() if '//' not in i)

    #This will print all the tweet text
    #print('###########All')
    alltweets = [tweet for tweet in tweets if
                 tweet['sentiment'] == 'negative' or tweet['sentiment'] == 'positive' or tweet[
                     'sentiment'] == 'neutral']
    for tweet in alltweets:
        strOfAllTweet += " " + tweet['text']
        #print(strOfAllTweet)

    # This gets rid of the @ username and &amp
    newStrAll = " ".join(list(filter(lambda x: x[0] != '@', strOfAllTweet.split())))
    newStrAll2 = " ".join(list(filter(lambda x: x[0] != '&', newStrAll.split())))
    strOfAllTweet = remove_back(newStrAll2)

    #print("OOOOOOOO")
    #print(strOfAllTweet)
    #print('OOOOOOOO')

    #print('###########Pos')
    # This will print positive tweet text
    #print(ptweets)
    for tweet in ptweets:
        strOfPosTweet += " " + tweet['text']
        #print(strOfPosTweet)

    #This gets rid of the @ username and &amp
    newStrPos = " ".join(list(filter(lambda x:x[0]!='@', strOfPosTweet.split())))
    newStr2 = " ".join(list(filter(lambda x: x[0] != '&', newStrPos.split())))
    strOfPosTweet = remove_back(newStr2)

    #print("OOOOOOOO")
    #print(strOfPosTweet)
    #print('OOOOOOOO')

    #print('###########Neg')
    for tweet in ntweets:
        strOfNegTweet += " " + tweet['text']
        #print(strOfNegTweet)
        #print(strOfNegTweet)

    newStrNeg = " ".join(list(filter(lambda x: x[0] != '@', strOfNegTweet.split())))
    newStrNeg2 = " ".join(list(filter(lambda x: x[0] != '&', newStrNeg.split())))
    strOfNegTweet = remove_back(newStrNeg2)
    #print("OOOOOOOO")
    #print(strOfNegTweet)
    #print('OOOOOOOO')

    #print('###########Neu')
    neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    for tweet in neutweets:
        strOfNeuTweet += " " + tweet['text']
        #print(strOfNeuTweet)

    newStrNeu = " ".join(list(filter(lambda x: x[0] != '@', strOfNeuTweet.split())))
    newStrNeu2 = " ".join(list(filter(lambda x: x[0] != '&', newStrNeu.split())))
    strOfNeuTweet = remove_back(newStrNeu2)
    #print("OOOOOOOO")
    #print(strOfNeuTweet)
    #print('OOOOOOOO')
    #print('********')
    ##########################################################
    #This makes the word cloud
    stopwords = set(STOPWORDS)
    stopwords.add("http")
    stopwords.add("https")
    stopwords.add("_")
    stopwords.add("RT")
    stopwords.add("via")
    stopwords.add("LOL")
    stopwords.add("lol")
    stopwords.add("co")
    stopwords.add("mean")
    stopwords.add("either")
    stopwords.add("amp")

    #This is a cloud for all tweets

    if len(alltweets) > 1:
        wordcloud = WordCloud(max_words=500, background_color="white", stopwords=stopwords, collocations=False,
                          relative_scaling=0.5).generate(strOfAllTweet)
        plt.title('All Tweets')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('static/WordCloudAll.png')
        plt.close()

    #This is a cloud for positive tweet
    if len(ptweets) == 0 or len(ptweets) == 1:
        plt.title('Positive Tweets: No Positive Tweets Found')
        plt.axis("off")
        plt.savefig('static/WordCloudPos.png')
        plt.close()
    elif len(ptweets) > 1:
        wordcloud = WordCloud(max_words=500, background_color="white", stopwords=stopwords, collocations=False,
                          relative_scaling=0.5).generate(strOfPosTweet)
        plt.title('Positive Tweets')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('static/WordCloudPos.png')
        plt.close()
    # This is a cloud for negative tweet
    if len(ntweets) == 0 or len(ntweets) == 1:
        plt.title('Negative Tweets: No Negative Tweets Found')
        plt.axis("off")
        plt.savefig('static/WordCloudNeg.png')
        plt.close()
    if len(ntweets) > 1:
        wordcloud = WordCloud(max_words=500, background_color="white", stopwords=stopwords, collocations=False,
                          relative_scaling=0.5).generate(strOfNegTweet)
        plt.title('Negative Tweets')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('static/WordCloudNeg.png')
        plt.close()
    # This is a cloud for Neutral tweet
    if len(neutweets) == 0 or len(neutweets) == 1:
        plt.title('Neutral Tweets: No Neutral Tweets Found')
        plt.axis("off")
        plt.savefig('static/WordCloudNeu.png')
        plt.close()
    elif len(neutweets) > 1:
        wordcloud = WordCloud(max_words=500, background_color="white", stopwords=stopwords, collocations=False,
                          relative_scaling=0.5).generate(strOfNeuTweet)
        plt.title('Neutral Tweets')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('static/WordCloudNeu.png')
        plt.close()
        ########################################################

        # This makes the time zone Bar graph

    print("###")
    timeZoneStr = []
    for tweet in alltweets:
        timeZoneStr.append(tweet['timezone'])
    #print(timeZoneStr)

    counts = Counter(timeZoneStr)
    # counts= dictionary
    #print(counts)
    # this is what is printed out => Counter({'None': 7, 'Central Time (US & Canada)': 1, 'America/Caracas': 1, 'Arizona': 1})

    # count.get is how you get values from the key
    default_value = 0  # the default_value gives you a 0 for the time zone,
    # as sometimes a timezone isn't there and then its value will be none and this mess up the code
    pt = counts.get("Pacific Time (US & Canada)", default_value)
    #print(pt)
    et = counts.get("Eastern Time (US & Canada)", default_value)
    #print(et)
    mt = counts.get("Mountain Time (US & Canada)", default_value)
    #print(mt)
    az = counts.get("Alaska", default_value)
    #print(az)
    hz = counts.get("Hawaii", default_value)
    #print(hz)
    ct = counts.get("Central Time (US & Canada)", default_value)
    #print(ct)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    # to give each bar its value
    performance = [et, pt, mt, az, ct, hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Tweets in US Time Zones')

    # plt.show()  to display on pycharm
    # savfig= saves graph as png
    plt.savefig('static/barchart.png')
    plt.close()

    # timezone for  positive tweets
    p_timeZoneStr = []
    for tweet in ptweets:
        p_timeZoneStr.append(tweet['timezone'])
    #print(p_timeZoneStr)

    p_counts = Counter(p_timeZoneStr)
    #print(p_counts)
    p_pt = p_counts.get("Pacific Time (US & Canada)", default_value)
    #print(p_pt)
    p_et = p_counts.get("Eastern Time (US & Canada)", default_value)
    #print(p_et)
    p_mt = p_counts.get("Mountain Time (US & Canada)", default_value)
    #print(p_mt)
    p_az = p_counts.get("Alaska", default_value)
    #print(p_az)
    p_hz = p_counts.get("Hawaii", default_value)
    #print(p_hz)
    p_ct = p_counts.get("Central Time (US & Canada)", default_value)
    #print(p_ct)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    # to give each bar its value
    performance = [p_et, p_pt, p_mt, p_az, p_ct, p_hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Positive Tweets in US Time Zones')

    # plt.show()  to display on pycharm
    # savfig= saves graph as png
    barG = plt.savefig('static/positive_barchart.png')
    plt.close()

    # timezone for  negative tweets
    n_timeZoneStr = []
    for tweet in ntweets:
        n_timeZoneStr.append(tweet['timezone'])
    #print(n_timeZoneStr)

    n_counts = Counter(n_timeZoneStr)
    #print(n_counts)
    n_pt = n_counts.get("Pacific Time (US & Canada)", default_value)
    #print(n_pt)
    n_et = n_counts.get("Eastern Time (US & Canada)", default_value)
    #print(n_et)
    n_mt = n_counts.get("Mountain Time (US & Canada)", default_value)
    #print(n_mt)
    n_az = n_counts.get("Alaska", default_value)
    #print(n_az)
    n_hz = n_counts.get("Hawaii", default_value)
    #print(n_hz)
    n_ct = n_counts.get("Central Time (US & Canada)", default_value)
    #print(n_ct)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    # to give each bar its value
    performance = [n_et, n_pt, n_mt, n_az, n_ct, n_hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Negative Tweets in US Time Zones')

    # plt.show()  to display on pycharm
    # savfig= saves graph as png
    barG = plt.savefig('static/negative_barchart.png')
    plt.close()

    # timezone for  neutral tweets
    neu_timeZoneStr = []
    for tweet in neutweets:
        neu_timeZoneStr.append(tweet['timezone'])
    #print(neu_timeZoneStr)
    # print(lens(neu_timeZoneStr))

    neu_counts = Counter(neu_timeZoneStr)
    #print(neu_counts)
    neu_pt = neu_counts.get("Pacific Time (US & Canada)", default_value)
    #print(neu_pt)
    neu_et = neu_counts.get("Eastern Time (US & Canada)", default_value)
    #print(neu_et)
    neu_mt = neu_counts.get("Mountain Time (US & Canada)", default_value)
    #print(neu_mt)
    neu_az = neu_counts.get("Alaska", default_value)
    #print(neu_az)
    neu_hz = neu_counts.get("Hawaii", default_value)
    #print(neu_hz)
    neu_ct = neu_counts.get("Central Time (US & Canada)", default_value)
    #print(neu_ct)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    # to give each bar its value
    performance = [neu_et, neu_pt, neu_mt, neu_az, neu_ct, neu_hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Neutral Tweets in US Time Zones')

    # plt.show()  to display on pycharm
    # savfig= saves graph as png
    barG = plt.savefig('static/neutral_barchart.png')
    plt.close()
    ####################################
    #This is for the map
    fig, ax = plt.subplots()
    m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    m_ = Basemap(llcrnrlon=-190,llcrnrlat=20,urcrnrlon=-143,urcrnrlat=46,
                projection='merc',lat_ts=20)  # do not change these numbers
    shp_info = m.readshapefile('st99_d00','states',drawbounds=False,
                               linewidth=0.45,color='gray') #drawbounds True gives the shape of the states border
    shp_info_ = m_.readshapefile('st99_d00','states',drawbounds=False)
    popdensity = {
    #Time Zone Hawaii
    'Hawaii':  70.10,
    #Time zone Alaska
    'Alaska':     10.42,
    #Time Zone Pacific
    'California':  30.85,
    'Washington':  30.20,
    'Oregon':  30.76,
    'Nevada':  30.03,
    #Time Zone Mountain
    'Idaho':   0.40,
    'Arizona':     0.43,
    'Colorado':    0.01,
    'Montana':     0.39,
    'New Mexico':  0.79,
    'Wyoming':      0.96,
    'Utah':	 0.50,
    #Time Zone Central
    'Kansas':  150.69,
    'Nebraska':    150.60,
    'South Dakota':	 150.84,
    'North Dakota':	 150.59,
    'Alabama':     150.84,
    'Arkansas':    150.82,
    'Missouri':    150.36,
    'Texas':   150.75,
    'Illinois':    150.27,
    'Tennessee':   150.29,
    'Louisiana':   150.61,
    'Kentucky':   150.28,
    'Wisconsin':  150.13,
    'Iowa':	 150.22,
    'Minnesota':  150.86,
    'Mississippi':	 150.42,
    'Oklahoma':    150.40,
    #Time Zone Eastern
    'Indiana':    110.46,
    'Michigan':    110.55,
    'Florida':     110.43,
    'New Jersey':  110.00,
    'Rhode Island':   110.35,
    'Massachusetts':   110.68,
    'Connecticut':	  110.40,
    'Maryland':   110.23,
    'New York':    110.18,
    'Delaware':    110.87,
    'Ohio':	 110.05,
    'Pennsylvania':	 110.80,
    'Virginia':    110.03,
    'North Carolina':  110.80,
    'Georgia':     110.59,
    'New Hampshire':   110.20,
    'South Carolina':  110.45,
    'West Virginia':   110.00,
    'Vermont':     110.41,
    'Maine':  110.95}

    #%% -------- choose a color for each state based on population density. -------
    colors={}
    statenames=[]
    cmap = plt.cm.Set1
    vmin = 0; vmax = 450 # set range.
    norm = Normalize(vmin=vmin, vmax=vmax)
    for shapedict in m.states_info:
        statename = shapedict['NAME']
        # skip DC and Puerto Rico.
        if statename not in ['District of Columbia','Puerto Rico']:
            pop = popdensity[statename]
            # calling colormap with value between 0 and 1 returns
            # rgba value.  Invert color range (hot colors are high
            # population), take sqrt root to spread out colors more.
            colors[statename] = cmap(np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        statenames.append(statename)

    #%% ---------  cycle through state names, color each one.  --------------------
    for nshape,seg in enumerate(m.states):
        # skip DC and Puerto Rico.
        if statenames[nshape] not in ['Puerto Rico', 'District of Columbia']:
            color = rgb2hex(colors[statenames[nshape]])
            poly = Polygon(seg,facecolor=color,edgecolor=color)
            ax.add_patch(poly)

    AREA_1 = 0.005  # exclude small Hawaiian islands that are smaller than AREA_1
    AREA_2 = AREA_1 * 30.0  # exclude Alaskan islands that are smaller than AREA_2
    AK_SCALE = 0.19  # scale down Alaska to show as a map inset
    HI_OFFSET_X = -1900000  # X coordinate offset amount to move Hawaii "beneath" Texas
    HI_OFFSET_Y = 250000    # similar to above: Y offset for Hawaii
    AK_OFFSET_X = -250000   # X offset for Alaska (These four values are obtained
    AK_OFFSET_Y = -750000   # via manual trial and error, thus changing them is not recommended.)

    for nshape, shapedict in enumerate(m_.states_info):  # plot Alaska and Hawaii as map insets
        if shapedict['NAME'] in ['Alaska', 'Hawaii']:
            seg = m_.states[int(shapedict['SHAPENUM'] - 1)]
            if shapedict['NAME'] == 'Hawaii' and float(shapedict['AREA']) > AREA_1:
                seg = [(x + HI_OFFSET_X, y + HI_OFFSET_Y) for x, y in seg]
                color = rgb2hex(colors[statenames[nshape]])
            elif shapedict['NAME'] == 'Alaska' and float(shapedict['AREA']) > AREA_2:
                seg = [(x*AK_SCALE + AK_OFFSET_X, y*AK_SCALE + AK_OFFSET_Y)\
                       for x, y in seg]
                color = rgb2hex(colors[statenames[nshape]])
            poly = Polygon(seg, facecolor=color, edgecolor='gray', linewidth=.45)
            ax.add_patch(poly)


    custom_lines = [Line2D([0], [0], color=cmap(0.3), lw=2),
                    Line2D([0], [0], color=cmap(0.), lw=2),
                    Line2D([0], [0], color=cmap(0.6), lw=2),
                    Line2D([0], [0], color=cmap(0.5), lw=2),
                    Line2D([0], [0], marker='o', color='w',
                              markerfacecolor='black', markersize=6)
                    ]

    ax.legend(custom_lines, ['Pacific','Mountain', 'Central', 'Eastern', 'One Tweet'], loc= 4)

    lats= []
    lons= []

  #et= eastern ,pt= pacific, mt= mountain, az= alaska, ct= central, hz= hawaii,
  #If any Hawaiian time zone is dectected
    if (hz > 0):
        hzlat = 19.8968
        hzlon = -155.5828
        while hz != 0:
            hz -= 1
            lats.append(hzlat)
            lons.append(hzlon)
            hzlat += random.random()
            hzlon += random.random()
            lats.append(hzlat)
            lons.append(hzlon)
    #If any Alaska time zone is dectected
    if (az > 0):
        azlat = 64.2008
        azlon = -149.4937
        while az != 0:
            az -= 1
            lats.append(azlat)
            lons.append(azlon)
            azlat += random.random()
            azlon += random.random()
            lats.append(azlat)
            lons.append(azlon)
    #If any Eastern time zone is dectected
    if (et > 0):
        elat = 37.4316
        elon = -78.6569
        while et != 0:
            et-=1
            lats.append(elat)
            lons.append(elon)
            elat -= random.random()
            elon -= random.random()
    #If any Pacific time zone is dectected
    if (pt > 0):
        plat = 37.5
        plon = -118.5
        while pt != 0:
            pt -= 1
            #plon -= random.random()
            if plat < 37.179553 and plat > 38.635730 and plon > -114.122681 and plon < -121.450562:
                plat = 37.000
                plon = -121.4937
                lats.append(plat)
                lons.append(plon)
            else:
                lats.append(plat)
                lons.append(plon)
                plat += random.random()
                plon += random.random()

    #If any Mountain time zone is dectected
    if (mt > 0):
        mlat = 39.5501
        mlon = -105.7821
        while mt != 0:
            mt -= 1
            lats.append(mlat)
            lons.append(mlon)
            mlat += random.random()
            mlon += random.random()
    #If any Central time zone is dectected
    if (ct > 0):
        clat = 41.8780
        clon = -93.0977
        while ct != 0:
            ct -= 1
            lats.append(clat)
            lons.append(clon)
            clat -= random.random()
            clon -= random.random()

    x, y = m(lons, lats)  # transform coordinates
    #x, y = m(lonsHA, latsHA)
    m.plot(x,y, 'ko')
    #m.plot(x,y, 'ko')

    ax.set_title('Time Zone for all tweets in the United States for the result:' + " " + term)
    #plt.show()
    fig.set_size_inches(18.5, 10.5, forward=True)
    Map = fig.savefig('static/basemap.png', dpi=100)
    plt.close()