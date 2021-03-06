# Cliquey

Cliquey is a customer segmentation tool for retail businesses that uses machine learning techniques on clickstream data to segregate online consumers as 'goal oriented' or 'experiential' shoppers. It can allow businesses to create a dynamic web layout tailored to increase shopper retention and reduce cart abandonment.  

Goal-oriented shoppers desire to purchase what they want quickly and without distraction, whereas experiential customers tend to spend more time, browse a larger variety of items, and enjoy a foraging attitude to shopping. 

Traditional market segmentation tools rely on demographic or geographic differences, rather than differentiating consumers on their transient behavioural shopping attitudes. This tool identifies and provides an actionable opportunity for retailers to better personalize their web interface based on the consumer's transient shopping behaviour and preferences. 

I employ Gaussian mixture models and perform unsupervised learning to identify these segments.

# Prerequisites and Data aquisition

The raw data used for this analysis is semi-proprietary but a sample of the attributes available has been made available in the file Sample_data.ipynb. Please get in touch with me (lavisha.jindal@gmail.com) for directions on how to obtain the entire dataset.

To run Cliquey on a local system, please install sklearn and python 3.7
Information on how to create a Dash website is available in the folder Dash along with instructions for the web deployment

# Result

I use multivariate Gaussian Mixture modelling to cluster individual clickstreams as either 'Goal oriented' or 'Experiential'. This tool can be used to improve sales funnel transitions and its effect can be easily measured through A/B testing. Since the underlying features are based on Graph architectures, it is scalable and ideal for large datasets. Using unsupervised learning to recognizing patterns in customer interaction with the platform can also be used for anomaly detection and to prevent attacks.

## How Does Cliquey Work?
### Workflow
![workflow](https://github.com/cellerdoor/ConMind/blob/master/Files/workflow1.jpg)

### Graph Encoding
The raw data for this project includes the following information: Clicks on unique anonymized products by anonymized users over a period of one month. From these clicks the sequence of products visited can be extracted as it also contains time of visit. A single clickstream is defined as the sequence of product visits preceeding a purchase. When a purchase is made, a new clickstream in initiated. 

By associating a unique integer value with every member of the ordered set of unique products visited by a single user, we can construct a graph corresponding to each session where vertices represent products and the sequence of visits is used to associate the vertices through edges. A simple sample is shown below:
![encoding](https://github.com/cellerdoor/ConMind/blob/master/Files/encoding.jpg)


### Feature Engineering
#### 1) Fractional Unique Nodes
This feature calculates the total number of unique nodes visited divided by the total number of nodes visited during a single session. It is bounded by (0,1] and clickstreams analogous to 'experiential' will have values close to 1 while clickstreams belonging to 'goal oriented' nature would be closer to 0. A lower value would imply a higher level of 'goal oriented'.

#### 2) Revisit Frequency
This feature calculates the total number of revisits to a previously visites unique node during a single session. It is unbounded and clickstreams analogous to 'experiential' will have lower values while clickstreams belonging to 'goal oriented' nature would have high number of revisits. 


#### 3) Graph Diameter
This feature calculates the longest path between two unique nodes in the clickstream. It is unbounded and is used to further segregate 'goal oriented' (which would have a lower diameters) and 'experiential' users (which would have higher diameters). This feature also segregates clickstreams that show mixed behaviours such that more 'goal oriented' clickstreams can be differentiated from less 'goal oriented' clickstreams.

#### 4) Revisit Duration
This feature calculates the time spent on the same product (only) during a revisit. Using this feature is based on the assumption that customers spend a longer time browing and reading the description of products when they have a specific goal in mind and that product aligns with this goal. 'Experiential' customers spend less time in comparison on a revisited product. 

We have chosed our features based on a qualitative understanding of what behaviours are likely associated with 'Goal oriented' and 'Experiential' customers. The caveat is that there is no 'true' underlying latent state that is associated with shopping patterns and the construction of this binary is based upon a heuristic approach to consumer behaviours. 

Details about feature engineering can be found in `notebooks/Feature_Engineering.ipynb` .

### Model Results
<img src="https://github.com/cellerdoor/ConMind/blob/master/Files/results.jpg" alt="drawing" width="450"/>

### Cluster Stability 

### Visual Validation


## Limits and Future Directions
Cliquey was built during a short time period (2.5 weeks) as part of the Insight Data Science program. Future improvements include:
* Including a Beta regression model that takes demographic data to forecast purchases
* Alters a session by only considering clickstream within a time-duration as a single session
* Create user-specific priors that can predict the mindset of the user within a few clicks
 

# Website

An interactive website, where the entire data journey and the resulting clusters for a sample of the data set have been visualized can be found on lavishaj.pythonanywhere.com

[![Cliquey Demo](/Files/Demo_pic.jpg)](http://lavishaj.pythonanywhere.com/)

# Acknowledgement 

This project has benefitted immensely from crucial inputs by the project directors at Insight-Toronto, the past members of the Insight family and members of my cohort.  

## Contact
* **Author**: Lavisha Jindal
* **Email**: lavisha.jindal@gmail.com
* **Linkedin**: https://www.linkedin.com/in/lavishajindal/




