# Predicting Heart Disease using Machine Learning
This notebook looks into using various Python based Machine Learning and Data Science libraries in an attempt to build a machine learning model capable of predicting if or not someone has heart disease based on their medical attributes.

We are going to take the following approach:
1. Problem Definition
2. Data
3. Features
4. Modelling
5. Experimentation

## 1. Problem Definition
In the statement
> Given clinical parameters about a patient, can we predict whether or not they have heart disease?

## 2. Data
The original data came from the UCI Machine Learning Repositoty. (https://archive.ics.uci.edu/dataset/45/heart+disease)

There is also a version of it available on Kaggle. (https://www.kaggle.com/datasets/sumaiyatasmeem/heart-disease-classification-dataset)

## 3. Evaluation
> If we can reach 90% accuracy at predicting whether or not a patient has heart disease during the proof of concept, we'll pursue the project.

## 4. Features
Different information about each of the features in the data.
#### Create data dictionary
* ##### Age:
  Displays the age of the individual.
* ##### Sex:
  1 = male 0 = female
* #####  CP:
   0 = typical angina 1 = atypical angina 2 = non — anginal pain 3 = asymptotic
* ##### Trestbps:
  Displays the resting blood pressure value of an individual in mmHg (unit). anything above 130-140 is typically cause for concern.
* ##### Cho: Serum Cholestrol:
  Displays the serum cholesterol in mg/dl (unit)
* ##### FBS- Fasting Blood Sugar:
  If fasting blood sugar > 120mg/dl then : 1 (true) else : 0 (false) '>126' mg/dL signals diabetes
* ##### Restecg- Resting ECG:
  Displays resting electrocardiographic results 0 = normal 1 = having ST-T wave abnormality 2 = left ventricular hyperthrophy
* ##### Thalach- Max heart rate achieved:
  Displays the max heart rate achieved by an individual.
* ##### Exang- Exercise induced angina:
  1 = yes 0 = no
* ##### Oldpeak- ST depression induced by exercise relative to rest:
  Displays the value which is an integer or float.
* ##### Slope- Slope of the peak exercise ST segment:
  0 = upsloping: better heart rate with excercise (uncommon) 1 = flat: minimal change (typical healthy heart) 2 = downsloping: signs of unhealthy heart
* ##### CA- Number of major vessels (0–3) colored by flourosopy:
  Displays the value as integer or float.
* ##### Thal - Displays the thalassemia:
  1,3 = normal 6 = fixed defect 7 = reversible defect: no proper blood movement when excercising
* ##### Target - Displays whether the individual is suffering from heart disease or not:
  1 = yes 0 = no
