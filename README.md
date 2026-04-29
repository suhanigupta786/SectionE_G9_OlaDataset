🚖 OLA Rides — Cancellation, Revenue & Operations Intelligence Platform

Newton School of Technology | Data Visualization & Analytics Capstone 2

A 2-week industry simulation project using Python, GitHub, and Tableau to convert raw ride-booking data into actionable business intelligence.

📌 Project Overview
Field	Details
Project Title	OLA Rides — Cancellation, Revenue & Operations Intelligence Platform
Sector	Ride-Hailing / Urban Mobility
Team ID	9
Section	Section E
Faculty Mentor	Ayushi Vashisth
Institute	Newton School of Technology
Submission Date	29 April 2026
👥 Team Members
Role	Name	GitHub
Project Lead	Suhani Gupta	https://github.com/suhanigupta786
Data Lead	Kavya Saraswat	https://github.com/KavyaSaraswat23
ETL Lead	Divyanshu Raj	https://github.com/divyanshu-114
Analysis Lead	Joshit Dutta	https://github.com/joshitdutta000
Visualization Lead	Husain Khorakiwala	https://github.com/AvgBlank
PPT & Quality Lead	Vidit Sachan	https://github.com/viditsachan
💼 Business Problem

OLA is experiencing a high cancellation rate (~33%), resulting in significant revenue loss and poor customer experience. Nearly one in three rides fails to complete, leading to inefficiencies in fleet utilization and lost business opportunities.

This project aims to identify where, when, and why cancellations occur, and provide actionable insights to improve ride completion, operational efficiency, and revenue.

🎯 Core Business Question

Which combination of location, time, and vehicle type drives the highest cancellation risk, and how can OLA reduce revenue loss?

📈 Decision Supported

This analysis enables stakeholders to:

Reduce cancellations through targeted interventions
Improve driver allocation and fleet efficiency
Recover lost revenue through data-driven strategies
📊 Dataset
Attribute	Details
Source	Kaggle – Ola Ride Dataset
Link	https://www.kaggle.com/datasets/muhammadahmadmujahid/ola-dataset

Rows	49,866
Columns	~20
Time Period	Jan 2024
Format	CSV
🔑 Key Columns Used
Column	Description	Role
Booking_ID	Unique ride identifier	KPI calculation
Vehicle_Type	Type of vehicle	Segmentation
Pickup_Location	Area code	Location analysis
Booking_Status	Ride outcome	KPI calculation
Revenue	Ride revenue	Financial analysis
Customer_Rating	User feedback	CX analysis
Driver_Rating	Driver feedback	CX analysis
Time_of_Day	Time bucket	Trend analysis
📐 KPI Framework
KPI	Definition	Formula
Total Requests	Total demand	COUNT(Booking_ID)
Completion Rate	Ride success rate	Successful / Total
Cancellation Rate	Failed rides	Cancelled / Total
Revenue Earned	Total income	SUM(Revenue)
Revenue Lost	Lost opportunity	Estimated from cancelled rides
Avg Revenue/Ride	Unit economics	Revenue / Completed rides
📊 Tableau Dashboard

🔗 Dashboard URL:
https://public.tableau.com/app/profile/suhani.gupta2725/viz/OLABusinessDashboardAnalysis/Dashboard1

Executive View
High-level KPIs (Revenue, Requests, Cancellation Rate)
Daily & hourly trends
Vehicle and location performance
Operational View
Driver cancellations
Fleet efficiency
Cancellation heatmaps
Main Filters
Vehicle Type
Pickup Location
Time of Day
Hour
🔍 Key Insights
33% cancellation rate indicates major operational inefficiency
Driver cancellations (~19%) dominate over customer cancellations
Area-34, 36, 37 have highest revenue loss
Wrong Address is top customer cancellation reason
Late night demand is high but under-served
Prime Plus has highest cancellation rate among vehicles
Wait time (~15.5 mins) is consistently high
Fleet efficiency is only ~66%
Area-50 shows best performance (benchmark area)
₹2.53M recovery potential exists from driver cancellations
💡 Recommendations
#	Insight	Recommendation	Impact
1	High driver cancellations	Introduce driver incentives in hotspot areas	+₹1.6M/month
2	Wrong address issue	Improve address validation system	+₹237K/month
3	Late-night demand gap	Increase night-time driver supply	+₹135K/month
4	Vehicle-based issues	Target Prime Plus drivers with incentives	+₹99K/month
5	Area efficiency gap	Replicate best practices from Area-50	+₹47K/month
📁 Repository Structure
SectionE_G9_OlaDataset/
|
|-- README.md
|
|-- data/
|   |-- raw/
|   |-- processed/
|
|-- notebooks/
|   |-- 01_extraction.ipynb
|   |-- 02_cleaning.ipynb
|   |-- 03_eda.ipynb
|   |-- 04_statistical_analysis.ipynb
|   |-- 05_final_load_prep.ipynb
|
|-- scripts/
|   |-- etl_pipeline.py
|
|-- tableau/
|   |-- screenshots/
|   |-- dashboard_links.md
|
|-- reports/
|   |-- project_report.pdf
|   |-- presentation.pdf
|
|-- docs/
|   |-- data_dictionary.md

⚙️ Tech Stack
Tool	Purpose
Python (pandas, numpy)	Data cleaning & analysis
Jupyter Notebook	EDA & modeling
Tableau Public	Dashboard
GitHub	Version control
Google Colab	Optional execution
🔄 Analytical Pipeline
Define problem
Extract dataset
Clean & transform data
Perform EDA
Conduct statistical analysis
Build Tableau dashboard
Provide recommendations
📦 Submission Checklist

✔ GitHub repo structured correctly
✔ Dataset uploaded
✔ Notebooks completed
✔ Tableau dashboard published
✔ Screenshots added
✔ Report & PPT uploaded
✔ Data dictionary completed

📜 Conclusion

OLA’s high cancellation rate is a major revenue and operational bottleneck, driven primarily by driver-side issues and demand-supply imbalance.

This project provides:

Clear identification of problem hotspots
Data-backed recommendations
A scalable analytics framework

👉 Implementing these strategies can recover ₹1.5M+ monthly revenue and significantly improve platform efficiency.

⚠️ Limitations
Single-month dataset
No driver/customer IDs
Revenue loss is estimated
No real-time data
🚀 Future Scope
Predictive cancellation model (ML)
Real-time dashboards
Driver behavior analytics
Demand forecasting system
