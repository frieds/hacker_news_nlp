This repo contains a natural language processing project completed on the latest 250K Hacker News posts. 

Blog post at: http://dfrieds.com/Hacker-News-Comments-Analysis/

- hn_analysis.ipynb is data analysis using Python, Pandas, Numpy and Matplotlib; cleaned data, performed text pre-processing, 
used LDA and KMeans clustering methods, and ultimately foudn a word2vec model revelead the best context for the data
- hn_api_crawler.py is code to crawl the Hacker News API and dump the data into a MongoDB database