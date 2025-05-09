import csv

# List of all columns (factors)
columns = [
    "crop_name",
    "region",
    "year",
    "month",
    "market_price",
    "rainfall",
    "crop_variety",

    # next 4 may be optional for input in model
    "area_sown",
    "yield",
    "irrigated_percent",
    "fertilizer_used",
    "msP",
    "market_demand",
    "export_demand",
    "input_cost",
    "transport_cost",
    "govt_scheme_active",
    "cold_storage_available",
    "mandi_open"
]

# Create the CSV file with only header row
with open("crop_price_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columns)

print("CSV file 'crop_price_data.csv' created with headers only.")
