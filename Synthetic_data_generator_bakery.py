# Synthetic Bakery Dataset Generator with Weighted Preferences, Inconsistencies and Visual Report

import pandas as pd
import numpy as np
from faker import Faker
import random
import sweetviz as sv
import webbrowser

# Patch for NumPy 2.x for compatibility with Sweetviz (visual report)
if not hasattr(np, "VisibleDeprecationWarning"):
    class VisibleDeprecationWarning(UserWarning):
        pass
    np.VisibleDeprecationWarning = VisibleDeprecationWarning

# Initialize Faker
fake = Faker()

# -------------------------------
# Constants and weighted preferences
# -------------------------------

# Batters
batters_adult = ["Lemon", "Carrot", "Red Velvet"]
batters_adult_weights = [0.4, 0.35, 0.25]

batters_kid = ["Chocolate", "Red Velvet"]
batters_kid_weights = [0.6, 0.4]

# Fillings
fillings_adult = ["Cream cheese", "Dulce de leche", "Lemon curd"]
fillings_adult_weights = [0.5, 0.3, 0.2]

fillings_kid = ["Chocolate ganache", "Strawberry jam"]
fillings_kid_weights = [0.7, 0.3]

# Frostings
frostings_adult = ["Cream cheese frosting", "Ganache", "Chocolate glaze"]
frostings_adult_weights = [0.5, 0.3, 0.2]

frostings_kid = ["Chocolate glaze", "Buttercream", "Whipped cream"]
frostings_kid_weights = [0.6, 0.25, 0.15]

# Toppings
topping_examples = ["Fruits", "Sprinkles", "Nuts", "Chocolate chips", "Edible flowers"]

# Configurations
configurations_adult = ["Slice", "Whole cake", "Wedding cake"]
configurations_kid = ["Cupcake", "Slice"]

# Occasions
occasions_adult = ["Celebration", "Gathering", "Wedding", "Work event"]
occasions_kid = ["Snack", "Birthday", "Celebration"]

# Frequencies and seasonal options
frequencies = ["Daily", "Weekly", "Monthly", "Sporadic"]
seasonal_options = ["Christmas", "Halloween", "Valentine's Day", "Easter", "Fall"]
genders = ["Feminine", "Masculine"]

# -------------------------------
# Price generation definition
# -------------------------------
def generate_price(product_type):
    if product_type in ["Cupcake", "Slice"]:
        price = round(random.uniform(1.0, 6.0), 2)
        price = round(price * 10) / 10
        return f"{price:.2f} €"
    elif product_type == "Whole cake":
        price = round(random.uniform(10.0, 40.0), 2)
        price = round(price * 10) / 10
        return f"{price:.2f} €"
    elif product_type == "Wedding cake":
        price = round(random.uniform(40.0, 100.0), 2)
        price = round(price * 10) / 10
        return f"{price:.2f} €"

# -------------------------------
# Generate data
# -------------------------------
n = 1500
data = []

