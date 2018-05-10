import matplotlib.animation as animation
import matplotlib.pyplot as plt
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
from os import path
from wordcloud import WordCloud, STOPWORDS

def data_vis(tweets, ptweets, ntweets, term):
    strOfAllTweet = " "
    strOfPosTweet = " "
    strOfNegTweet = " "
    strOfNeuTweet = " "

    # This removes the // from http
    remove_back = lambda s: ' '.join(i for i in s.split() if '//' not in i)
    #This will make all the tweet text as one str
    alltweets = [tweet for tweet in tweets if
                 tweet['sentiment'] == 'negative' or tweet['sentiment'] == 'positive' or tweet[
                     'sentiment'] == 'neutral']
    for tweet in alltweets:
        strOfAllTweet += " " + tweet['text']
        
    #This gets rid of any words that starts with @ and & for all tweets
    newStrAll = " ".join(list(filter(lambda x: x[0] != '@', strOfAllTweet.split())))
    newStrAll2 = " ".join(list(filter(lambda x: x[0] != '&', newStrAll.split())))
    strOfAllTweet = remove_back(newStrAll2)

    # This will make positive tweet text as one str
    for tweet in ptweets:
        strOfPosTweet += " " + tweet['text']  
    #This gets rid of the @ username and &amp for positive tweets
    newStrPos = " ".join(list(filter(lambda x:x[0]!='@', strOfPosTweet.split())))
    newStr2 = " ".join(list(filter(lambda x: x[0] != '&', newStrPos.split())))
    strOfPosTweet = remove_back(newStr2)

    #This will make negative tweet text as one str
    for tweet in ntweets:
        strOfNegTweet += " " + tweet['text']
    #This gets rid of the @ username and &amp for negative tweets
    newStrNeg = " ".join(list(filter(lambda x: x[0] != '@', strOfNegTweet.split())))
    newStrNeg2 = " ".join(list(filter(lambda x: x[0] != '&', newStrNeg.split())))
    strOfNegTweet = remove_back(newStrNeg2)
 
    #This will make neutral tweets as a one str
    neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    for tweet in neutweets:
        strOfNeuTweet += " " + tweet['text']
    #This gets rid of the @ username and &amp for neutral tweets
    newStrNeu = " ".join(list(filter(lambda x: x[0] != '@', strOfNeuTweet.split())))
    newStrNeu2 = " ".join(list(filter(lambda x: x[0] != '&', newStrNeu.split())))
    strOfNeuTweet = remove_back(newStrNeu2)
    
    ##########################################################
    #This makes the word cloud
    #This add additional stopwords
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
        plt.title('All Tweets', fontsize=20)
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
        plt.title('Positive Tweets', fontsize=20)
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
        plt.title('Negative Tweets', fontsize=20)
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
        plt.title('Neutral Tweets', fontsize=20)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig('static/WordCloudNeu.png')
        plt.close()
    ########################################################
    # This makes the time zone Bar graph
    
    timeZoneStr = []
    for tweet in alltweets:
        timeZoneStr.append(tweet['timezone'])

    counts = Counter(timeZoneStr)
    default_value = 0  # the default_value gives you a 0 for the time zone,
    # as sometimes a timezone isn't there and then its value will be none and this mess up the code
    pt = counts.get("Pacific Time (US & Canada)", default_value)
    et = counts.get("Eastern Time (US & Canada)", default_value)
    mt = counts.get("Mountain Time (US & Canada)", default_value)
    az = counts.get("Alaska", default_value)
    hz = counts.get("Hawaii", default_value)
    ct = counts.get("Central Time (US & Canada)", default_value)

    fig = plt.figure
    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    
    # to give each bar its value for all time zone
    performance = [et, pt, mt, az, ct, hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Tweets in US Time Zones')
    plt.savefig('static/barchart.png')
    plt.close()

    # timezone for  positive tweets
    p_timeZoneStr = []
    for tweet in ptweets:
        p_timeZoneStr.append(tweet['timezone'])

    p_counts = Counter(p_timeZoneStr)
    p_pt = p_counts.get("Pacific Time (US & Canada)", default_value)
    p_et = p_counts.get("Eastern Time (US & Canada)", default_value)
    p_mt = p_counts.get("Mountain Time (US & Canada)", default_value)
    p_az = p_counts.get("Alaska", default_value)
    p_hz = p_counts.get("Hawaii", default_value)
    p_ct = p_counts.get("Central Time (US & Canada)", default_value)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    
    # to give each bar its value for positive 
    performance = [p_et, p_pt, p_mt, p_az, p_ct, p_hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Positive Tweets in US Time Zones')
    barG = plt.savefig('static/positive_barchart.png')
    plt.close()

    # timezone for  negative tweets
    n_timeZoneStr = []
    for tweet in ntweets:
        n_timeZoneStr.append(tweet['timezone'])

    n_counts = Counter(n_timeZoneStr)
    n_pt = n_counts.get("Pacific Time (US & Canada)", default_value)
    n_et = n_counts.get("Eastern Time (US & Canada)", default_value)
    n_mt = n_counts.get("Mountain Time (US & Canada)", default_value)
    n_az = n_counts.get("Alaska", default_value)
    n_hz = n_counts.get("Hawaii", default_value)
    n_ct = n_counts.get("Central Time (US & Canada)", default_value)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    
    # to give each bar its value negative
    performance = [n_et, n_pt, n_mt, n_az, n_ct, n_hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Negative Tweets in US Time Zones')
    barG = plt.savefig('static/negative_barchart.png')
    plt.close()

    # timezone for  neutral tweets
    neu_timeZoneStr = []
    for tweet in neutweets:
        neu_timeZoneStr.append(tweet['timezone'])
    neu_counts = Counter(neu_timeZoneStr)
    neu_pt = neu_counts.get("Pacific Time (US & Canada)", default_value)
    neu_et = neu_counts.get("Eastern Time (US & Canada)", default_value)
    neu_mt = neu_counts.get("Mountain Time (US & Canada)", default_value)
    neu_az = neu_counts.get("Alaska", default_value)
    neu_hz = neu_counts.get("Hawaii", default_value)
    neu_ct = neu_counts.get("Central Time (US & Canada)", default_value)

    fig = plt.figure

    objects = ('Eastern  ', 'Pacific  ', 'Mountain  ', 'Alaska', 'Central  ', 'Hawaii')
    y_pos = np.arange(len(objects))
    
    # to give each bar its value for neutral tweets
    performance = [neu_et, neu_pt, neu_mt, neu_az, neu_ct, neu_hz]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tweets')
    plt.title('Neutral Tweets in US Time Zones')
    barG = plt.savefig('static/neutral_barchart.png')
    plt.close()
    ####################################
    
    #This creates the map
    
    fig, ax = plt.subplots()
    m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    m_ = Basemap(llcrnrlon=-190,llcrnrlat=20,urcrnrlon=-143,urcrnrlat=46,
                projection='merc',lat_ts=20)  
                
    shp_info = m.readshapefile('st99_d00','states',drawbounds=False,
                               linewidth=0.45,color='gray') 
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
            colors[statename] = cmap(np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
        statenames.append(statename)

    #cycle through state names, color each one. 
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
    AK_OFFSET_X = -250000   # X offset for Alaska 
    AK_OFFSET_Y = -750000   

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
        hzlat = 27
        hzlon = -105
        while hz != 0:
            hz -= 1
            lats.append(hzlat)
            lons.append(hzlon)
            if(hz% 2 == 0):
                hzlat += random.uniform(0.0, 1.0)
                hzlon += random.uniform(0.0, 1.0)
            else:
                hzlat -= random.uniform(0.0, 1.0)
                hzlon -= random.uniform(0.0, 1.0)    
    #If any Alaska time zone is dectected
    if (az > 0):
        azlat = 27
        azlon = -107
        while az != 0:
            az -= 1
            lats.append(azlat)
            lons.append(azlon)
            if(az% 2 == 0):
                azlat += random.uniform(0.0, 1.0)
                azlon += random.uniform(0.0, 1.0)
            else:
                azlat -= random.uniform(0.0, 1.0)
                azlon -= random.uniform(0.0, 1.0)
                    
    #If any Eastern time zone is dectected
    if (et > 0):
        etlat = 38
        etlon = -79
        while et != 0:
            et -= 1
            lats.append(etlat)
            lons.append(etlon)
            if(et% 2 == 0):
                etlat += random.uniform(0.0, 1.0)
                etlon += random.uniform(0.0, 1.0)
            else:
                etlat -= random.uniform(0.0, 1.0)
                etlon -= random.uniform(0.0, 1.0)
    #If any Pacific time zone is dectected
    if (pt > 0):
        plat = 40
        plon =  -118.5
        while pt != 0:
            pt -= 1
            lats.append(plat)
            lons.append(plon)
            if(pt% 2 == 0):
                plat += random.uniform(0.0, 1.0)
                plon += random.uniform(0.0, 1.0)
            else:
                plat -= random.uniform(0.0, 1.0)
                plon -= random.uniform(0.0, 1.0)

    #If any Mountain time zone is dectected
    if (mt > 0):
        mlat = 40
        mlon = -110.5
        while mt != 0:
            mt -= 1
            lats.append(mlat)
            lons.append(mlon)
            if(mt% 2 == 0):
                mlat += random.uniform(0.0, 1.0)
                mlon += random.uniform(0.0, 1.0)
            else:
                mlat -= random.uniform(0.0, 1.0)
                mlon -= random.uniform(0.0, 1.0)    
    #If any Central time zone is dectected
    if (ct > 0):
        clat = 40
        clon = -94.5
        while ct != 0:
            ct -= 1
            lats.append(clat)
            lons.append(clon)
            if(ct% 2 == 0):
                clat += random.uniform(0.0, 1.0)
                clon += random.uniform(0.0, 1.0)
            else:
                clat -= random.uniform(0.0, 1.0)
                clon -= random.uniform(0.0, 1.0)   
    x, y = m(lons, lats)  # transform coordinates
    m.plot(x,y, 'k.')

    ax.set_title('Time Zone for all tweets in the United States for the result:' + " " + term, fontsize=14)
    fig.set_size_inches(8, 8, forward=True)
    Map = fig.savefig('static/basemap.png', dpi=100)
    plt.close()