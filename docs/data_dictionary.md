# 📊 Data Dictionary — OLA Rides Analysis  

---

## 📌 Dataset Summary  

| Item | Details |
|------|--------|
| **Dataset Name** | OLA Ride Booking Dataset |
| **Source** | Kaggle |
| **Raw File Name** | ola_dataset.csv |
| **Last Updated** | January 2024 |
| **Granularity** | One row per ride booking |

---

## 📋 Column Definitions  

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|------------|----------|------------|--------------|--------|--------------|
| **booking_id** | string | Unique identifier for each ride | BKG12345 | KPI, EDA | Ensured uniqueness, no nulls |
| **vehicle_type** | string | Type of vehicle booked | prime sedan | Segmentation, Tableau | Converted to lowercase, standardized |
| **pickup_location** | string | Area code of pickup location | area-34 | Location analysis | Normalized format |
| **booking_status** | string | Status of ride | success | KPI | Standardized categories |
| **ride_distance** | float | Distance of trip in km | 12.5 | EDA | Converted to numeric |
| **revenue** | float | Revenue earned per ride | 680 | KPI | Missing values handled |
| **customer_rating** | float | Rating given by customer (1–5) | 4.0 | CX analysis | Nulls excluded from averages |
| **driver_rating** | float | Rating given by driver (1–5) | 4.2 | CX analysis | Nulls excluded from averages |
| **date** | date | Booking date | 2024-01-15 | Trend analysis | Converted to datetime |
| **hour** | int | Hour of booking (0–23) | 14 | Time analysis | Extracted and cleaned |
| **cancel_reason** | string | Reason for cancellation | wrong address | EDA | Cleaned and grouped |
| **ctat** | float | Customer Time to Arrival (minutes) | 15.5 | KPI | Missing values handled |
| **vtat** | float | Vehicle Time to Arrival (minutes) | 14.2 | Ops analysis | Converted to numeric |

---

## ⚙️ Derived Columns  

| Derived Column | Logic | Business Meaning |
|---------------|------|----------------|
| **is_successful** | booking_status == "success" | Identifies completed rides |
| **cancel_flag** | booking_status contains "cancel" | Flags cancelled rides |
| **time_of_day** | Derived from hour buckets | Enables time-based analysis |
| **revenue_lost** | Avg revenue for cancelled rides | Estimates opportunity loss |
| **completion_rate** | successful / total rides | Measures operational efficiency |
| **cancellation_rate** | cancelled / total rides | Core business problem metric |

---

## ⚠️ Data Quality Notes  

- Dataset covers **only January 2024** → no seasonal variation  
- Pickup locations are **anonymized (Area-1 to Area-50)**  
- Ratings missing for cancelled rides  
- Revenue for cancelled rides is **estimated using average fare**  
- No driver/customer IDs available  
- Some categorical values were inconsistent and standardized  

---

## 🛠 Tools Used  

- **Python (pandas, numpy)** for cleaning and transformation  
- **Jupyter Notebook** for analysis  
- **Tableau Public** for visualization  
