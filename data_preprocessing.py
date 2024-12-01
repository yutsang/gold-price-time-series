import pandas as pd

def clean_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    
    # Remove duplicates
    data = data.drop_duplicates()
    
    # Handle missing values
    data = data.fillna(method='ffill')  # Forward fill
    
    # Convert data types if necessary
    # e.g., data['column_name'] = data['column_name'].astype('float')
    
    # Save cleaned data
    cleaned_file_path = 'cleaned_data.csv'
    data.to_csv(cleaned_file_path, index=False)
    return cleaned_file_path

# Example usage:
if __name__ == "__main__":
    raw_file = 'gold_dec24(GC=F)_1d.csv'
    cleaned_file = clean_data(raw_file)
    print(f"Cleaned data saved to: {cleaned_file}")