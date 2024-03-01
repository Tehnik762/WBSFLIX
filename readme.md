# WBSFLIX

WBSFLIX is a Streamlit-based application that allows users to explore top-rated movies, search for similar films, and receive personalized movie suggestions based on their user ID.

## Features

- Display the top 10 movies of all time.
- Search for movies and find similar films.
- Provide personalized movie suggestions based on user ID.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/WBSFLIX.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:

    ```
    streamlit run wbsflix.py
    ```

## Usage

1. After launching the application, you'll see the top 10 movies displayed.
2. Type the name of a movie in the text input box to search for similar films.
3. If you're a registered user, input your user ID to receive personalized movie suggestions.

## File Structure

- `wbsflix.py`: Main Python script containing the Streamlit application code.
- `functions.py`: Utility functions for searching movies.
- `ml-latest-small/`: Directory containing movie data and user databases.

## Dependencies

- Streamlit
- Pandas
- Joblib
- Suprise

## Data Sources

- MovieLens Latest Small Dataset: Used for movie information and user databases.
