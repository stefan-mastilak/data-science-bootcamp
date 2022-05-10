----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

How we will proceed:
--------------------
1) Create a framework
    * general framework based on the above schema
   

2) Match to data science and machine learning tools
    * there are existing tools for variety of problems
   

3) Learn by doing
    * create a projects to build portfolio of the skills and tools
   

General idea for machine learning framework:
--------------------------------------------

1) Problem definition
   * supervised or unsupervised learning?
   * classification or regression problem?
   

2) Data
   * data is requirement for any ML project
   * what kind of data we have? 
        - structured? (spreadsheet, database, etc.)
        - unstructured? (images, audio, etc.)
   

3) Evaluation
   * define what success means for us
   * evaluation metrics
   

4) Features
   * what do we already know about the data?
   * numerical or categorical data
   

5) Modeling
   * what model should we used based on the problem and data that we have?


6) Experiments
   * how could we improve?
   * what can we try next?

![ml_framework drawio](https://user-images.githubusercontent.com/74961891/167399711-08876d1d-649d-41ad-9b3f-88e240925b28.png)

################################################################################################################

## 1) Problem definition

Types of machine learning problems:
-----------------------------------

### a) Supervised learning
   * data with labels ("I know my inputs and outputs")
   * algorithm tries to use data to predict labels
   * if it guesses a label wrong, algorithm corrects itself and tries again 
   * this active correction is why it's called supervised
   * purpose of label is to provide a context  
   * labels might indicate whether a photo contains a bird or car, which words were uttered in an audio recording, 
     or if an x-ray contains a tumor. Data labeling is required for a variety of use cases including computer vision, 
     natural language processing, and speech recognition
     
   #### Classification problem
   * Problem - Is this example one thing or another?
   * Binary classification - two options (Does patient have heart disease based on medical records?)
   * Multi-class classification - more than two options (What type of breed is this dog based on photo?)

   #### Regression problem
   * Problem - How much will this house sell for? Or How many people will buy this app?
   * In general, we're trying to predict a number here
   * like number of days, sell price of the house, number of clicks or website visits, etc.


### b) Unsupervised learning
   * data has no labels ("I'm not sure about the outputs, but I have inputs")
   * goal is to find patterns in the data and group similar things together
   * data in the same group (cluster) will have same labels
   * clustering is the process of putting groups of similar examples together 
     
   * Example 1: You have customer purchase data. You want to send promotion for the summer clothes to the customers.
     So based on the purchase data you need to split the customers into the two groups. Those who purchase mostly during 
     the summer, and the second group of customers that purchase mostly in winter. So you will label them as winter and
     summer customers. Problems like this are also called the clustering
     
   * Example 2: Recommendation problem is also unsupervised learning problem (like recommend a next song to play etc.) 
     

### c) Transfer learning
   * type of learning that takes existing model and use its foundational patterns and apply it to the another problem
   * "I think my problem may be similar to something else"  
   * Example: You have a model that can detect a car on the picture. You want to create a model that will be able to
     detect a dog on the picture. You can use existing car model and transfer some useful patterns from that model 
     to the new one for dogs detection.
     
### d) Reinforcement learning
   * involves having a computer program performing some actions within a defined space and rewarding it for doing well
     and punishing it for doing poor. This could be achieved by assigning a score for the performed action. Goal for 
     the algorithm could be to achieve the highest possible score. 
   * Example: Good example is teaching algorithm to play chess. If computer wins, algorithm will learn moves that led 
     to win. Board is a space and actions are movements of pieces on the chess board.
     
################################################################################################################

## 2) Data

Different types of data:
------------------------

### a) structured data
   * all of a samples/records are typically in the similar format
   * excel files, csv files, database tables

### b) unstructured data
   * samples/records has totally different formats
   * images, natural language text (transcript phone calls, videos and audio files)


### Data could be:
   * static - data that doesn't change over time (csv files, etc.)
   * streaming - data that are constantly changing over time 

### Data science workflow:
   * Input - Static data
   * Jupyter notebook
   * Data analysis - Pandas 
   * Data visualisation - Matplotlib
   * Building a model - Scikitlearn

################################################################################################################

## 3) Evaluation
   * evaluation metric is a measure of how well machine learning algorithm predicts the future
   * there are different evaluation metrics for different machine learning problems  
   * what defines success?

### Different types of metrics for Classification:
   * Accuracy
   * Precision
   * Recall

### Different types of metrics for Regression:
   * Mean absolute error (MAE)
   * Mean squared error (MSE)
   * Root mean squared error (RMSE)

### Metrics for Recommendation:
   * Precision at K 
   * Example: K is a number - top 10 recommendations for songs made by algorithm

################################################################################################################

## 4) Features