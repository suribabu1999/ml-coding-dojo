import kagglehub

# Download latest version
path = kagglehub.dataset_download("ranafayezz/flight-price-prediction-df")

print("Path to dataset files:", path)