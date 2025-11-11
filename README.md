# Creation and Visualization of a Synthetic Dataset - Bakery Market (python)

### Simulating Realistic Customer Data for Data Analysis and Insights

## Description

This project demonstrates the end-to-end creation of a **synthetic customer dataset** for data analysis purposes. The entities and atributtes are related to the bakery market but can be adjusted to other markets needs.

The dataset simulates realistic information about **customer demographics, preferences, purchase behavior, seasonality, and pricing sensitivity**, reflecting a typical e-commerce or retail environment. Moreover, also include inconsistencies related to real world surveys.

This dataset was designed, generated, and structured using a **relational data model** and later exported to `.csv` and `.xlsx` formats for analytical use. The project also includes **built-in visualization tools** to inspect the generated data quickly and tune for adjustments.

The dataset is **educational**: it allows practice in **data cleaning, visualization, and analysis** using tools like Excel, Tableau, or Power BI. Although inconsistencies are known, the goal is to practice **realistic data handling and exploratory analysis**.


---

## Business Context & Problem

Students often struggle to analyze **customer behavior and pricing perception** due to fragmented or private data.  
This project addresses that issue by **creating a realistic synthetic dataset** that answers key business questions such as:

- What are the main customer segments (kids vs adults)?
- Which flavor preferences or product configurations are most common?
- How do seasonal interests influence purchase frequency?
- What pricing tiers are most appealing to different customer types?

The goal is to **build a structured, queryable dataset** that supports analytics on customer behavior and business insights.

---

## Project Objectives

- Simulate a realistic relational dataset following database design principles.  
- Generate synthetic but coherent data using Python.  
- Provide a dataset ready for querying and visualization.  
- Derive insights about customer preferences, seasonality, and pricing willingness.  
- Strengthen portfolio skills in **data modeling**, **synthetic data creation**, and **data storytelling**.

---

## Dataset Overview

The dataset includes **five main entities**:

| Entity | Description |
|--------|--------------|
| **Customer** | Basic demographic data of each client (type, age, gender). |
| **Preference** | Favorite product characteristics (batter, filling, frosting, toppings). |
| **Purchase** | Customer buying behavior and frequency. |
| **Seasonality** | Seasonal patterns or interests in specific times of the year. |
| **Pricing** | Product type and willingness to pay. |

Each entity is connected logically based on a conceptual model reflecting **customer interaction with products and pricing**.

---

## Tools and Technologies

| Category | Tools |
|-----------|--------|
| **Language** | Python 3 |
| **Libraries** | Pandas, NumPy, Faker, Random |
| **Environment** | Google Colab / Jupyter Notebook |
| **Data Format** | CSV, XLSX |
| **Visualization** | Sweetviz HTML report |

---

## Dataset Creation Process

1. **Define logical structure** based on five entities and their relationships.  
2. **Simulate realistic data** using the `Faker` library and random distributions.  
3. **Apply logical constraints**, such as:
   - Kids: ages 4–17  
   - Adults: ages 18–99
4.  **Apply pricing rules and category limitations**:
   - **Cupcake or Slice:** €1.00 – €6.00  
   - **Whole Cake:** up to €40.00  
   - **Wedding Cake:** up to €100.00  
5. **Ensure data consistency** across related entities.
6. **Insert intentional inconsistencies** to simulate real-world messy datasets , perfect for cleaning practice:
  - Random **null values** in multiple columns.  
  - Extreme or invalid **ages** (e.g., negative, 999, or None).  
  - **Typos in categorical columns** for spelling correction exercises.  
  - **Mixed data types** in categorical columns (e.g., numbers and strings in the same column).  
  - **Kids assigned adult products**, such as Wedding cakes.  
  - **Inconsistent price formats** (`€`, `Free`, `NaN`, empty strings).  
  - **Duplicate rows** to practice handling redundancy.
7. ** Insert Weighted Preferences and Statistical Relevance**:
  - Adults and kids have distinct preferences for **batter, filling, frosting, and toppings**:  
  - **Adults:** Lemon, Carrot, Cream Cheese, etc.  
  - **Kids:** Chocolate, Red Velvet, Chocolate glaze, extra toppings  
  - Weighted probabilities create **statistically significant differences** between adults, kids, and genders, so analyses reveal real distinctions.  
  - **Gender distribution** is set to **65% female** and **35% male**.  
  - Extra toppings are **mostly chosen by kids**, reflecting realistic behavior patterns.
8. **Create Quick Data Visualization** to verify the data, identify issues, and prepare datasets for further analysis:
  - **Sweetviz HTML report**:
  - Shows feature distributions, correlations, and inconsistencies.
  - Automatically highlights categorical and numerical columns.
  - Compare **Type_of_client vs Gender**.
  - Analyze favorite flavors by **client type**.
  - Observe the effect of weighted preferences and inconsistencies.

9. **Export final dataset** to `.csv` and `.xlsx` for analysis in Tableau, Power BI, Excel, etc.

Example output file:  
`synthetic_dataset_raw_bakery.csv`

---

## Example Use Cases

- Segmenting customers by age group and purchase frequency.  
- Analyzing preferences by product configuration.  
- Identifying seasonal buying patterns.  
- Correlating willingness to pay with demographic variables.  
- Power BI / Tableau visualization projects.

---

## Project Structure

📁 Synthetic_Customer_Dataset/<br>
├── README.md<br>
├── requirements.txt<br>
├── Synthetic_data_generator_bakery.py  # Python archive<br>
├── Synthetic_data_generator_bakery.ipynb  # Colab notebook<br>
├── synthetic_dataset_raw_bakery.csv  # Exported dataset<br>
├── synthetic_dataset_raw_bakery.xlsx  # Excel version<br>
└── synthetic_data_bakery_report.html  # HTML data visualization



---

## How to Run

### Option 1 — Google Colab
1. Open [Google Colab](https://colab.research.google.com)
2. Upload the `.ipynb` file  
3. Run all cells  
4. Download your dataset via:
   ```python
   from google.colab import files
   files.download('synthetic_customer_dataset.csv')


### Option 2 — Local Environment

pip install pandas numpy faker sweetviz webbrowser

python Synthetic_data_generator_bakery.py


## Conclusion

This project combines database modeling, synthetic data generation, and analytical design to simulate a realistic scenario of customer behavior in the confectionery industry.
It demonstrates how to transform a business problem into structured, analyzable data by building a foundation for future exploration in SQL querying, data visualization, and market insights.

## Agatha Carretero
Data Analyst | Data Visualization | SQL | Python | Power BI
Contact: agathacarretech@gmail.com
Medium article: [Insert Medium post ]





