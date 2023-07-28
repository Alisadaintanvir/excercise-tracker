# Exercise Tracker using Nutritionix API and Google Sheets
#### This is a simple exercise tracker application that allows users to input their exercise details and store them in a Google Sheets spreadsheet using the Nutritionix API for exercise information retrieval.

## Setup
1. Install the required Python packages by running the following command:
   `pip install -r requirements.txt`
   
2. Create a .env file in the project directory with the following environment variables:
```
APP_ID=YOUR_NUTRITIONIX_APP_ID
API_KEY=YOUR_NUTRITIONIX_API_KEY
SHEET_AUTHORIZATION=YOUR_GOOGLE_SHEET_AUTHORIZATION_TOKEN
SHEET_ENDPOINT=YOUR_GOOGLE_SHEET_ENDPOINT_URL
```

Replace YOUR_NUTRITIONIX_APP_ID, YOUR_NUTRITIONIX_API_KEY, YOUR_GOOGLE_SHEET_AUTHORIZATION_TOKEN, and YOUR_GOOGLE_SHEET_ENDPOINT_URL with your actual credentials.

## Usage
Run the main.py script:
`python main.py`

The application will prompt you to enter the exercise you performed. After entering the exercise, the script will use the Nutritionix API to fetch exercise details and then store the exercise data in the Google Sheets spreadsheet.

## Code Overview
#### main.py
This is the main script of the application. It takes user input, interacts with the Nutritionix class to get exercise details, and then stores the data in the Google Sheets using the Sheet class.

#### nutritionix.py
This module contains the Nutritionix class, which is responsible for making requests to the Nutritionix API to get exercise information based on user input.

#### sheet.py
This module contains the Sheet class, which is used to interact with the Google Sheets API to post-exercise data to the specified spreadsheet.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
