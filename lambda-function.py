from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import json
import os

def process_nutritional_data_from_azurite():
    connect_str = "UseDevelopmentStorage=true"

    print(" Connecting to Azurite Blob Storage...")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create container if it doesn't exist
    container_name = 'datasets'
    try:
        blob_service_client.create_container(container_name)
        print(f" Container '{container_name}' created.")
    except Exception:
        print(f" Container '{container_name}' already exists.")

    # Upload CSV to Azurite
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='All_Diets.csv')
    with open('All_Diets.csv', 'rb') as f:
        blob_client.upload_blob(f, overwrite=True)
    print(" All_Diets.csv uploaded to Azurite.")

    # Download and process it
    print(" Downloading and processing data...")
    stream = blob_client.download_blob().readall()
    df = pd.read_csv(io.BytesIO(stream))
    print(f" Dataset loaded: {len(df)} rows")

    df['Diet_type'] = df['Diet_type'].str.lower().str.strip()
    df['Protein(g)'].fillna(df['Protein(g)'].mean(), inplace=True)
    df['Carbs(g)'].fillna(df['Carbs(g)'].mean(), inplace=True)
    df['Fat(g)'].fillna(df['Fat(g)'].mean(), inplace=True)

    avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
    print("\n Average Macronutrients per Diet Type:")
    print(avg_macros)

    # Save to simulated NoSQL (JSON file)
    os.makedirs('simulated_nosql', exist_ok=True)
    result = avg_macros.reset_index().to_dict(orient='records')
    with open('simulated_nosql/results.json', 'w') as f:
        json.dump(result, f, indent=4)

    print("\n Results saved to simulated_nosql/results.json")
    return " Data processed and stored successfully."

if __name__ == "__main__":
    message = process_nutritional_data_from_azurite()
    print(f"\n {message}")
