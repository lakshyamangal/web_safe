# Malicious-website-detection


## Abstract

Malicious websites are created to obtain sensitive information or data, such as usernames, passwords and credit card details or other sensitive details, by impersonating oneself as a trustworthy entity in a digital communication. Such attacks are the simplest way to obtain sensitive information from innocent users. Aim of the phishers is to acquire critical information like username, password and bank account details. Cyber security persons are now looking for trustworthy and steady detection techniques for such website detection. The aim of this research is to develop these methods of defence utilizing various approaches to categorize websites. Our aim is for general people to understand our project and for that we are creating a report for every input explaining why that particular website is malicious or safe. Some of our results from the model will also be present in the report. The complete project will be hosted on a  hosted on cloud with a simple GUI for easy user access.


## Introduction

There are many websites which are typical starting points of online social engineering attacks, including many recent online scams. The attackers develop web pages mimicking legitimate websites, and send the malicious URLs to victims to lure them to input their sensitive information. In this project we aim to develop a system which can help tract such websites. Our project deals with detecting malicious websites which can attack users in various forms such as spam, phishing, data stealing,etc. The following web-based application will be hosted on Amazon cloud and will be further protected using cloud services. 

## Problem Statement

Developing a cloud-hosted security system which can detect and save users from cyber attacks such as identity theft,malware attack, fake websites,etc.

## Dataset
The presented dataset was collected and prepared for the purpose of building and evaluating various classification methods for the task of detecting phishing websites based on the uniform resource locator (URL) properties, URL resolving metrics, and external services. 
The dataset has been taken from https://www.sciencedirect.com/science/article/pii/S2352340920313202 
The attributes of the prepared dataset can be divided into six groups.For this project we need to find few details before we can proceed to our model. They are:
Address Bar based Features
Domain based Features
HTML & JavaScript based Features
 
These data consist of a collection of legitimate, as well as phishing website instances. Each website is represented by the set of features that denote whether the website is legitimate or not. Data can serve as input for the machine learning process.

## Solution Approach

We have used Random Forest just to get the idea of the features importance and then created Xgboost from scratch as our Ensemble Learning techniques . Further have generated a report which is a pdf therefore can be downloaded by the client describing why that particular decision was made. We have researched on how to select and extract the above mentioned features with the help of few research papers.  Finally the server is hosted on Amazon Ec2(Ubuntu Server 20.04 LTS) for public use. We have developed a basic GUI to accompany the app. The frontend uses HTML,CSS ,JavaScript and the back-end is made of python. Python code and the frontend interact using flask. All the requirements needed for the app are mentioned in the requirement.txt file. The following block diagram will demonstrate our approach to the presented problem





Gradient Boosting Machines fit into a category of machine learning are called  Ensemble Learning, which is a branch of machine learning  methods that train and predict with many models at once to produce a single superior output. XGBoost is a scalable and accurate implementation of gradient boosting machines and it has proven to push the limits of computing power for boosted trees algorithms as it was built and developed for the sole purpose of model performance and computational speed. Specifically, it was engineered to exploit every bit of memory and hardware resources for tree boosting algorithms. 
Our model uses XGBoost to classify the result. For every feature we assemble a weak learner that is we assign whether the URL is malicious (1) or safe (0). This method is called Ensemble method as now we have many weak learners to develop the model.

## Report Creation
For the output we generate a report which gives detailed analysis of the URL. It describes various attributes of the URL and presents a graph through which users can compare how good or bad is the website. The final result (Malicious or safe) is also present on the website. The purpose of this report is for clients to understand how such features contribute to creation of such websites.


## Conclusion

With this research based application we hope that people will understand more about such websites and save themself from potential cyber activities which can lead to loss of personal information, malware infection, etc.


