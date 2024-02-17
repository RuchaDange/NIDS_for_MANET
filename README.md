Network Intrusion Detection System for MANETs
This project aims to develop a Network Intrusion Detection System (NIDS) specifically tailored for Mobile Ad-Hoc Networks (MANETs). MANETs present unique challenges due to their dynamic nature and resource constraints, making traditional intrusion detection techniques less effective.

Table of Contents
Overview
Exploratory Data Analysis (EDA)
Machine Learning Models
Live Streaming Prediction

Overview
In this project, we perform comprehensive Exploratory Data Analysis (EDA) to gain insights into the characteristics of the data collected from MANETs. Subsequently, various machine learning models are trained using this data to detect network intrusions.

Exploratory Data Analysis (EDA)
The EDA phase involves analyzing the dataset collected from MANETs to understand its structure, patterns, and anomalies. This step is crucial for feature selection, preprocessing, and identifying potential issues in the data.

Machine Learning Models
We have trained several machine learning models on the processed data to identify network intrusions. The models include:

Logistic Regression
Multinomial Naive Bayes
K-Nearest Neighbors (KNN)
Gradient Boosting
Random Forest
Decision Tree
AdaBoost
XGBoost
Support Vector Machine (SVM)
TensorFlow (Deep Learning)
Each model is evaluated based on its accuracy on unseen data to determine its effectiveness in detecting network intrusions in MANETs.

Live Streaming Prediction
A live streaming prediction system has been implemented using RabbitMQ for message queuing and Streamlit for visualization. The K-Nearest Neighbors (KNN) model is used for real-time prediction of network intrusions as the data streams in.
