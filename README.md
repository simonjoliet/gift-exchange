# gift-exchange
This code performs a gift exchange within a family while taking into account their gift-giving history and the fact that couples cannot give to each other. The algorithm runs for a specified number of years, and the gift history is saved to a CSV file.

# Inputs
persons.json: a JSON file containing a list of all individuals participating in the gift exchange and a dictionary of couples (optional)
history.csv: a CSV file containing the gift exchange history for previous years (optional)

#Outputs
gift_exchange.csv: a CSV file containing the gift exchange history for all years

#How to Use
1. Ensure that persons.json and history.csv files are in the data folder in the same directory as the Python code.
2. Run the Python code.
3. The program will create a gift_exchange.csv file in the data folder containing the gift exchange history for all years.

#Program Overview
1. Load the list of individuals participating in the gift exchange and couples dictionary from the persons.json file.
2. Load the gift exchange history from the history.csv file.
3. Run the gift exchange program for 30 years, with a maximum gift history of 7 years.
4. Save the gift exchange history to a gift_exchange.csv file in the data folder.

# Functionality
`run_gift_exchange`
This function takes in three arguments:

1. persons: a list of all individuals participating in the gift exchange
2. couples: a dictionary of couples (optional)
3. history: a dictionary containing the gift exchange history for previous years (optional)
The function returns a dictionary containing the gift exchange results for the current year.

`shuffle`
This variable contains the results of run_gift_exchange function.

`history`
This variable contains a dictionary containing the gift exchange history for all years.

`YEARS_ROLL`
This constant variable determines the number of years to run the gift exchange program.

`MAX_GIFT_HISTORY_YEARS`
This constant variable determines the maximum number of years a person cannot receive a gift from the same giver.
