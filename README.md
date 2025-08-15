# 🚗 United States Accident Severity Forecasting

> **Predicting road accident severity using big data & cloud computing**  
> Leveraging AWS (S3, Glue, SageMaker) and machine learning models to transform large-scale accident data into actionable road safety insights.

---

## 📌 Table of Contents
1. [Introduction](#introduction)
2. [Project Workflow](#project-workflow)
3. [Dataset](#dataset)
4. [Data Processing](#data-processing)
5. [Modeling Approach](#modeling-approach)
6. [Results](#results)
7. [Demo & Video](#demo--video)
8. [Future Enhancements](#future-enhancements)
9. [Contributors](#contributors)
---

## 📝 Introduction
Road traffic accidents cause over **1.3 million deaths annually** worldwide, along with massive socio-economic losses.  
Despite abundant data from sensors, APIs, and government agencies, accident prevention efforts are still mostly **reactive** rather than **predictive**.

This project — **United States Accident Severity Forecasting** — applies machine learning and cloud technologies to predict accident severity using **7.7 million+ records** from across **49 U.S. states (2016–2023)**.

The solution is **scalable, cloud-based**, and integrates seamlessly with visualization dashboards for real-time decision-making.

---

## 🔄 Project Workflow

1. **Raw Accident Data** → Collected from multiple sources (APIs, DOT feeds, law enforcement records, roadway sensors).  
2. **AWS S3 Upload** → Raw data stored securely in AWS S3 bucket.  
3. **AWS Glue Preprocessing** → Data cleaning, transformation, and ETL operations.  
4. **Feature Engineering** → Creation of temporal, spatial, weather-based, and encoded features.  
5. **Model Training on SageMaker** → Training predictive models (SARIMAX, Random Forest, XGBoost).  
6. **Evaluation & Forecasting** → Model performance evaluation and future severity prediction.  
7. **Interactive Dashboard** → Visualization of trends and predictions using QuickSight / Power BI.  

---
## 🛠 Tools & Services Used

- **AWS S3** → Cloud-based data storage for raw and processed accident data.  
- **AWS Glue** → ETL (Extract, Transform, Load) service used for preprocessing large datasets.  
- **AWS SageMaker** → Model training and deployment platform for scalable machine learning.  
- **Python** (Pandas, XGBoost, Statsmodels) → For feature engineering, statistical analysis, and modeling.  
- **QuickSight / Power BI** → Interactive dashboarding and visualization tools for insights delivery.  

---

## 📂 Dataset

- **Source:** U.S. Accident Dataset (compiled from multiple APIs, Department of Transportation feeds, law enforcement records, and roadway sensors).  
- **Size:** ~7.7 million records  
- **Period:** February 2016 – March 2023  
- **Coverage:** 49 U.S. states
- **Link:** https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents 

**Key Features:**
- **Start_Time, Start_Lat, Start_Lng** – Temporal and spatial accident coordinates  
- **Weather:** Temperature(F), Humidity(%), Visibility(mi), etc.  
- **Road:** Distance(mi), Traffic_Signal, Junction, and related road features  
- **Temporal:** Hour, DayOfWeek, Month, IsWeekend  
- **Target:** Severity (1 to 4) – Classification of accident seriousness  

---

## 🛠 Data Processing

### **Preprocessing Steps**
- Handling missing values and anomalies in the dataset  
- Standardizing timestamps and extracting temporal features  
- Encoding weather conditions and road-related categorical features  
- Normalizing spatial data (latitude/longitude)  
- One-hot encoding for categorical variables  

### **Generalization**
- **Time-based:** Weekend vs. weekday grouping  
- **Location-based:** Presence of traffic control signals and junctions  
- **Weather-based:** Grouping similar weather conditions for better modeling  
- **National trends:** Aggregating accident statistics per state/year for trend analysis



## 🤖 Modeling Approach

We experimented with **three models**:

| Model        | Purpose                   | Key Metric (RMSE) |
|--------------|---------------------------|-------------------|
| SARIMAX      | Time-series forecasting    | ~1020             |
| RandomForest | Baseline ML model          | ~845              |
| **XGBoost**  | Final chosen model         | **~796**          |

**Why XGBoost?**
- Handles mixed feature types well  
- Robust to missing values  
- Excellent performance on tabular data  

---

## 📊 Results

**Key Insights:**
- **Severity 2** accidents were the most frequent.  
- Weather conditions & traffic control presence had strong correlations with severity.  
- Temporal patterns: peak accident hours in morning & evening rush.  

**Example Visualization:**
### Home Tab
![Severity Distribution](https://github.com/cantor08/Traffic-Accident-Severity-Prediction-/blob/main/ScreenShot/Home%20Tab.png)

### Weather Mode tab
![Severity Distribution](https://github.com/cantor08/Traffic-Accident-Severity-Prediction-/blob/main/ScreenShot/Wheather%20Mode%20Tab.png)

## 🎥 Demo & Video

📌 **Video Demo:** [Watch on YouTube](https://youtu.be/3ujSNFvaCvs) 

---

## 🚀 Future Enhancements

- Deploy as a **real-time accident alert API**  
- Integrate with **live traffic feeds**  
- Add **deep learning models** (LSTM, Transformers)  
- Enable **multi-modal data fusion** (video, IoT sensor data)  

---

## 👥 Contributors

- **Maulik Raval**
- **Hemin Shah**
