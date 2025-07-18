# Movie-Genre-Survey-Sorter
A Python program to collect and analyze movie genre preferences from a survey, sorting genres by popularity and alphabetically in case of ties.

## Description

This program conducts a survey to collect the favorite movie genres of participants. Each participant provides their name and three preferred genres from a predefined list: `Horror`, `Romance`, `Comedy`, `History`, `Adventure`, and `Action`. The program counts the number of preferences for each genre and outputs the genres sorted by popularity (descending order). If multiple genres have the same number of preferences, they are sorted alphabetically. Genres with zero preferences are included in the output with a count of 0.

## Features

- Accepts the number of participants as input.
- Collects each participant's name and their three favorite genres.
- Validates input genres against a predefined list.
- Counts and sorts genres by the number of preferences (descending) and alphabetically for ties.
- Outputs each genre and its preference count, including genres with zero preferences.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-genre-survey-sorter.git
   ```

2. Navigate to the project directory:
  ```bash
  cd movie-genre-survey-sorter
  ```

## Usage

1. Run the program:
  ```bash
  python genre_survey.py
  ```

2. Enter the number of participants when prompted.


3. For each participant, enter their name followed by three genres, separated by spaces (e.g.):
   ```bash
   # <orange>**hossein**</orange> Horror Romance Comedy  # Name in orange


## Example Input/Output

### Input
  ```plain
   4
   hossein Horror Romance Comedy
   mohsen Horror Action Comedy
   mina Adventure Action History
   sajjad Romance History Action
   ```
### Output
  ```plain
   Action : 3
   Comedy : 2
   History : 2
   Horror : 2
   Romance : 2
   Adventure : 1
   ```

## Code Structure

* genre_survey.py: Main script that handles input, processing, and output.

* Uses a dictionary to store participant names and their genre preferences.

* Uses another dictionary to count genre preferences.

* Sorts genres using Python's sorted() function with a custom key for descending count and alphabetical ordering.


## Notes

* The program ignores invalid genres (not in the predefined list).

* Input validation ensures at least one name and three genres are provided per participant.

* The output format strictly follows the requirement: genre : count.

