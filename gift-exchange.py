import random
import pandas as pd
import json
import csv

YEARS_ROLL = 30
MAX_GIFT_HISTORY_YEARS = 7

def run_gift_exchange(persons: list, couples: dict, history: list):

    receivers = {person: [] for person in persons}
    current_year = max(history.keys())

    max_lookback = min(current_year - min(history.keys()), MAX_GIFT_HISTORY_YEARS)

    past_gift_years = range(current_year, current_year - max_lookback, -1)

    for giver in persons:

        while not receivers[giver]:
            
            prior_years_receivers = [history[past_year][giver] for past_year in past_gift_years if giver in history[past_year]]

            potential_receivers = [person for person in persons if person != giver 
                                   and person not in list(receivers.values())
                                   and person != couples.get(giver)
                                   and person not in prior_years_receivers]

            if not potential_receivers:
                return 0
            
            receivers[giver] = random.choice(potential_receivers)

    return receivers

# Open the JSON file in read mode
with open('data/persons.json', 'r') as jsonfile:
    # Load the data from the JSON file into a dictionary
    data = json.load(jsonfile)

# Extract the couples dictionary and persons set from the data dictionary
couples = data['couples']
persons = set(data['persons'])

history = {}

# Load the history dataset
with open('data/history.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row['Year'])
        giver = row['Giver']
        receiver = row['Receiver']
        if year not in history:
            history[year] = {}
        history[year][giver] = receiver

reverse = {v: k for k, v in couples.items()}
couples.update(reverse)

for _ in range(1,YEARS_ROLL):
    
    shuffle = run_gift_exchange(persons, couples, history)

    while shuffle == 0:
        shuffle = run_gift_exchange(persons, couples, history)

    history[max(history.keys()) + 1] = shuffle

try:
    pd.DataFrame(history).T.to_csv('gift_exchange.csv')
except Exception as e:
    print(f"Failed to save history to file: {e}")