for _ in range(n):
    # Client type
    type_of_client = np.random.choice(["Adult", "Kid"], p=[0.7, 0.3])
    age = random.randint(4, 17) if type_of_client == "Kid" else random.randint(18, 65)

    # Gender: 65% female
    gender = np.random.choice(genders, p=[0.65, 0.35])

    # Favorites with weighted choices
    if type_of_client == "Kid":
        favorite_batter = np.random.choice(batters_kid, p=batters_kid_weights)
        favorite_filling = np.random.choice(fillings_kid, p=fillings_kid_weights)
        favorite_frosting = np.random.choice(frostings_kid, p=frostings_kid_weights)
        more_toppings = np.random.choice(["Yes", "No"], p=[0.7, 0.3])
        configuration = np.random.choice(configurations_kid)
        occasion = np.random.choice(occasions_kid)
    else:
        favorite_batter = np.random.choice(batters_adult, p=batters_adult_weights)
        favorite_filling = np.random.choice(fillings_adult, p=fillings_adult_weights)
        favorite_frosting = np.random.choice(frostings_adult, p=frostings_adult_weights)
        more_toppings = np.random.choice(["Yes", "No"], p=[0.3, 0.7])
        configuration = np.random.choice(configurations_adult)
        occasion = np.random.choice(occasions_adult)

    topping_choice = np.random.choice(topping_examples) if more_toppings == "Yes" else "None"

    # Frequency and seasonality
    frequency = np.random.choice(frequencies, p=[0.3, 0.4, 0.2, 0.1])
    interest_in_seasonality = np.random.choice(["Yes", "No"], p=[0.3, 0.7])
    seasonal_choice = np.random.choice(seasonal_options) if interest_in_seasonality == "Yes" else "None"

    # Price
    product_type = configuration
    willingness_to_pay = generate_price(product_type)

    # Append row
    data.append([
        type_of_client, age, gender,
        favorite_batter, favorite_filling, favorite_frosting,
        more_toppings, topping_choice, configuration,
        frequency, occasion,
        interest_in_seasonality, seasonal_choice,
        product_type, willingness_to_pay
    ])

# -------------------------------
# Create DataFrame
# -------------------------------
columns = [
    "Type_of_client", "Age", "Gender",
    "Favorite_batter", "Favorite_filling", "Favorite_frosting",
    "More_toppings", "Topping_examples", "Configuration",
    "Frequency_of_buying", "Occasion",
    "Interest_in_seasonality", "Seasonal_option",
    "Product_type", "Willingness_to_pay"
]
df = pd.DataFrame(data, columns=columns)

# -------------------------------
# Introduce artificial inconsistencies to simulate real-world data
# -------------------------------
print("Adding artificial inconsistencies...")

# Random nulls
for col in random.sample(df.columns.tolist(), 6):
    idx = random.sample(range(len(df)), random.randint(15, 40))
    df.loc[idx, col] = None

# Wrong age
for i in random.sample(range(len(df)), 20):
    df.loc[i, "Age"] = random.choice([-3, 150, 999, None])

# Typos mispellings
typo_values = {
    "Favorite_batter": ["Choclate", "Vannila", "Red Velvt", "Lemonn"],
    "Frequency_of_buying": ["Daly", "Weeekly", "Montly", "Spordic"],
    "Gender": ["Fem", "Masc", "Femanine"]
}
for col, typos in typo_values.items():
    for _ in range(8):
        idx = random.randint(0, len(df)-1)
        df.loc[idx, col] = random.choice(typos)

# Inconsistent prices
for i in random.sample(range(len(df)), 15):
    df.loc[i, "Willingness_to_pay"] = random.choice(["Free", "?", "NaN", "", "€", "10", None])

# Kids buying adult products that don't make sense
for i in random.sample(range(len(df)), 10):
    if df.loc[i, "Type_of_client"] == "Kid":
        df.loc[i, "Occasion"] = np.random.choice(["Work event", "Wedding"])
        df.loc[i, "Product_type"] = "Wedding cake"

# Duplicate rows
for i in random.sample(range(100,200), 5):
    df.loc[i+5] = df.loc[i]

# Mixed types in categorical columns
for i in random.sample(range(len(df)), 10):
    df.loc[i, "Favorite_filling"] = random.choice([123, None, True, "ok"])

print("Artificial inconsistencies added successfully!")

# -------------------------------
# To export the dataset
# -------------------------------
df.to_excel("synthetic_dataset_raw_bakery.xlsx", index=False)
df.to_csv("synthetic_dataset_raw_bakery.csv", index=False, sep=";", encoding="utf-8")
print("File 'synthetic_dataset_raw_bakery' created with 1500 rows.")

# -------------------------------
# Generate quick report for visual analysis
# -------------------------------
df = df.astype(str)  # ensure compatibility
print("Generating visualization report...")
report = sv.analyze(df)
report.show_html("synthetic_data_bakery_report.html")
webbrowser.open("synthetic_data_bakery_report.html")
print("Report generated: synthetic_data_bakery_report.html")
