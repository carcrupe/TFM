# Master thesis - Heart Stroke Predictor

## Table of Contents  
- [Introduction](#Introduction)  
- [Data description](#Data-description)  
- [Methodology](#Methodology) 
  * [1. Prepare the notebook with the data and requirements](#Prepare-the-notebook-with-the-data-and-requirements)
  * [2. Data cleaning](#Data-cleaning)
  * [3. Feature extraction](#Feature-extraction)
  * [4. Feature selection](#Feature-selection)
  * [5. Machine Learning modeling](#Machine-Learning-modeling)  
- [Summary of main results](#Summary-of-main-results)  
- [Conclusions](#Conclusions)  
- [Run and use the web app](#Run-and-use-the-web-app)  


## Introduction

Nowadays cardiovascular diseases are the leading cause of death globally. In particular, [isquemic heart or stroke](https://ourworldindata.org/causes-of-death#what-do-people-die-from) have led the ranking in the last 15 years. In addition, it is very hard to anticipate a stroke episode and usually when it is detected, it is too late for a treatment, resulting in severe problems or death.

To anticipate a stroke in advance, heart electrophysiological indicators or arrythmia information might be very useful. For example, a very good indicator could be to diagnose the patient with [atrial fibrilation](https://www.cdc.gov/heartdisease/atrial_fibrillation.htm), since it is the most common arrythmia and seems to be related to a stroke over time. However, to detect and treat these kind of arrythmias one needs an experienced specialist and dedicated technology, which unfortunately, cannot be guaranteed for this really demanding disease. 

Here is where data plays a very important role and offers a really good opportunity to better understand and predict strokes. If we had relevant heart related data, we could take a huge step in the healthcare world, allowing anticipated patient treatments and saving an uncountable amount of lives.

In this project, with the data I could obtain for free, I have worked to create a binary classification model and answer the following question:

#### Based on measurable patient parameters, is this patient likely to suffer a stroke?

## Data description

[Stroke data](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)</br>

In the dataset almost 70.000 patients will be explored and analyzed based on the following features: age, sex,	height, weight, systolic pressure, diastolic pressure, cholesterol, diabetes, and habits like smoke, alcohol or sport. The target will be whether the patient suffered a stroke episode or not.

As we can see, we have two types of features, categorical and continuous, which will help predict the target.

## Methodology

[Notebook with EDA of the dataset](https://github.com/carcrupe/TFM/blob/master/notebooks/stroke_exploring_data.ipynb)</br>

I will describe briefly the different steps taken in the notebook. For a further and detailed explanation, please refer to the [notebook](https://github.com/carcrupe/TFM/blob/master/notebooks/stroke_exploring_data.ipynb).</br>

### 1. Prepare the notebook with the data and requirements

To provide an easy-to-use notebook, the first cells are to download the appropriate data and install the necessary libraries. You can run the notebook without downloading any other file.

### 2. Data cleaning 

In this section,the first thing is to assess null values and duplicates. Since there are not many I decided to delete these observations, lossing only 5% of the data. 

Moreover, for the continuous features, I have evaluated the outliers. To do that I have written a function that measures the amount of outliers for a given property and calculates Q1, Q3 and the IQR (inter quartile range Q3-Q1). Based on these three parameters I decided to discard, for each feature, all the observations below (Q1 - 1.5 x IQR) and above (Q3 + 1.5 x IQR). I have taken this decision based on the conventional definition of outliers, detailed [here](https://en.wikipedia.org/wiki/Interquartile_range).

### 3. Feature extraction

Now that the data are clean and without outliers, in order to improve the insights I have created two new features, BMI (Body Mass Index) and Pulse (derived from the pressures). The idea of the feature extraction is to obtain new valuable data to improve our model.

### 4. Feature selection

If you have more features in the data, it does not necessarily mean your data is better and your model performs better. It is time to evaluate each characteristic and do the feature selection for the modeling. For that purpose, I run the correlation between all independant properties and the target. 

In fact, having irrelevant features in data can decrease the accuracy of the model and make it learn based on unrelated aspects. High correlation within independent features means that they represent the same thing and when you drop one of them, you do not lose much data quality.

Taking into account this previous explanation, my goal is to select features with good correlation with the target and low correlation with any other independent feature.

Eventually, based on the correlation matrix, the [selected features](https://github.com/carcrupe/TFM/blob/master/data/stroke_data_for_modeling.csv) for my model are: Age, SystolicPressure, DiastolicPressure, Cholesterol, Pulse.

### 5. Machine Learning modeling

[Notebook with Machine Learning models](https://github.com/carcrupe/TFM/blob/master/notebooks/stroke_predictor_models.ipynb)</br>

Since my purpose is to predict a binary output (having or not having a stroke), I will be training a few classification models with the selected features. Again, this notebook can be run without any other file or data, all is ready to be installed and downloaded at the begining of the notebook.

Before starting with the modeling, I will define a metric to evaluate the performance of the classifier. Since I do not want any patient potentially suffering from stroke to be misdiagnosed, I need to minimize the amount of false negatives. Therefore, the metric I chose to evaluate my model is the recall. The higher the recall, the lower the false negatives and thus, more patients will be diagnosed for further evaluation.

The steps I followed for training and evaluating each model are: 

1. Divide the data in train and test sets, setting the test 20% of the data.
2. Define the model with default hyperparameters and fit the training set.
3. Predict with the trained model and see recall performance to have a first overview.
4. Improve model performance tuning hyperparameters manually, using GridSearch or Randomized search.
5. Fit the model with the optimized hyperparameters and evaluate again for recall.
6. Plot the confusion matrix and classification report to better evaluate model performance.
7. Use cross validation with recall as score. Calculate the mean of all cross-validated runs and store it as model performance metric.
8. Finally, select the model with the highest recall and performance. In my case it is the Random Forest model.

## Summary of main results

After the exploratory analysis of the data I found out that parameters such as systolic pressure, diastolic pressure or choleterol have different distribution depending on the target. This will possibly make these features important predictors. Also, I confirmed that the number of strokes increases with the age, which is something we could expect and should also be helpful for training the model.

According to the model performance, I have accomplished a recall of around 69%. Despite the fact that the model has been optimized, the perfomance has not improved much. This might be the result of poor data quality or simply not enough data to make the model learn properly. Obtaining clinical data is very complicated and unfortunately, I wish I had had more data to do my research.

## Conclusions

#### Based on measurable patient parameters, is this patient likely to suffer a stroke?

I have worked to solve a really relevant problem, which nowadays causes the highest amount of deaths worldwide. Detecting a stroke in advance is obviously not an easy task and it has been in research for many years. 

With my work, I could not obtain a very high recall and I have learnt how important is to have valuable data to answer a given question reliably. In particular, in this complex problem, I should have included much more information about the patients. The bottleneck here is that this information is very sensitive and confidential, and therefore, it was very hard for me to obtain the right data. 
However, for those who have access to cardiovascular databases, I would recommend to include parameters such as sleep time, left/right atrial size, left/right ventricle size, kidney diseases, aorta ejection rate or percentage of oxygenated blood.  With all these parameters in mind, I am sure predictions would be much more accurate, providing precise results and hopefully, allowing to have a tool to get to know the stroke likelihood of your own heart.

Again, the challenge remains in acquiring the right data to do the research.

## Run and use the web app

To finalize the project, I have created a simple web application with [Streamlit](https://www.streamlit.io/). The application runs the best trained classifier (Random Forest) and predicts the input that the user sets. There are two ways to run the app:

**Streamlit notebook:** From the repository notebook folder download and run the file [stroke_stream.ipynb](https://github.com/carcrupe/TFM/blob/master/notebooks/stroke_stream.ipynb). You can run this notebook without previously training the model, it will by default use the pretrained model that I have saved in my repository. To show the app, I create a ngrok tunnel to expose my local server in a dinamically created URL.

**Running the docker file:** I have created a docker container with all the needed information to install and run the streamlit application. The instructions to execute the app are:

- In the terminal, navigate to the project folder, which contains the Dockerfile.
- Build the docker image: *sudo docker build -f Dockerfile -t stroke_app .*
- Run the image: *sudo docker run -p 8501:8501 stroke_app*

*To do this it is assumed you have docker installed in your computer and you have superuser permission.*

**Deploy the app in the Cloud:** As an alternative, if you do not have Docker installed in your computer or you want to deploy the classifier in the Cloud, you can use Google Cloud, AWS or Azure to do it. In my case, I have used the Compute Engine tool from GCP. Here are the steps for the deployment:

- Within Google Cloud Platform, open the Compute Engine section and create a Virtual Machine with all default settings.
- Establish a secure connection with the new Virtual Machine by clicking on the SSH button.
- After clicking the SSH button, the VM console will open. Follow the next steps in the console to run the app:
  - Install Git: *sudo apt-get install git*
  - Clone the project from the git repository: *git clone https://github.com/carcrupe/TFM.git*
  - Install Docker by running the two following commands separately:  *sudo apt-get install docker* , *sudo curl -sSL https://get.docker.com/ | sh* 
  - Execute the instrucions detailed in the previous *Running the docker file* section, to deploy the docker container.
  - The app will be running at the corresponding network URL, allowing every user to predict his/her heart stroke status with the trained classifier.

