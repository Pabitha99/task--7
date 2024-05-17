import requests
def brewery_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def count_and_type_breweries_by_state(brewery_data, states):
    state_breweries = {}
    for brewery in brewery_data:
        state = brewery.get('state', 'Unknown')
        if state in states:
            brewery_type = brewery.get('brewery_type', 'Unknown')
            if state not in state_breweries:
                state_breweries[state] = {brewery_type: 1}
            else:
                if brewery_type not in state_breweries[state]:
                    state_breweries[state][brewery_type] = 1
                else:
                    state_breweries[state][brewery_type] += 1
    return state_breweries

url = "https://api.openbrewerydb.org/v1/breweries"
data = brewery_data(url)  # Fetch brewery data
states_of_interest = ['Alaska', 'Maine', 'New York']
breweries_by_state = count_and_type_breweries_by_state(data, states_of_interest)

for state, breweries in breweries_by_state.items():
    print(f"State: {state}")
    for brewery_type, count in breweries.items():
        print(f"  - Type: {brewery_type}, Count: {count}")
