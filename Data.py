# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_IN1yxIW6KbDbht75hGcyTSJsJDklXzp
"""

import pandas as pd

# Data for snacks, candies, cookies, and other eating products
data = [
    {"Product Name": "Օրեո (Oreo) 150գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Gluten, Dairy"},
    {"Product Name": "ԿիտԿատ (KitKat) 40գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Dairy, Soy"},
    {"Product Name": "Սնիքերս (Snickers) 50գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Peanuts, Dairy"},
    {"Product Name": "Միլկա Շոկոլադ (Milka Chocolate) 100գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Dairy"},
    {"Product Name": "Թաֆի (Taffy Candy) 100գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Թթվասեր Սմարթիս (Sour Smarties) 50գ", "Packaging Info": "Plastic Tube", "Reusability Score": 0.4, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "ՄՄԴ (M&M's) 100գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Dairy, Peanuts"},
    {"Product Name": "Մարշմալո (Marshmallow) 100գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Չիպսեր (Potato Chips) 200գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Դորիտոս (Doritos) 150գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Պոպկորն (Popcorn) 100գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Սուպեր Քուկի (Super Cookie) 150գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Gluten, Dairy"},
    {"Product Name": "Պրետցելներ (Pretzels) 200գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Gluten"},
    {"Product Name": "Ֆրունչ Սթիքս (Crunch Sticks) 100գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Բաունթի (Bounty) 50գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Coconut, Dairy"},
    {"Product Name": "Տոբլերոնե (Toblerone) 100գ", "Packaging Info": "Cardboard Box", "Reusability Score": 0.8, "Health Labels": "Eco-friendly, Recyclable", "Allergens": "Dairy, Nuts"},
    {"Product Name": "Սփրիտ Քենդի (Sprite Candy) 50գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Հրուշակ (Nougat Candy) 100գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Nuts, Dairy"},
    {"Product Name": "Միկադո Սթիքս (Mikado Sticks) 75գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Gluten"},
    {"Product Name": "Նուտելլա Բիսքվիթ (Nutella Biscuit) 150գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Gluten, Dairy, Hazelnut"},
    {"Product Name": "Մաքսի Կոուքի (Maxi Cookie) 200գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Gluten, Dairy"},
    {"Product Name": "Չիթոս (Cheetos) 150գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Կրեկեր (Crackers) 200գ", "Packaging Info": "Plastic Bag", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Gluten"},
    {"Product Name": "Բրիկետներ (Granola Bars) 100գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "Nuts"},
    {"Product Name": "Լեվե Ֆրեշ (Leve Fresh Gum) 50գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.2, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Խնձոր (Apple) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "None"},
    {"Product Name": "Բանան (Banana) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Տանձ (Pear) 1կգ", "Packaging Info": "Cardboard Box", "Reusability Score": 0.8, "Health Labels": "Eco-friendly, Recyclable", "Allergens": "None"},
    {"Product Name": "Խաղող (Grapes) 1կգ", "Packaging Info": "Biodegradable Plastic", "Reusability Score": 0.6, "Health Labels": "Eco-friendly, Biodegradable", "Allergens": "None"},
    {"Product Name": "Նարինջ (Orange) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Կիվի (Kiwi) 1կգ", "Packaging Info": "Cardboard Box", "Reusability Score": 0.8, "Health Labels": "Eco-friendly, Recyclable", "Allergens": "None"},
    {"Product Name": "Սեխ (Melon) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "None"},
    {"Product Name": "Սերկեւիլ (Quince) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Բալի (Cherry) 1կգ", "Packaging Info": "Biodegradable Plastic", "Reusability Score": 0.6, "Health Labels": "Eco-friendly, Biodegradable", "Allergens": "None"},
    {"Product Name": "Մանդարին (Mandarin) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "None"},
    {"Product Name": "Կարտոֆիլ (Potato) 1կգ", "Packaging Info": "Mesh Bag", "Reusability Score": 0.5, "Health Labels": "Eco-friendly, Recyclable", "Allergens": "None"},
    {"Product Name": "Սոխ (Onion) 1կգ", "Packaging Info": "Mesh Bag", "Reusability Score": 0.5, "Health Labels": "Eco-friendly, Recyclable", "Allergens": "None"},
    {"Product Name": "Սմբուկ (Eggplant) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Լոլիկ (Tomato) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "None"},
    {"Product Name": "Վարունգ (Cucumber) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Գազար (Carrot) 1կգ", "Packaging Info": "Mesh Bag", "Reusability Score": 0.5, "Health Labels": "Eco-friendly, Recyclable", "Allergens": "None"},
    {"Product Name": "Բազուկ (Beetroot) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "None"},
    {"Product Name": "Բուլղարական պղպեղ (Bell Pepper) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Սպանախ (Spinach) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "None"},
    {"Product Name": "Ծաղկակաղամբ (Cauliflower) 1կգ", "Packaging Info": "Biodegradable Plastic", "Reusability Score": 0.6, "Health Labels": "Eco-friendly, Biodegradable", "Allergens": "None"},
    {"Product Name": "Ծիրանաչիր (Dried Apricot) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Սալորաչիր (Dried Plum) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Ընկույզ (Walnut) 1կգ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Organic, Biodegradable", "Allergens": "Tree Nuts"},
    {"Product Name": "Նուշ (Almond) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Tree Nuts"},
    {"Product Name": "Սունկ (Mushroom) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "None"},
    {"Product Name": "Հաց (Bread) 500գ", "Packaging Info": "Paper Bag", "Reusability Score": 0.7, "Health Labels": "Biodegradable, Organic", "Allergens": "Gluten"},
    {"Product Name": "Պանիր (Cheese) 1կգ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Dairy"},
    {"Product Name": "Կաթնաշոռ (Cottage Cheese) 500գ", "Packaging Info": "Plastic Wrapper", "Reusability Score": 0.3, "Health Labels": "Non-biodegradable", "Allergens": "Dairy"},
    {"Product Name": "Կաթ (Milk) 1լ", "Packaging Info": "Glass Bottle", "Reusability Score": 0.9, "Health Labels": "Reusable, Recyclable", "Allergens": "Dairy"},
    {"Product Name": "Յոգուրտ (Yogurt) 400գ", "Packaging Info": "Plastic Container", "Reusability Score": 0.4, "Health Labels": "Non-biodegradable", "Allergens": "Dairy"},
]

# Create a pandas DataFrame
df = pd.DataFrame(data)

df.to_csv('products.csv', index=False)

df = pd.read_csv('products.csv')
print(df)

from google.colab import files

# Download the file
files.download('products.csv')
