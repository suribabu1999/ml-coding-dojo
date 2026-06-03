import kagglehub
import shutil
import os

# Download dataset to cache
cache_path = kagglehub.dataset_download(
    "ranafayezz/flight-price-prediction-df"
)

# Destination folder in your project
destination = os.path.join(
    os.path.dirname(__file__),
    "flight-price-prediction-df"
)

# Create folder if it doesn't exist
os.makedirs(destination, exist_ok=True)

# Copy files from cache to project folder
for file_name in os.listdir(cache_path):
    source_file = os.path.join(cache_path, file_name)
    destination_file = os.path.join(destination, file_name)

    if os.path.isfile(source_file):
        shutil.copy2(source_file, destination_file)

print("Dataset copied to:", destination)