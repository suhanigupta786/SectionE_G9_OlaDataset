📊 Data Dictionary — OLA Rides Analysis
📌 Dataset Summary
Item	Details
Dataset Name	OLA Ride Booking Dataset
Source	Kaggle
Raw File Name	ola_dataset.csv
Last Updated	January 2024
Granularity	One row per ride booking
🧩 Data Schema (High-Level)
Diagram
flowchart LR

A[Booking_ID] --> B[Ride Details]
B --> C[Vehicle_Type]
B --> D[Pickup_Location]
B --> E[Ride_Distance]

A --> F[Time Data]
F --> G[Date]
F --> H[Hour]
F --> I[Time_of_Day]

A --> J[Status & Outcome]
J --> K[Booking_Status]
J --> L[Cancel_Reason]
J --> M[Is_Successful]

A --> N[Financials]
N --> O[Revenue]
N --> P[Revenue_Lost]

A --> Q[Experience Metrics]
Q --> R[Customer_Rating]
Q --> S[Driver_Rating]
Q --> T[CTAT]
Q --> U[VTAT]

🗂 Column Grouping
📊 Business Metrics
booking_id
booking_status
is_successful
cancel_flag
cancellation_rate
completion_rate
💰 Financial Metrics
revenue
revenue_lost
⚙️ Operational Metrics
vehicle_type
pickup_location
ride_distance
hour
time_of_day
ctat
vtat
😊 Customer Experience Metrics
customer_rating
driver_rating
cancel_reason
📋 Column Definitions
Column Name	Data Type	Description	Example Value	Used In	Cleaning Notes
booking_id	string	Unique identifier for each ride	BKG12345	KPI, EDA	Ensured uniqueness
vehicle_type	string	Type of vehicle booked	prime sedan	Segmentation	Standardized to lowercase
pickup_location	string	Area code of pickup	area-34	Location analysis	Normalized
booking_status	string	Ride outcome	success	KPI	Cleaned categories
ride_distance	float	Trip distance (km)	12.5	EDA	Converted to numeric
revenue	float	Revenue per ride	680	Financial KPI	Missing handled
customer_rating	float	Rating by customer	4.0	CX analysis	Nulls excluded
driver_rating	float	Rating by driver	4.2	CX analysis	Nulls excluded
date	date	Booking date	2024-01-15	Trends	Converted to datetime
hour	int	Hour of booking	14	Time analysis	Extracted
cancel_reason	string	Reason for cancellation	wrong address	EDA	Cleaned
ctat	float	Customer wait time	15.5	KPI	Missing handled
vtat	float	Vehicle arrival time	14.2	Ops analysis	Converted
⚙️ Derived Columns
Derived Column	Logic	Business Meaning
is_successful	booking_status == "success"	Completed rides
cancel_flag	booking_status contains "cancel"	Cancelled rides
time_of_day	Based on hour buckets	Time segmentation
revenue_lost	Avg revenue for cancelled rides	Opportunity loss
completion_rate	successful / total	Efficiency metric
cancellation_rate	cancelled / total	Core KPI
⚠️ Data Quality Notes
Dataset covers only January 2024
Locations are anonymized (Area-1 to Area-50)
Ratings missing for cancelled rides
Revenue for cancelled rides is estimated
No driver/customer IDs available
Some categorical inconsistencies corrected
🛠 Tools Used
Python (pandas, numpy) — data cleaning & transformation
Jupyter Notebook — analysis
Tableau Public — visualization
