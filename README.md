# Master thesis - Heart Stroke Predictor

## Introduction

Nowadays cardiovascular diseases are the leading cause of death globally. In particular, [isquemic heart or stroke](https://ourworldindata.org/causes-of-death#what-do-people-die-from) remained the leading causes of death globally in the last 15 years. In addition, it is very hard to anticipate a stroke episode and usually when it is detected, it is too late for a treatment, resulting in severe problems or death.

To anticipate a stroke in advance, heart electrophysiological indicators or arrythmia information might be very useful. For example, a very good indicator of a potential stroke could be a patient with [atrial fibrilation](https://www.cdc.gov/heartdisease/atrial_fibrillation.htm), since it is the most common arrythmia and seems to be related to a stroke over time. However, to detect and treat these kind of arrythmias one needs an experienced specialist, dedicated technology and attention, which unfortunately, cannot be guaranteed for this really demanding disease. 

Here is where data plays a very important role and offers a very good opportunity to better understand and predict strokes. This would be a realy big step in the healthcare world, allowing anticipated patient treatments and saving an uncountable amount of lives.

In this project I have worked to answer the following question: 

#### Based on simple patient paramenters, is this patient going to have a stroke?

## Data description

[Stroke data](https://www.kaggle.com/sulianova/cardiovascular-disease-dataset)</br>
In the dataset almost 70.000 patients will be explored and analyzed based on the following features: age, sex,	height, weight, systolic pressure, diastolic pressure, cholesterol, diabetes, smoker, alcoholic, active sport. The target will be weather the patient suffered a stroke episode or not.

As we can see, we have two types of features, categorical and continuous, which will help predict the target.

I have done an exploratory analyisis of the data and found out that parameters such as systolic pressure, dyastilic pressure or choleterol have different distribution depending on the target. This will make these features important predictors. Also, I confirmed that the number of strokes increases with the age, which is something we could expect.

## Methodology

[Notebook with EDA of the dataset](https://github.com/carcrupe/TFM/blob/master/notebooks_models/stroke_exploring_data.ipynb)</br>

I will describe briefly the different steps taken in the notebook. For further and detailed explanation, please refer to the [notebook](https://github.com/carcrupe/TFM/blob/master/notebooks_models/stroke_exploring_data.ipynb)</br>

### 1. Prepare the notebook with the data and requirements

To provide an easy-to-use notebook, the first cells are to download the appropriate data and install the necessary libraries. You can run the notebook without any other file.

### 2. Data cleaning 

In this section,the first thing is to assess null values and duplicates. Since there are not many I decided to delete these observations, lossing only 5% of the data. 

Moreover, for the continuous features, I have evaluated the outliers. To do that I have written a function that measures the amount of outliers for a given feature and calculates Q1, Q3 and the IQR (inter quartile range Q3-Q1). Based on these three parameters I decided to discard, for each feature, all the observations below (Q1 - 1.5 x IQR) and above (Q3 + 1.5 x IQR). For further information about this refer to [the IQR definition and outlier detection](https://en.wikipedia.org/wiki/Interquartile_range)

### 3. Feature extraction

Now that the data are clean and without outliers, in order to improve the insights I have created two new features, BMI (Body Mass Index) and Pulse (derived from the pressures). The idea of the feature extraction is to obtain new valuable data to improve our model.

### 4. Feature selection

If you have more features in the data, it does not necessarily mean your data is better and your model will have better performance. It is time to evaluate each feature and do the feature selection for the modeling. For that purpose, I run the correlation between all independant features and the target. 

To be more precise, having irrelevant features in data can decrease the accuracy of the model and make the model learn based on unrelated aspects. High correlation within independent features means that they represent the same thing and when you drop one of them, you do not lose much quality data.

Taking into account this previous explanation my goal is to select features with good correlation with the target and low correlation with any other independent feature.

Eventually, based on the correlation matrix, the [selected features](https://github.com/carcrupe/TFM/blob/master/data/stroke_data_for_modeling.csv) for my model are: Age, SystolicPressure, DiastolicPressure, Cholesterol, Pulse.

### 5. Machine Learning classifier

[Notebook with Machine Learning models](https://github.com/carcrupe/TFM/blob/master/notebooks_models/stroke_predictor_models.ipynb)</br>

Since my goal is to predict a binary output (having or not having a stroke), I will be training a few classification models with the selected features. Again, this notebook can be run without any other file or data, all is ready to be installed and downloaded at the begining of the notebook.

Before starting with the modeling, I will define a metric to evaluate the performance of the classifier. Since I do not want any patient potentially suffering from stroke to be misdiagnosed, I need to minimize the amout of false negatives. Therefore, the metric I chose to evaluate my model is the recall. The higher the recall, the lower the false negatives and thus, more patients will be diagnosed for further evaluation.

The steps I followed for training and evaluating each model are: 

1. Divide the data in train and test sets, setting the test 20% of the data.
2. Define the model with default hyperparameters and fit the training set.
3. Predict with the trained model and see recall performance to have a first overview.
4. Improve model performance manually, using GridSearch or Randomized search.
5. Fit the model with the optimized hyperparameters and evaluate again for recall.
6. Plot the confusion matrix and classifiation report to better evaluate model performance.
7. Use cross validation with recall as score. Calculate the mean of all cross-validated runs and store it as model performance metric.
8. Finally, select the model with the highest recall and performance. In my case it is the Random Forest model.

## Summary of main results

The most important features to predict a heart stroke are age and systolic pressure. Optimizing the model I have accomplished a recall of around 69%. Despite the fact that the model has been optimized, I have not improved much the performance. This might be the result of poor data quality or simply not enough data to make the model learn properly. Obtaining clinical data is very complicated and unfortunately, I did not have a better dataset to do my research.

## Conclusions

I have worked to solve a really relevant problem, which nowadays causes the biggest amount of deaths worldwide. Detecting a stroke in advance is obviously not an easy task and it has been in research for many years. With my work, I have learnt how important is to have valuable data to answer a given question. In particular, in this complex problem, I should have included much more information about the patients. This information is very sensitive and private, and therefore, it was very hard for me to obtain the right data. However, for those who have access to cardiovascular databases, I would recommend to include parameters such as sleep time, left/right atrial size, left/right ventricle size, kidney diseases, aorta ejection rate or percetange of oxygenated blood.  With all these parameters in mind, I am sure predictions would be much more accurate, providing precise results and hopefully, providing a tool to get to know your own heart at any time. Again, the challenge here remains in acquiring the right data to do the research.

## Run and use the web app

To finalize the project, I have created a simple web application with Streamlit. The application runs the best trained classifier (Random Forest) and predicts the input that the user sets. There are two ways to run the app:

**Docker File:** I have created a container with all the needed information to install and run the application. The instructions to execute the app are:

- Build the docker image: *sudo docker build -f Dockerfile -t stroke_app .*
- Run the image: *sudo docker run stroke_app*

*To do this it is assumed you have docker installed in your computer.*

**Streamlit notebook:** From the repository notebook folder download and run the file [stroke_stream.ipynb](https://github.com/carcrupe/TFM/blob/master/notebooks_models/stroke_stream.ipynb). You can run this notebook without previously training the model, it will by default use the pretrained model that I have saved in my repository. To show the app, I create a ngrok tunnel to expose my local server in a dinamically created URL.


