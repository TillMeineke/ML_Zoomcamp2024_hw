# Evaluate Projects for "Capstone 1"

## Project 1 - Evaluation: Peaceful Herschel's Submission

GitHub Link: <https://github.com/tomojpin1234/machine-learning-zoomcamp-2024-capstone-1>
Commit Hash: 27ce032
I evaluated the submission according to the following criteria:

1. Problem description
   - [x] Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used (2 points)
2. EDA
   - [x] Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis). For images: analyzing the content of the images. For texts: frequent words, word clouds, etc. (2 points)
     - Calculate correlation between the TF-IDF features and upvote_count -> plot not readeable
3. Model training
   - [x] Trained multiple models and tuned their parameters. For neural networks: same as previous, but also with tuning: adjusting learning rate, dropout rate, size of the inner layer, etc. (3 points)
     - surpress warnings
4. Exporting notebook to script
   - [x] The logic for training the model is exported to a separate script (1 point)
5. Reproducibility
   - [x] It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data (1 point)
6. Model deployment
   - [x] Model is deployed (with Flask, BentoML or a similar framework) (1 point)
7. Dependency and environment management
   - [x] Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to activate the env (2 points)
8. Containerization
   - [x] The application is containerized and the README describes how to build a container and how to run it (2 points)
9. Cloud deployment
   - [x] ~~There's code for deployment to cloud or Kubernetes cluster (local or remote).~~ There's a URL for testing - or video/screenshot of testing it (2 points)

Comment:

- Calculate correlation between the TF-IDF features and upvote_count -> plot not readable
- surpress warnings -> they clutter the notebook
- more explanation why you did what would be nice
- word clouds would be nice as visualisation
- There's no code for deployment to cloud or Kubernetes cluster

nice project 👍🏼

- [x] Learning in public 1: Evaluation Review [LinkedIn](https://www.linkedin.com/posts/tillmeineke_mlzoomcamp-activity-7285976421116637184-hFMv?utm_source=share&utm_medium=member_desktop) on 17 January 2025
- [x] Learning in public 2: General learnings from evaluation [LinkedIn](https://www.linkedin.com/posts/tillmeineke_mlzoomcamp-learninginpublic-datascience-activity-7285987756806131712-ecnk?utm_source=share&utm_medium=member_desktop) on 17 January 2025

## Project 2 - Evaluation: Elated Nash's Submission

GitHub Link: <https://github.com/marvik/ml_zoomcamp_capstone_1>
Commit Hash: cd717a5
I evaluated the submission according to the following criteria:

1. Problem description
   - [x] Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used (2 points)
2. EDA
   - [x] Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis). For images: analyzing the content of the images. For texts: frequent words, word clouds, etc. (2 points)
3. Model training
   - [x] Trained multiple models and tuned their parameters. For neural networks: same as previous, but also with tuning: adjusting learning rate, dropout rate, size of the inner layer, etc. (3 points)
4. Exporting notebook to script
   - [x] The logic for training the model is exported to a separate script (1 point)
5. Reproducibilityaccessible (0 points)
   - [x] It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data (1 point)
6. Model deployment
   - [x] Model is deployed (with Flask, BentoML or a similar framework) (1 point)
7. Dependency and environment management
   - [x] Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to activate the env (2 points)
8. Containerization
   - [x] The application is containerized and the README describes how to build a container and how to run it (2 points)
9. Cloud deployment
   - [x] There's code for deployment to cloud or Kubernetes cluster (local or remote). There's a URL for testing - or video/screenshot of testing it (2 points)

Comment:

Nice and clear project 👍

Deployment not running anymore?

```plaintext
Error: Connection to the server at <https://online-shopper-prediction-558797510368.us-central1.run.app/predict> timed out.
Details: HTTPSConnectionPool(host='online-shopper-prediction-558797510368.us-central1.run.app', port=443): Read timed out. (read timeout=10)
```

```bash
ping <https://online-shopper-prediction-558797510368.us-central1.run.app/predict>
ping: cannot resolve <https://online-shopper-prediction-558797510368.us-central1.run.app/predict>: Unknown host
```

- [x] Learning in public 1: Evaluation Review [LinkedIn](https://www.linkedin.com/posts/tillmeineke_mlzoomcamp-activity-7285978850105192450-AoNS?utm_source=share&utm_medium=member_desktop) on 17 January 2025
- [x] Learning in public 2: Coding fail [LinkedIn](https://www.linkedin.com/posts/tillmeineke_datascience-machinelearning-pylabel-activity-7285989292449878016-NBBj?utm_source=share&utm_medium=member_desktop) on 17 January 2025

## Project 3 - Evaluation: Brava Man's Submission
GitHub Link: <https://github.com/Wali-Mohamed/used_car_price_prediction>
Commit Hash: eb2fbe4
I evaluated the submission according to the following criteria:

1. Problem description
   - [x] Problem is described in README with enough context, so it's clear what the problem is and how the solution will be used (2 points)
2. EDA
   - [x] Extensive EDA (ranges of values, missing values, analysis of target variable, feature importance analysis). For images: analyzing the content of the images. For texts: frequent words, word clouds, etc. (2 points)
     - EDA is done, but it's not clear what the insights are
     - Some explanation in notebook would be nice.
     - some plot labels not readable
3. Model training
   - [x] Trained multiple models and tuned their parameters. For neural networks: same as previous, but also with tuning: adjusting learning rate, dropout rate, size of the inner layer, etc. (3 points)
      - C:\Users\user\.virtualenvs\10-kubernetes-taEED_rI\Lib\site-packages\sklearn\preprocessing\_encoders.py:246: UserWarning: Found unknown categories in columns [0, 1] during transform. These unknown categories will be encoded as all zeros
4. Exporting notebook to script
   - [x] The logic for training the model is exported to a separate script (1 point)
5. Reproducibilityaccessible (0 points)
   - [x] It's possible to re-execute the notebook and the training script without errors. The dataset is committed in the project repository or there are clear instructions on how to download the data (1 point)
6. Model deployment
   - [x] Model is deployed (with Flask, BentoML or a similar framework) (1 point)
7. Dependency and environment management
   - [x] Provided a file with dependencies and used virtual environment. README says how to install the dependencies and how to activate the env (2 points)
     - typo: pip install -r requirements.t**e**xt
8. Containerization
   - [x] The application is containerized and the README describes how to build a container and how to run it (2 points)
9. Cloud deployment
   - [x] There's code for deployment to cloud or Kubernetes cluster (local or remote). There's a URL for testing - or video/screenshot of testing it (2 points)

Comment:
nice project 👍
- EDA is done, but it's not clear what the insights are
- Some explanation in notebook would be nice.
- some plot labels not readable
- C:\Users\user\.virtualenvs\10-kubernetes-taEED_rI\Lib\site-packages\sklearn\preprocessing\_encoders.py:246: UserWarning: Found unknown categories in columns [0, 1] during transform. These unknown categories will be encoded as all zeros
- typo: pip install -r requirements.t**e**xt
- just a link to an ip address with a nice web app, but no code for cloud deployment

- [x] Learning in public 1: Review [LinkeIn](https://www.linkedin.com/posts/tillmeineke_mlzoomcamp-activity-7285981649710813184-Z2hb?utm_source=share&utm_medium=member_desktop) on 17 January 2025
- [x] Learning in public 2: Insights from Peer Project Reviews [LinkedIn](https://www.linkedin.com/posts/tillmeineke_mlzoomcamp-machinelearning-activity-7287394676809068545-4W0s?utm_source=share&utm_medium=member_desktop)
