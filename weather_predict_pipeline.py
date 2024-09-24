import ast
import requests
from datetime import datetime
import pandas as pd


# Function to get weather forecast for a specific city and date
def get_weather_forecast(city, match_date):
    api_key = "YOU_API_KEY"
    # Ensure the match_date is a string in the proper format
    date_match = match_date
    print(city)
    print(date_match)
    
    # Make the API request
    url = f"http://api.weatherapi.com/v1/future.json?key={api_key}&q={city}&dt={date_match}"
    response = requests.get(url)
    data = response.json()
    print(data)

    forecast_text = data['forecast']['forecastday'][0]['day']['condition']['text']
    print(f"Weather Condition: {forecast_text}")

    return forecast_text

# Helper function to extract the city from the 'stadium_details' column
def extract_city(stadium_details):
    # Convert the string representation of tuple into a real tuple using ast.literal_eval
    city_country_tuple = ast.literal_eval(stadium_details)
    print(city_country_tuple)
    city = city_country_tuple[0]  # Extract the city
    print(city)
    return city

# Part 1
ucl_match_df = pd.read_csv('ucl_matches.csv')

ucl_match_df['date'] = ucl_match_df['date'].astype(str)

ucl_match_df['date'] = pd.to_datetime(ucl_match_df['date'], format='%Y%m%d')

# Define the date to compare with (Oct 8, 2024)
cutoff_date = pd.to_datetime('20241008', format='%Y%m%d')

# Subset the DataFrame with dates greater than October 8, 2024
subset_ucl_match_df = ucl_match_df[ucl_match_df['date'] > cutoff_date]

# Add a new column 'weather_forecast' to the DataFrame
subset_ucl_match_df['weather_forecast'] = subset_ucl_match_df.apply(lambda row: get_weather_forecast(extract_city(row['stadium_details']), row['date']), axis=1)

# Save the DataFrame with the weather forecast appended to a new CSV file
subset_ucl_match_df.to_csv('pl_matches_with_forecast.csv', index=False)

# Display the updated DataFrame with the weather forecasts
print(subset_ucl_match_df.head(30))



# Part 2 
pl_match_df = pd.read_csv('pl_matches.csv')

pl_match_df['date'] = pl_match_df['date'].astype(str)

pl_match_df['date'] = pd.to_datetime(pl_match_df['date'], format='%Y%m%d')

# Define the date to compare with (Oct 8, 2024)
cutoff_date = pd.to_datetime('20241008', format='%Y%m%d')

# Subset the DataFrame with dates greater than October 8, 2024
subset_pl_match_df = pl_match_df[pl_match_df['date'] > cutoff_date]

# Add a new column 'weather_forecast' to the DataFrame
subset_pl_match_df['weather_forecast'] = subset_pl_match_df.apply(
    lambda row: get_weather_forecast(row['stadium_details'], row['date']), axis=1
)
# Save the DataFrame with the weather forecast appended to a new CSV file
subset_pl_match_df.to_csv('pl_matches_with_forecast.csv', index=False)

# Display the updated DataFrame with the weather forecasts
print(subset_pl_match_df.head(30))
