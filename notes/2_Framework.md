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

![6-step-ml-framework](https://user-images.githubusercontent.com/74961891/167846239-2886a2b7-e756-4f02-a19b-993487b2de9c.png)

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
   * Problem - What defines success in our case?
   * evaluation metric is a measure of how well machine learning algorithm predicts the future
   * there are different evaluation metrics for different machine learning problems  
   

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
   * Known information about the data are called features
   * Process of working with features is called feature engineering
   * Ideal scenario is to have data with the same features
   * Variables:
     
     * feature variables (known data)
        * numerical features 
            * numbers - age or body weight, etc.
        * categorical features 
            * one thing or another - male or female, smoker or non-smoker, etc.
        * derived features 
            * creating new or altering features based on different existing features 
            * example: I can create derived feature that will tell if patient has visited doctor last year based on the 
              hospital data. This is the way how you can derive new feature from existing features.
     
     * target variables (unknown data) 
        * this is what we want to predict
       

   * Example: We want to predict heart disease from patients records containing weight, sex, heart rate and chest pain
     We call those data feature variables. We want to use feature variables to predict target variables - in our case
     target variable is a decision if patient have heart disease or not (yes/no)
     

##########################################################################################################

## 5) Modelling
   * Problem - What model should we use based on our problem definition and data?
   * Generalisation - ability of machine learning model to perform well on data it hasn't seen before 
   * Data split:
      * Training set - training a model with those data (70-80%)
      * Validation set - Tune your model on those data (10-15%)
      * Testing set - Test and compare on those data (10-15%) 
    

   * Why you need to split your dataset:
     * it's similar to learning for a math exam. You initially learn from the math
       lessons materials (training phase). Then you do some practice exams on your own to 
       verify your gained knowledge (validation phase). Finally, you take a final exam at school (testing phase) to test
       your knowledge on the examples that you've never seen before. This adaptation that you get from the lessons 
       materials and practice exams to complete final exam refers to the machine learning as generalisation.
     * When things go wrong - If your final exam will be same as the practice exam, everybody in the class will
       pass the math exam with top marks. But, did the students really learn anything?
     

### a) Choosing and training a model
   * Dataset: training data
   * Some models work better than others on different problems  
   * But which algorithm/model is suitable for my problem?  
     * structured data:
        * Decision tree algorithms - Random Forest 
        * Gradient boosting algorithms - XGBoost, CatBoost
     * unstructured data:
        * Deep learning algorithms - Neural networks
        * Transfer learning
   * Always start small and build up (add complexity) as you need. If you have a million of records in your initial
     dataset, you don't need to work with all of them. Start with the 10 thousands and add complexity later on.


### b) Tuning a model
   * Dataset: validation data
   * Goal is to improve initial performance of the model trained with training dataset
   * Model can be tuned for different types of data - similar to F1 car that can be tuned for different types of tracks
      * if you don't have a validation dataset, you can tune up your model with training data 
   * Machine learning models have hyper-parameters you can adjust
   * Tuning can take place on training or validation data sets


### c) Model comparison
   * Dataset: test data
   * Keep the test set separate at all costs
   * Test set is like a final exam for a machine learning models  
   * You might train a different models on the same data, but how to choose the best one?
   

   * Testing a model:
      * We want to avoid underfitting and overfitting problems
      * Underfitting: 
         * Happens when training set performance is dramatically higher than a test set performance
         * Poor performance on training data means the model hasn’t learned properly and is underfitting
         * Data mismatch - happens when data you're testing on is different that the data you're training on - having
                           different features in your testing and training data. Having this kind of mismatch is leadin
                           to underfitting
      * Overfitting:
         * Happens when test set performance is higher than training set performance
         * Great performance on the training data but poor performance on test data means your model doesn’t generalize well. Your model may be overfitting the training data
         * Data leakage - happens when some of your test data leaks into your training data, which results in overfitting 
   

   * Fixes for underfitting:
      * Try more advanced model
      * Increase model hyper-parameters
      * Reduce amount of features - model could struggle to find a patterns in data
      * Train longer
       

   * Fixes for underfitting:
      * Collect more data
      * Try less advanced model

 ![image](https://user-images.githubusercontent.com/74961891/167783433-2431b6e8-1173-4207-a338-39b0a52d3dd9.png)

   * Comparing of models:
     * Make sure you're comparing apples with apples and oranges with oranges
     * Meaning that it make sense to compare different models performances that were trained with the same data
     * One best performance metric does not equal best model
    

##########################################################################################################

## 6) Experimentation
   * Problem - What have we tried and what else we can try?
      * This is iterative process that starts at stage 1 (problem definition) and ends at stage 5 (modeling)
      * Try different model
      * Try to change parameters slightly
