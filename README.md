# Homework repository for [ML_Zoomcamp 2024](https://github.com/DataTalksClub/machine-learning-zoomcamp)

Sep 2024 - Jan 2025
[Course management platform](https://courses.datatalks.club/ml-zoomcamp-2024/)

This folder contains the homework for the course. Each week has its own folder. The homework is in the form of Jupyter notebooks.

I also keep track of my progress in this `README.md` file. I will update it every week.

## [Homework 1: Introduction to Machine Learning](./01-intro/homework_01_till_meineke.ipynb) due 1 Oktober 2024 01:00

Extra material in subfolder contains the setup of the environment, the portfolio page, and other things I learned during the first week of course.

- [x] [Set up the environment](./01-intro/Setup_environment.md)
  - [x] locally on Mac
  - [x] on AWS
  - [ ] on GCP
  - [ ] on Azure
  - [x] Kaggle
  - [x] Colab
- [x] Finished the homework
  - [x] Q1. Pandas version
  - [x] Getting data
  - [x] Q2. Records count
  - [x] Q3. Laptop brands
  - [x] Q4. Missing values
  - [x] Q5. Maximum final price
  - [x] Q6. Median value of Screen
  - [x] Q7. Sum of weights
- [x] Learn in public 1: Setting up [Portfolio homepage](till.meineke.github.io) published on 23.09 [medium](https://medium.com/@till.meineke/how-to-setup-a-portfolio-page-on-github-io-3b951fc94f22)
- [x] Learn in public 2: Setting up the environments - medium article published on 26.09 [medium](https://medium.com/@till.meineke/setting-up-the-environments-for-ml-zoomcamp-2024-eceb6e42e36e)
- [x] Learn in public 3: Setting up the environments - LinkedIn post published on 26.09 [LinkedIn](https://www.linkedin.com/posts/tillmeineke_setting-up-the-environments-for-ml-zoomcamp-activity-7244840475675807745-ExVD?utm_source=share&utm_medium=member_desktop)
- [x] Learn in public 4: weekly learning published on 30.09 [LinkedIn](https://www.linkedin.com/pulse/learning-ml-zoomcamp-week-1-introduction-till-meineke-k05mc)
<!-- - [ ] Learn in public 5: Setup macBook
- [ ] Learn in public 6: Setup iTerm2
- [ ] Learn in public 7: Setup VSCode
- [ ] Learn in public 8: Organize the homework repository
- [ ] Learn in public 9: `.dotfiles`? -->

## [Homework 2: Machine Learning for regression](./02-regression/homework_02_till_meineke.ipynb) due 8 Oktober 2024 01:00

- [x] Finished the homework
- [ ] Learn in public 1:
- [ ] Learn in public 2: [California housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) - predict the price of a house
- [ ] Learn in public 3: [Student Performance Data Set](https://archive.ics.uci.edu/dataset/320/student+performance)
- [ ] Learn in public 4: [UCI ML datasets](https://archive.ics.uci.edu/datasets)
- [ ] Learn in public 5: Default prediction - <https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients>
- [ ] Learn in public 6:
- [ ] Learn in public 7:

## [Homework 3: Machine Learning for Classification](./03-classification/homework_03_till_meineke.ipynb) due 15 Oktober 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1: exclude least useful features
- [ ] Learn in public 2: scikit-learn in project of last week
- [ ] Learn in public 3: use `LinearRegression` (not regularized) and `RidgeRegression` (regularized)
- [ ] Learn in public 4: Find the best regularization parameter for Ridge
- [ ] Learn in public 5: using the `OneHotEncoding` class
- [ ] Learn in public 6: [Lead scoring](https://www.kaggle.com/ashydv/leads-dataset)
- [ ] Learn in public 7: [Default prediction](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)

## [Homework 4: Evaluation Metrics for Classification]() due 22 Oktober 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1: Check the precision and recall of the dummy classifier that always predict "FALSE"
- [ ] Learn in public 2: F1 score = 2 P R / (P + R)
- [ ] Learn in public 3: Evaluate precision and recall at different thresholds, plot P vs R - this way you'll get the precision/recall curve (similar to ROC curve)
- [ ] Learn in public 4: Area under the PR curve is also a useful metric
- [ ] Learn in public 5: Calculate the metrics for the suggested datasets from the previous week
- [ ] Learn in public 6:
- [ ] Learn in public 7:

## [Homework 5: Deploying Machine Learning Models]() due 29 Oktober 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1:
- [ ] Learn in public 2:
- [ ] Learn in public 3:
- [ ] Learn in public 4:
- [ ] Learn in public 5:
- [ ] Learn in public 6:
- [ ] Learn in public 7:

## [Homework 6: Decision Trees and Ensemble Learning]() due 5 November 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1: do EDA or feature engineering for this dataset to get more insights into the problem
- [ ] Learn in public 2: For random forest, there are more parameters that we can tune. Check max_features and bootstrap.
- [ ] Learn in public 3: Try ExtraTreesClassifier
- [ ] Learn in public 4: Check if not filling NA's help improve performance (XGBoost).
- [ ] Learn in public 5: Experiment with other XGBoost parameters: subsample and colsample_bytree.
- [ ] Learn in public 6: When selecting the best split, decision trees find the most useful features. This information can be used for understanding which features are more important than others. See example here (?) for random forest (it's the same for plain decision trees) and for xgboost
- [ ] Learn in public 7: using trees solving regression problems: check DecisionTreeRegressor, RandomForestRegressor and the objective=reg:squarederror parameter for XGBoost

## [Homework 8: Neural Networks and Deep Learning]() due 3 December 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1: Add more data, e.g, Zalando etc
- [ ] Learn in public 2: Albumentations - another way of generating augmentations
- [ ] Learn in public 3: Use PyTorch or MXNet instead of TensorFlow/Keras
- [ ] Learn in public 4: In addition to Xception, there are others architectures - try them
- [ ] Learn in public 5: Project: cats vs dogs
- [ ] Learn in public 6: Project: Hotdog vs not hotdog
- [ ] Learn in public 7: Project: Category of images

## [Homework 9: Serverless Deep Learning]() due 10 December 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1: Try similar serverless services from Google Cloud and Microsoft Azure
- [ ] Learn in public 2: Deploy cats vs dogs and other Keras models with AWS Lambda
- [ ] Learn in public 3: AWS Lambda is also good for other libraries, not just Tensorflow. You can deploy Scikit-Learn and XGBoost models with it as well
- [ ] Learn in public 4:
- [ ] Learn in public 5:
- [ ] Learn in public 6:
- [ ] Learn in public 7:

## [Homework 10: Kubernetes and TensorFlow Serving]() due 17 December 2024 01:00

- [ ] Finished the homework
- [ ] Learn in public 1: Other local Kubernetes: minikube, k3d, k3s, microk8s, EKS Anywhere
- [ ] Learn in public 2: [Rancher desktop](https://rancherdesktop.io/)
- [ ] Learn in public 3: [Docker desktop](https://www.docker.com/products/docker-desktop/)
- [ ] Learn in public 4: [Lens](https://k8slens.dev/)
- [ ] Learn in public 5: Many cloud providers have Kubernetes: GCP, Azure, Digital ocean and others. Look for "Managed Kubernetes" in your favourite search engine
- [ ] Learn in public 6: Deploy the model from previous modules and from your project with Kubernetes
- [ ] Learn in public 7: Learn about Kubernetes namespaces. Here we used the default namespace

# Projects

## [ ] Midterm Project: due 26 November 2024 00:00
## [ ] Capstone 1 Project: due 7 January 2025 00:00
## [ ] Capstone 2 Project: due 28 January 2025 00:00