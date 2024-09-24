# Soccer Match Scraper and Weather Forecast

## Project Description

This project is designed to scrape soccer match schedules from the UEFA Champions League (UCL) and English Premier League (EPL) using CBS Sports and to enhance that data by providing weather forecasts for the matches using the WeatherAPI. The purpose of the project is to create a combined dataset of upcoming matches, including details like the teams, venues, and weather conditions on the matchday. This offers soccer enthusiasts, sports journalists, and analysts a way to get both match information and weather forecasts in one place.

### Why CBS Sports?
CBS Sports was chosen because it provides detailed, structured, and reliable information about upcoming soccer fixtures, including match times, team details, and venue names. The website updates the match data in real time and ensures accuracy, making it a trusted source for scraping upcoming fixtures.

## Data Collection

### Web Scraper Data (CBS Sports)
The data collected from CBS Sports includes:
- **Date**: The day the match will be played.
- **Time**: The scheduled time for the match.
- **Home Team**: The team playing at home.
- **Away Team**: The visiting team.
- **Venue**: The stadium where the match will be played.

The web scraper is designed to gather match schedules for multiple matchdays in the UCL and EPL and save them in CSV format (`ucl_matches.csv` and `pl_matches.csv`).

### Weather Forecast Data (WeatherAPI)
For each match, a weather forecast for the day of the match and the city of the venue is fetched using the WeatherAPI. The data includes:
- **City**: The city in which the match will take place, derived from the venue.
- **Weather Condition**: The predicted weather condition (e.g., clear, cloudy, rainy) for the day of the match.

The weather forecasts are added to the existing match data, creating a CSV file with both match and weather information.

## Purpose and Value of the Dataset

The primary goal of this project is to create a **comprehensive dataset** that combines soccer match information with **weather forecasts**. Weather conditions can have a significant impact on match outcomes, player performance, and audience experience, making this combined dataset valuable to multiple user groups.

### Value Proposition:
1. **Sports Analysts**: Analysts can use the dataset to identify trends, such as how weather conditions impact match outcomes, goal counts, and player performance.
2. **Betting Enthusiasts**: Weather plays a significant role in soccer, influencing match results. By integrating weather data, betting enthusiasts can make more informed decisions.
3. **Sports Journalists**: With a single dataset, journalists can quickly prepare articles and reports, mentioning not only upcoming match details but also expected weather conditions.
4. **Soccer Fans**: Fans attending matches can plan better by knowing the weather in advance. They can adjust their travel or prepare for weather conditions when watching games in outdoor stadiums.
5. **Data Scientists and Researchers**: The combined dataset is a rich source for conducting research in sports analytics, including correlations between weather and game performance.

### Why This Dataset is Unique:
- **Combination of Match and Weather Data**: While match schedules are publicly available and weather forecasts can be accessed via APIs, a **dataset that combines both match schedules and weather forecasts for future matches** is not readily available for free. This dataset fills that gap.
- **Customized for Soccer**: Unlike generic weather services, this dataset focuses specifically on **soccer matches**, which makes it highly relevant to soccer enthusiasts and professionals.
- **Automation**: This project automates the collection and combination of this data, which would otherwise require manual aggregation.

Given that most available datasets either focus on **match statistics** or **historical data**, the availability of **weather data for future matches** is a unique feature, which is typically a paid feature in certain premium sports analysis services.

## How to Run This Project

### Prerequisites
1. **Python 3.10**: Make sure Python is installed on your system.
2. **API Key**: Sign up for a free API key from [WeatherAPI](https://www.weatherapi.com/) to fetch weather data.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/soccer-match-forecast.git
   cd soccer-match-forecast
   ```

2. **Install Required Libraries**:
   Install the necessary Python libraries using the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Scrape the Match Data**:
   Run `scraper.py` to scrape match data for upcoming UCL and EPL games from CBS Sports. This will create CSV files with the match data.
   ```bash
   python scraper.py
   ```

2. **Get Weather Forecasts**:
   After you have the match data, run `weather_predict_pipeline.py` to fetch weather forecasts and augment the dataset with weather information. Ensure you have replaced `YOUR_API_KEY` with your WeatherAPI key in the `weather_predict_pipeline.py` file.
   ```bash
   python weather_predict_pipeline.py
   ```

3. **Output**:
   After running the scripts, the final datasets will be available in the following files:
   - `ucl_matches_with_forecast.csv`: UEFA Champions League matches with weather forecasts.
   - `pl_matches_with_forecast.csv`: Premier League matches with weather forecasts.

### Example Output CSV

| date       | time       | home_team        | away_team      | venue             | stadium_details | weather_forecast              |
|------------|------------|------------------|----------------|-------------------|-----------------|-------------------------------|
| 2024-11-05 | 3:00 PM    | Real Madrid      | AC Milan       | Santiago Bernabéu  | Madrid          | Moderate or heavy rain shower  |
| 2024-11-03 | 11:30 AM   | Manchester United| Chelsea        | Old Trafford       | Manchester      | Patchy rain possible           |

## Future Improvements

- **Add Support for Other Leagues**: Expanding the scraper to include other leagues like La Liga, Serie A, and Bundesliga.
- **Historical Weather Data**: Adding functionality to fetch and analyze weather data for past matches.
- **Match Results Integration**: Augmenting the dataset with match results to correlate weather conditions with match outcomes.

## Contributions
Contributions are welcome! If you want to improve the project, feel free to fork the repository and submit a pull request, or open an issue if you find a bug.

