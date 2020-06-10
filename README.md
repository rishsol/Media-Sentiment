# Media-Sentiment
Media companies are notorious for their often exaggerated headlines meant to capture the attention of users. During the height of the 2019-2020 coronavirus pandemic and later the police brutality and race riots, I wanted to determine if media headlines have been hyperbolized even more so. 

Focusing only on financial news websites, I used Python's Natural Language Toolkit (NLTK) to gauge the sentiment intensity of the headlines of 7 particular sites. (Python's NLTK measures sentiment on a scale of -1 to 1, with a -1 indicating the most negative sentiment and a 1 indicating the most positive). Headlines were scraped daily and a daily and cumulative list were created on the webpage.

From the cumulative and daily average lists seen in the image below, which represents averages at the end of the day on June 9th, 2020, the daily mean hovered around the 0.05 mark, a slightly positive sentiment, despite the currently dismal conditions. Cumulative sentiment since creating the project was slightly less than the daily sentiment average:

![sample site](https://github.com/rishsol/Media-Sentiment/blob/master/Sample%20Site.png)

In order to create a fair comparision, the pandemic and riots must come to a complete end to determine what the typical sentiment of these sites' headlines is during "normal times".

In addition, it is important to note that financial news sites may be more unbiased in their reporting. A future extension of this project would be determining sentiments of popular media sources, such as CNN and CBS, over time.
