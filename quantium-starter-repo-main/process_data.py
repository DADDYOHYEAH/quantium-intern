import pandas as pd
import glob
import os

def process_data():
    # Attempt to find files in the 'data' folder
    csv_files = glob.glob("data/*.csv")
    
    # Debugging: Print what was found
    print(f"Looking for files in: {os.getcwd()}/data")
    print(f"Found {len(csv_files)} CSV files.")

    # ERROR HANDLING: If no files found, stop here so it doesn't crash
    if not csv_files:
        print("ERROR: No files found! Check if the 'data' folder exists and contains CSVs.")
        return

    combined_data = []

    for file in csv_files:
        df = pd.read_csv(file)
        # Filter for Pink Morsel
        df = df[df['product'] == 'pink morsel']
        # Clean price
        df['price'] = df['price'].str.replace('$', '').astype(float)
        # Calculate sales
        df['sales'] = df['quantity'] * df['price']
        # Select columns
        df = df[['sales', 'date', 'region']]
        combined_data.append(df)

    final_df = pd.concat(combined_data, ignore_index=True)
    final_df = final_df.rename(columns={'sales': 'Sales', 'date': 'Date', 'region': 'Region'})
    final_df.to_csv("formatted_data.csv", index=False)
    print("Success! Created 'formatted_data.csv'")

if __name__ == "__main__":
    process_data()