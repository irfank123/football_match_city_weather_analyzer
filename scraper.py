import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# function to print out all the matches corresponding to a particular date.
def scrape_match_data(url,date):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    matches = []
    
    # Finding match table
    match_table = soup.find('table', class_='TableBase-table')
    if not match_table:
        return matches
    
    # Find all match rows
    match_rows = match_table.find_all('tr', class_='TableBase-bodyTr')

    
    for row in match_rows:
        teams = row.find_all('span', class_='TeamName')

        
        home_team = teams[0].text.strip() if len(teams) > 0 else 'N/A'
        away_team = teams[1].text.strip() if len(teams) > 1 else 'N/A'
        # Extract the time
        time = row.find('td', class_='TableBase-bodyTd', style=lambda x: x and "width: 15%;" in x).get_text(strip=True)

        # Extract the stadium name
        stadium = row.find('td', class_='TableBase-bodyTd', style=lambda x: x and "min-width: 120px;" in x).get_text(strip=True)
                    
        matches.append({
            'date': date,
            'time': time,
            'home_team': home_team,
            'away_team': away_team,
            'venue': stadium
        })
    
    return matches

# Part 1 : Creation of the Dataset for UEFA Champions League Games that have been announced and not been played yet.

# Dictionary to map the stadium name to the location its is present in
ucl_stadiums = {
    'Stadio Giuseppe Meazza': ('Milan', 'Italy'),
    'Emirates Stadium': ('London', 'England'),
    'Villa Park': ('Birmingham', 'England'),
    'Gewiss Stadium': ('Bergamo', 'Italy'),
    'Estadio Civitas Metropolitano': ('Madrid', 'Spain'),
    'Estadi Olimpic Lluis Companys': ('Barcelona', 'Spain'),
    'Allianz Arena': ('Munich', 'Germany'),
    'BayArena': ('Leverkusen', 'Germany'),
    'Estadio do Sport Lisboa e Benfica': ('Lisbon', 'Portugal'),
    "Renato Dall'Ara": ('Bologna', 'Italy'),
    'Signal Iduna Park': ('Dortmund', 'Germany'),
    'Stade du Roudourou': ('Guingamp', 'France'),
    'Celtic Park': ('Glasgow', 'Scotland'),
    'Jan Breydelstadion': ('Bruges', 'Belgium'),
    'Stadion Maksimir': ('Zagreb', 'Croatia'),
    'Stadion Feijenoord': ('Rotterdam', 'Netherlands'),
    'Estadi Municipal de Montilivi': ('Girona', 'Spain'),
    'Allianz Stadium': ('Turin', 'Italy'),
    'Stade Pierre Mauroy': ('Lille', 'France'),
    'Anfield': ('Liverpool', 'England'),
    'Etihad Stadium': ('Manchester', 'England'),
    'Stade Louis II': ('Monaco', 'Monaco'),
    'Parc des Princes': ('Paris', 'France'),
    'Philips Stadion': ('Eindhoven', 'Netherlands'),
    'Red Bull Arena': ('Leipzig', 'Germany'),
    'Santiago Bernabéu': ('Madrid', 'Spain'),
    'Stadion Rajko Mitic': ('Belgrade', 'Serbia'),
    'Red Bull Arena': ('Salzburg', 'Austria'),
    'Veltins-Arena': ('Gelsenkirchen', 'Germany'),
    'Stadion Tehelne pole': ('Bratislava', 'Slovakia'),
    'epet ARENA': ('Prague', 'Czech Republic'),
    'Jose Alvalde': ('Lisbon', 'Portugal'),
    'Merkur Arena': ('Graz', 'Austria'),
    'Mercedes-Benz Arena': ('Stuttgart', 'Germany'),
    'Stade de Suisse Wankdorf': ('Bern', 'Switzerland')
}

matches_df = pd.DataFrame(columns=['date','time', 'home_team', 'away_team', 'venue'])

# list containing all the matchdays of this season that have not been played and are announced
games_days =['20241001', '20241002', '20241022', '20241023', '20241105', '20241106', '20241126', '20241127', '20241210', '20241211', '20250121', '20250122', '20250129']

import time
for date in games_days:
    url = f'https://www.cbssports.com/soccer/champions-league/schedule/{date}/'
# Scrape data
    data = scrape_match_data(url,date)
    # Convert the data to a DataFrame and append to the main DataFrame
    time.sleep(3)
    if data:
        new_matches_df = pd.DataFrame(data)
        matches_df = pd.concat([matches_df, new_matches_df], ignore_index=True)



# Create a new column with stadium details using the dictionary
matches_df['stadium_details'] = matches_df['venue'].apply(lambda x: ucl_stadiums.get(x))

# Saving the data to a csv file
matches_df.to_csv('ucl_matches.csv', index=False)


# Part 2: Creation of the Dataset for UEFA English Premier League games that have been announced and not been played yet. 

