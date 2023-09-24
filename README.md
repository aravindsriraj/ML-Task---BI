# Machine Learning Assignment

## Connecting to Database and Extracting tables

- Connected to a PostgreSQL database. I retrieved data from three specific tables named "loan_outcomes," "user_gps_fixes," and "user_attributes." After fetching the data, I stored it in pandas DataFrames.

### Understanding the data

**Loan Outcomes Data:**

This data appears to have three columns: user_id, application_at, and loan_outcome. It provides information about when users applied for loans and whether the outcome was "defaulted" or "repaid."

**User GPS Fixes Data:**

This dataset contains information related to GPS fixes, including columns such as id, gps_fix_at, server_upload_at, longitude, latitude, accuracy, altitude, bearing, location_provider, and user_id. It appears to capture GPS coordinates, accuracy, and other attributes associated with user locations.

**User Attributes Data:**

This dataset includes columns such as user_id, age, and cash_incoming_30days. It seems to contain information about users, including their ages and cash incoming in the last 30 days.

**Information of the Datasets:**

- For "Loan Outcomes," there are 400 rows with columns user_id, application_at, and loan_outcome.

- For "User GPS Fixes," there are 26,710 rows with various columns including timestamps and geographical information.

- For "User Attributes," there are 400 rows with columns user_id, age, and cash_incoming_30days.

**Checking Missing Values:**

- In all three datasets, there are no missing values, as indicated by the count of zeros for each column.

## Exploratory Data Analysis

**Loan Outcomes Over Time:**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/1c7731d4-7376-42cb-988d-cc6a9d4bcef6)


**Loan Outcomes by User Age:**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/e17f08a5-0977-47c9-bf28-5d4886d300e9)


**Loan Outcomes by Age Group:**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/03b2244c-be3f-496f-960e-7b8dcf6f7399)



**Locations of GPS Fixes:**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/3b4f2b66-3356-4b58-bc22-aeea2956e0ee)


**Distribution of location providers**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/8d5647b7-455c-455d-8420-f63365b0bfa6)


**Age Distribution of Borrowers:**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/e2357a49-dc13-4c42-aa19-16967ce6e177)


**User Segmentation by Age and Cash Incoming**
![image](https://github.com/aravindsriraj/ML-Task---BI/assets/60252521/c1fc8e8b-b430-4211-b893-3b85c03090c9)

## Model Building and Evaluation

I started with a dataset combining loan outcomes and user attributes, dropping unnecessary columns. Then, I encoded the loan outcomes and split the data into training and testing sets. I trained and evaluated four models:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost.

XGBoost performed the best, so I trained it on the full dataset and saved it as 'xgb_model.pkl' for future use in a Streamlit application.




