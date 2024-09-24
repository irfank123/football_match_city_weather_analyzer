# ETHICS.md

## Ethical Considerations for Soccer Match Scraper and Weather Forecast Project

This project has been developed with attention to key ethical considerations related to data collection, usage, and privacy. Below is a detailed discussion of how these issues have been addressed:

### 1. **Purpose of Data Collection**

The primary purpose of this project is to gather soccer match schedules from publicly available websites (CBS Sports) and augment the data with weather forecasts. The dataset is intended to provide insights for educational, research, and non-commercial purposes, including sports analysis, weather correlation studies, and fan engagement.

- **Why are we collecting this data?**  
  The data is collected to create a unique dataset that combines match schedules with weather forecasts. This dataset provides added value to users by presenting soccer fans, analysts, and researchers with a comprehensive overview of upcoming games and predicted weather conditions. By integrating weather data, users can explore trends in how weather may impact match outcomes and fan experience.

### 2. **Data Sources and Robots.txt Compliance**

The project scrapes match data from the CBS Sports website, a publicly accessible platform that provides sports schedules and information. **Robots.txt** files of the target sites are respected to ensure the scraper operates within ethical and legal bounds.

- **CBS Sports (https://www.cbssports.com/robots.txt)**: The scraper has been designed to follow the rules defined in the `robots.txt` file. The CBS Sports website does not explicitly disallow scraping of match schedules for non-commercial purposes, which aligns with the project's usage.
  
- **WeatherAPI**: Weather data is collected through a legitimate API (WeatherAPI), which requires the use of an API key. Users must obtain their own API key and agree to WeatherAPI's terms of service.

### 3. **Collection Practices**

The web scraper has been built with responsible data collection practices in mind:

- **Rate Limiting**: To minimize any potential strain on the CBS Sports website, the scraper includes `time.sleep()` calls to introduce delays between requests. This prevents overwhelming the server with rapid-fire requests and ensures that the site is accessed in a non-disruptive manner.
  
- **Avoiding Password-Protected Content**: The scraper only targets publicly available match schedules. It does **not** attempt to access or bypass any password-protected pages, paywalls, or private content.

### 4. **Data Handling and Privacy**

The project takes special care to avoid collecting any Personally Identifiable Information (PII) or private user data. The project only scrapes **public** sports data (match schedules) and **public** weather forecasts (via WeatherAPI).

- **PII**: No user data or personal information is collected at any point during the scraping process.
  
- **Secure Data Storage**: The data collected is stored in CSV files, which do not contain sensitive information. However, it is recommended that API keys (such as the WeatherAPI key) are **not stored in public repositories**. API keys should be added to `.gitignore` to prevent them from being exposed to the public. Any files containing sensitive information, such as `config.py` or `settings.py`, should also be excluded from version control.

### 5. **Data Usage**

The data collected is strictly intended for **educational and research purposes**. This project does not use the data for commercial purposes, and no data collected by this project is sold or shared with third parties. Users of this dataset should also adhere to these principles and ensure that data is not misused for commercial exploitation.

- **Educational Use Only**: This project aims to support sports analytics, weather-related studies, and fan engagement by providing an informative and accessible dataset. Users are encouraged to use the data to enhance their understanding of how weather might affect soccer games but should refrain from using the data for betting purposes or other commercial interests.
  
- **No Redistribution**: The collected data should not be redistributed without proper attribution to the original sources (CBS Sports and WeatherAPI).

---

### Conclusion

In summary, this project was developed with a clear commitment to ethical practices in data collection and usage. The project respects the terms of service of all data sources, ensures responsible scraping practices, and safeguards user privacy by avoiding the collection of any sensitive information. The dataset produced is intended solely for educational and research purposes, and users are encouraged to follow similar ethical standards when utilizing this data.