# Dictionary to help find the city in which the match is being played
stadium_to_city = {
    "American Express Community Stadium": "Brighton",
    "Anfield": "Liverpool",
    "Emirates Stadium": "London",
    "Etihad Stadium": "Manchester",
    "Goodison Park": "Liverpool",
    "King Power Stadium": "Leicester",
    "London Stadium": "London",
    "Old Trafford": "Manchester",
    "Selhurst Park": "London",
    "St. James' Park": "Newcastle upon Tyne",
    "St. Mary's Stadium": "Southampton",
    "Stamford Bridge": "London",
    "Tottenham Hotspur Stadium": "London",
    "Villa Park": "Birmingham",
    "Molineux": "Wolverhampton",
    "The City Ground": "Nottingham",
    "Craven Cottage": "London",
    "Gtech Community Stadium": "London",
    "Vitality Stadium": "Bournemouth",
    "Portman Road": "Ipswich"
}
# List that stores all the gamesdays this football season in the English Premier League
premier_league_dates = [
    "Saturday, September 28, 2024",
    "Sunday, September 29, 2024",
    "Saturday, October 5, 2024",
    "Sunday, October 6, 2024",
    "Saturday, October 19, 2024",
    "Sunday, October 20, 2024",
    "Saturday, October 26, 2024",
    "Sunday, October 27, 2024",
    "Saturday, November 2, 2024",
    "Sunday, November 3, 2024",
    "Saturday, November 9, 2024",
    "Sunday, November 10, 2024",
    "Saturday, November 23, 2024",
    "Sunday, November 24, 2024",
    "Saturday, November 30, 2024",
    "Sunday, December 1, 2024",
    "Tuesday, December 3, 2024",
    "Wednesday, December 4, 2024",
    "Saturday, December 7, 2024",
    "Sunday, December 8, 2024",
    "Saturday, December 14, 2024",
    "Sunday, December 15, 2024",
    "Saturday, December 21, 2024",
    "Sunday, December 22, 2024",
    "Thursday, December 26, 2024",
    "Saturday, December 28, 2024",
    "Sunday, December 29, 2024",
    "Saturday, January 4, 2025",
    "Tuesday, January 14, 2025",
    "Wednesday, January 15, 2025",
    "Saturday, January 18, 2025",
    "Sunday, January 19, 2025",
    "Saturday, January 25, 2025",
    "Sunday, January 26, 2025",
    "Saturday, February 1, 2025",
    "Sunday, February 2, 2025",
    "Saturday, February 8, 2025",
    "Sunday, February 9, 2025",
    "Saturday, February 15, 2025",
    "Sunday, February 16, 2025",
    "Saturday, February 22, 2025",
    "Sunday, February 23, 2025",
    "Saturday, March 1, 2025",
    "Sunday, March 2, 2025",
    "Saturday, March 8, 2025",
    "Sunday, March 9, 2025",
    "Saturday, March 15, 2025",
    "Sunday, March 16, 2025",
    "Saturday, March 22, 2025",
    "Sunday, March 23, 2025",
    "Saturday, April 5, 2025",
    "Sunday, April 6, 2025",
    "Saturday, April 12, 2025",
    "Sunday, April 13, 2025",
    "Saturday, April 19, 2025",
    "Sunday, April 20, 2025",
    "Tuesday, April 22, 2025",
    "Wednesday, April 23, 2025",
    "Saturday, April 26, 2025",
    "Sunday, April 27, 2025",
    "Saturday, May 3, 2025",
    "Sunday, May 4, 2025",
    "Saturday, May 10, 2025",
    "Sunday, May 11, 2025",
    "Saturday, May 17, 2025",
    "Sunday, May 18, 2025",
    "Sunday, May 25, 2025"
]

# Convert dates to the format YYYYMMDD
formatted_dates = []
for date_str in premier_league_dates:
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, "%A, %B %d, %Y")
    # Format the date as YYYYMMDD
    formatted_date = date_obj.strftime("%Y%m%d")
    formatted_dates.append(formatted_date)

matches_df_pl = pd.DataFrame(columns=['date','time', 'home_team', 'away_team', 'venue'])

for date in formatted_dates:
    url = f'https://www.cbssports.com/soccer/premier-league/schedule/{date}/'
# Scrape data
    data = scrape_match_data(url,date)
    # Convert the data to a DataFrame and append to the main DataFrame
    time.sleep(3)
    if data:
        new_matches_df = pd.DataFrame(data)
        matches_df_pl = pd.concat([matches_df_pl, new_matches_df], ignore_index=True)
# Print result
    for match in data:
        print(match)

# Map venue to city using the dictionary
matches_df_pl['stadium_details'] = matches_df_pl['venue'].apply(lambda x: stadium_to_city.get(x, ''))

# Save to CSV
matches_df_pl.to_csv('pl_matches.csv', index=False)
