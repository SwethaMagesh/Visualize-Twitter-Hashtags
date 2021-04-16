# Visualize-Analyse-Twitter-Hashtags
## Social Network Analysis
---
- Team of 5 for Social and Economic Network Analysis project
## Proposed work
- Identify hashtags related to IPL Auction 2021
	- Like `#IPLAuction #CSK #Dhoni #MI #Gayle etc. `
- Scrap the tweets from twitter ( Library used for scrapping: ***twint*** )
- Identify the counts of hashtags and mentioned accounts and display it as ***graph and wordcloud***
- Cluster the hashtags and detect ***communities using Louvain algorithm and visualise clusters in gephi***
---
## How to view this repository
- [Scrapper folder](https://github.com/SwethaMagesh/Visualize-Twitter-Hashtags/tree/main/Scrapper) has the twint code for scrapping the tweets along with outputs
- [Dataset folder](https://github.com/SwethaMagesh/Visualize-Twitter-Hashtags/tree/main/Dataset) has the results - Tweets in a particular format (ID, date, time, text)
- [Visualise n Analyse](https://github.com/SwethaMagesh/Visualize-Twitter-Hashtags/tree/main/Visualise%20n%20Analyse) has the code to visualise as word cloud and to detect communities using Networkx
- [Clustering-Louvain](https://github.com/SwethaMagesh/Visualize-Twitter-Hashtags/tree/main/Clustering-Louvain) has the graph file and gephi workspace where the nodes are colored and visualised. The gephi workspace file has hover option to view the names of co-occuring hashtags
- [OUTPUTS](https://github.com/SwethaMagesh/Visualize-Twitter-Hashtags/tree/main/OUTPUTS) have the visualisations and outputs
- [Reports]() have the documentation of the project

---
## Sample Outputs
### VISUALISE - Bar and wordcloud representation
![image](https://user-images.githubusercontent.com/43994542/115013710-06891c80-9ecf-11eb-95e2-9fb6318d9840.png)

![image](https://user-images.githubusercontent.com/43994542/115013635-ec4f3e80-9ece-11eb-802c-bd9d557889d8.png)

### ANALYSE - Clusters in Louvain algorithm
![image](https://user-images.githubusercontent.com/43994542/115013832-2d475300-9ecf-11eb-984d-e5ac8fe6afe2.png)


---
## References
- [twint](https://github.com/twintproject/twint)
- [Analysis](https://towardsdatascience.com/visualization-of-information-from-raw-twitter-data-part-1-99181ad19c)
- [Networkx](https://python-louvain.readthedocs.io/en/latest/)
