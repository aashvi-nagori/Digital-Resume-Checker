# Fake News Detection Using Machine Learning
## Overview

Fake news spreads quickly on social media and online platforms, misleading people and causing confusion. This project uses Natural language processing (NLP) and machine learning classification algorithms for detecting whether a news article is real or fake automatically. 
The system can help users identify trustworthy news efficiently.
## Features
 - It classify if the news article is Real or Fake automatically
 - Text preprocessing: lowercasing, stopword removal, stemming
 - TF-IDF vectorization of news text
 - Machine Learning models: Logistic Regression, Naive Bayes
 - Displays prediction results clearly (Real/Fake)
## Technologies / Tools Used
 - Python 3
 - Google Colab / Jupyter Notebook
 - Pandas, Numpy
 - scikit-learn
 - NLTK (Natural Language Toolkit)
 - Matplotlib / Seaborn (for visualization)
## Steps to Install & Run the Project
 1. Clone the repository:
    git clone
    https://github.com/aashvi-nagori/Fake-News-Detection.git
 2. Open the project in Google Colab or Jupyter Notebook
 3. Make sure the following libraries are installed:
    pip install pandas numpy
    scikit-learn nltk matplotlib seaborn
 4. Open the notebook 'FakeNewsDetection.ipynb'.
 5. Run each cell step by step to:
 - Load the dataset
 - Preprocess the text
 - Train the model
 - Test predictions
## Instructions for testing
 1. The project contains a test dataset ('test.csv') to check model performance.
 2. Users can also input custom news text in the notebook.
 3. After running the notebook, the model predicts whether the input news is Real or Fake.
 4. The notebook also displays accuracy, confusion matrix, and other evaluation matrices.
## Screenshots
   The screenshots of the codes are as follows:
     
<img width="1340" height="386" alt="Installing libraries" src="https://github.com/user-attachments/assets/91c89fc9-eb80-4c2c-8b85-74692ba49761" />
<img width="980" height="211" alt="Importing libraries" src="https://github.com/user-attachments/assets/5da646cf-6d06-4a4c-82cc-cbad6ae5f127" />
<img width="1282" height="835" alt="news csv xlsx" src="https://github.com/user-attachments/assets/12f1e611-d789-40f7-bcb4-6ab624eb5236" />
<img width="853" height="410" alt="Checking data" src="https://github.com/user-attachments/assets/035e54b2-e2c8-40f1-a37e-a22aa30229e9" />
<img width="1012" height="342" alt="split" src="https://github.com/user-attachments/assets/e53bb5e5-32f5-4526-9556-9c9cc9033844" />
<img width="767" height="507" alt="Converting to numbers" src="https://github.com/user-attachments/assets/141e3558-1259-410d-a04f-caf50bf72d84" />
<img width="1072" height="306" alt="Model training" src="https://github.com/user-attachments/assets/d2de7049-4a73-4424-900f-ac19c8f7d2b1" />
<img width="715" height="208" alt="Predict and accuracy" src="https://github.com/user-attachments/assets/586bd0b7-fa30-4314-9989-7f22b79644f1" />
<img width="1783" height="582" alt="Report output1" src="https://github.com/user-attachments/assets/6f0d0ed2-1fe8-4e7b-9313-25f61b206c30" />
<img width="1746" height="578" alt="Report output2" src="https://github.com/user-attachments/assets/36e933db-5263-4df5-9919-46ab561c5fee" />
