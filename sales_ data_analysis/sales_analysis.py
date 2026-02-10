import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")


df['Date'] = pd.to_datetime(df['Date'])
df['Total_Sales'] = df['Quantity'] * df['Price']

print("\n--- Cleaned Data ---")
print(df)


print("\n--- Summary Statistics ---")
print(df.describe())

total_sales = df['Total_Sales'].sum()
print("\nTotal Sales:", total_sales)


category_sales = df.groupby('Category')['Total_Sales'].sum()
print("\nSales by Category:")
print(category_sales)


category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

daily_sales = df.groupby('Date')['Total_Sales'].sum()
daily_sales.plot(marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
