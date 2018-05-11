# HealthMsgU

## HealthMsgU is a web platform that enables researchers to gauge public perception and find trends regarding health topics. The web platform gathers posts using the Twitter API and analyzes them to generate visualized statistical data.

### User Stories:

#### The following required functionality needs to be completed for the MVP:

* User can enter search terms in a search field
* Tweets are pulled using Twitter's API and the Tweepy API
* An error message is displayed if no pertinent messages are found
* User can move seamlessly between visualizations using dropwdown menu
* Frequency of words associated with search terms can be viewed
* A map will display the time zone location of where the Tweets are being generated
* User can view data as a word cloud based on frequency
* User can learn more about the project by clicking "About Us" from the navigation bar
* Sentiment analyses is performed on the tweets displaying positive, negative and neutral results.

#### The following features will be implemented:

* User can gather data from other social media outlets such as Facebook and reddit (web-scraping)
* A loading animation will display while rensults are rendered.
* User can customize generated word cloud, eg: change fonts, colors, isolate certain words
* There can be a history of previous word clouds plotted with dates (e.g the most recent cloud or the most frequently plotted word association) (Database configuration)
* Web platform can pull more than 7 days of Tweets
* 3rd party authentication for user login (Facebook, Google, security)

#### Tasks our group needs to do to create the MVP:

- [X] Host website
- [X] Generate an informative blurb about HealthMsgU
- [x] Create a user interface to allow the user to have search input
- [x] Word Cloud generator: generates a word cloud depicting the most common words associated with HIV on Twitter
- [x] Implement Google Maps API to display Tweet locations
- [x] Implement sentiment analyses algorithm

### Architecture:

**Web host:** Horoku, GitHub pages

**Languages used:** HTML, CSS, JS, Python

**API's used:** Twitter, Tweepy, Flask, Google Maps, TextBlob, Word cloud

**Resources:**  
[Hedonometer](http://hedonometer.org/index.html)  
[Word cloud resource](https://github.com/amueller/word_cloud)  
[A great article illustrating why our project is relevant](https://www.nytimes.com/2017/09/21/opinion/sunday/-truvada-gay-hiv-aids.html?_r=0)  


### Storyboard:

**Home Page**

![Home Page](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/Homepage.PNG)

**Navigation Tabs**

![Tabs](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/Tabs.PNG)

**Word Cloud**

![Word Cloud](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/Wordcloud.PNG)

**Word Association**

![Word Association](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/wordassociation.PNG)

**Message Map**

![Map](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/Map.PNG)

**Message Timeline**

![Timeline](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/Timeline.PNG)

**About Us**

![About Project](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/AboutProject.PNG)

**Contact Us**

![Contact Us](https://github.com/CSC698-TeamPrep/HealthMsgU/blob/master/static/Photo_Storyboard/Contact_us.PNG)
