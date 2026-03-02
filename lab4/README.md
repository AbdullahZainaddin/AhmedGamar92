# Lab 4 - Data Quality Assessment & Preprocessing

## Student Information
Name: Abdullah Zainaddin  
Course: Machine learning
Lab: 4  

---

## Objective
The objective of this lab is to perform Data Quality Assessment and Data Preprocessing on the Titanic dataset (test.csv).

---

## Dataset Information
- Number of rows: 418
- Number of columns: 11
- Dataset file: test.csv

---

## Data Quality Assessment

### 1. Missing Values
- Age: 86 missing values
- Fare: 1 missing value
- Cabin: 327 missing values

### 2. Data Types
- Numerical: PassengerId, Pclass, Age, SibSp, Parch, Fare
- Categorical: Name, Sex, Ticket, Cabin, Embarked

---

## Data Preprocessing Steps

### 1. Handling Missing Values
- Filled Age with median value
- Filled Fare with median value
- Created new feature "HasCabin"
- Dropped Cabin column

### 2. Feature Engineering
- Created FamilySize = SibSp + Parch + 1
- Created IsAlone feature

### 3. Encoding
- Applied one-hot encoding to:
  - Sex
  - Embarked

### 4. Dropped Columns
- PassengerId
- Name
- Ticket

---

## Final Result
- Dataset cleaned
- No missing values
- Ready for machine learning models
