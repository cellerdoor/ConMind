# Cliquey

ConMind is a customer segmentation tool for retail businesses that uses machine learning techniques on clickstream data to segregate online consumers as 'goal oriented' or 'experiential' shoppers. It can allow businesses to create a dynamic web layout tailored to increase shopper retention and reduce cart abandonment.  

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

#### 1) Unique Nodes

#### 2) Revisit Frequency

#### 3) Graph Diameter

#### 4) Revisit Duration



Details about feature engineering can be found in `notebooks/week3_Feature_Engineering.ipynb` .

### Model Training and Validation



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




