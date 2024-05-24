# Weather Dashboard

#### Video Demo: [Insert URL Here]

#### Description:
Weather Dashboard is a web application that allows users to check the current weather conditions for a specified city. The application retrieves real-time weather data using the OpenWeatherMap API and provides users with information such as temperature, weather description, and an icon representing the current weather.

## Features
- **City Search:** Users can enter the name of a city and receive up-to-date weather information.
- **Temperature Unit:** The application displays temperature in Celsius by default, but users can choose to view it in Fahrenheit.
- **Weather Icon:** A visual representation of the current weather conditions is provided.

## Installation
1. Clone the repository: `git clone https://github.com/saugatpe9/weather-dashboard.git`
2. Navigate to the project directory: `cd weather-dashboard`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`

## Usage
1. Open your web browser and go to `http://localhost:5000/`.
2. Enter the name of the city you want to check the weather for.
3. Click the "Get Weather" button to see the current weather conditions.

## Project Structure
- **app.py:** The main Flask application file.
- **templates/:** HTML templates for rendering pages.
- **static/:** Static files (CSS, images, etc.).
- **requirements.txt:** Dependencies required for the project.

## Design Choices
- **Flask:** Chosen as the web framework for its simplicity and flexibility.
- **OpenWeatherMap API:** Used for real-time weather data due to its comprehensive coverage.

## Future Improvements
- Add a multi-day forecast feature.
- Implement user authentication for personalized experiences.

Feel free to explore the code and contribute to the project!

