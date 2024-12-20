# 🍽️ Dishcovery - Restaurant Recommendation and Customer Segmentation System

## 📚 Project Overview

Dishcovery is a restaurant recommendation system tailored for Mexican restaurants, designed to cater to very specific consumer characteristics. Users can explore restaurants based on features such as family-friendly atmosphere, smoking areas, parking availability, and more. A key highlight of the system is the ability to view satisfaction ratings from users with similar demographic and social profiles, alongside traditional restaurant searches.

Additionally, Dishcovery offers a unique feature for entrepreneurs aiming to open a restaurant business. By analyzing customer ratings and segmenting demographics, entrepreneurs can identify the profiles of customers who highly rated similar restaurants, or conversely, those who gave negative ratings. This allows for strategic decision-making when designing a new restaurant concept.

The project segments users who rate restaurants based on diverse characteristics, such as income level, marital status, and demographics, enabling a deeper understanding of customer preferences and satisfaction.

## ⚠️ Important Note for Data Usage

To replicate the project using SQL with Workbench, create a database named **"restaurants"** and import the CSV files using the SQL "Wizard" option. The table mapping is as follows:

| 📂 CSV File Name         | 🗂️ Table Name     | 🗑️ Description                                      |
|--------------------------|------------------|---------------------------------------------------|
| chefmozaccepts.csv       | rest_pay         | Payment methods accepted by the restaurant        |
| chefmozcuisine.csv       | rest_cui         | Cuisine type by restaurant                        |
| chefmozhours4.csv        | opening          | Opening hours and days of operation              |
| chefmozparking.csv       | if_parking       | Indicates if the restaurant has parking           |
| geoplaces2.csv           | location         | City, country, and coordinates of the restaurant  |
| rating_final.csv         | rating           | Ratings of different characteristics of the restaurant |
| usercuisine.csv          | user_cui         | User cuisine type preferences                     |
| userpayment.csv          | user_pay         | User payment method preferences                   |
| userprofile.csv          | user_profile     | User profile information                          |

## ⭐ Rating Methodology

The project uses a customer satisfaction survey rating system based on the Net Promoter Score (NPS) methodology. Ratings are categorized into three groups:

- **Promoters** (score of 2) 👍
- **Passives** (score of 1) 😐
- **Detractors** (score of 0) 🙇

This categorization helps in understanding customer sentiment and loyalty, enabling more accurate recommendations and analysis.

## 📂 Project Structure

The project is organized into the following directories:

### 1. `code` 🖥️
Contains the core scripts for the project:

- **Jupyter Notebooks**: Four notebooks for cleaning, exploratory data analysis (EDA), and table processing:
  - `cleaning_EDA_restaurants.ipynb`: Handles the cleaning and standardization of restaurant data, including the removal of underscores and capitalization of column names for better user readability. The cleaning and EDA processes retrieve data directly from the SQL database via Workbench.
  - `cleaning_EDA_users.ipynb`: Focuses on cleaning and analyzing user data.
  - `merge_filter.ipynb`: Processes combined tables for integration into Streamlit, using the cleaned and analyzed data from the previous notebooks.

- **SQL File**: A script to set up the relational database and perform queries for creating joint tables.

### 2. `data` 📊
Contains:

- Original CSV files used to populate the SQL database.
- Processed CSV files resulting from the cleaning steps in the Jupyter Notebooks.

### 3. `documents` 📜
Includes:

- `model_sql`: Documentation for the SQL database configuration, named "restaurants."
- An Entity-Relationship Diagram (ERD) file illustrating the database structure.

### 4. `streamlit` 🌐
Contains:

- `st_link.py`: The code for the Dishcovery application. This Streamlit app allows users to access the two core services:
  1. Personalized restaurant recommendations. 🍽️
  2. Customer segmentation insights for aspiring restaurant entrepreneurs. 🏢

### 5. Root Directory 📁
Includes:

- **ERD Diagram**: A JPEG file of the SQL database schema.
- **CSV Documentation**: A text file recognizing the original data sources:
  - Creators: Rafael Ponce Medellín and Juan Gabriel González Serna (Department of Computer Science, National Center for Research and Technological Development CENIDET, México).
  - Donors: Blanca Vargas-Govea and Juan Gabriel González Serna (Department of Computer Science, National Center for Research and Technological Development CENIDET, México).
- **Tableau File**: A `.twb` file showcasing the final project presentation.

## 📌 Project Log

A relational database was developed to store information about restaurants and their customers. SQL Workbench was used to connect with Python, enabling the extraction of data for exploratory analysis.

### Workflow Summary 🛠️
1. **Database Setup**: Tables were imported and cleaned in SQL Workbench.
2. **Exploratory Data Analysis (EDA)**: Conducted in Jupyter Notebooks (`cleaning_EDA_restaurants` and `cleaning_EDA_users`), focusing on restaurant and user characteristics.
3. **Table Processing**: Final table processing was completed in `merge_filter.ipynb` for Streamlit integration.
4. **Streamlit App**: Built to provide personalized recommendations and customer segmentation insights.
5. **Visualization**: Tableau was used to present the project's final outcomes.
