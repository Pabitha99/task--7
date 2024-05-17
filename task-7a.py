import requests
def fetch_data(url):
    response=requests.get(url)
    json_data=response.json()
    return json_data    
# diplaying countries, their currencies, and currency symbols
def display_country_info(country_data):
    for country in country_data:
        country_name=country.get('name','N/A')
        currencies=country.get('currencies',{})
        # print(country_name)
        for name_of_currency,currencys in currencies.items():
            currency_name=currencys.get('name','N/A')
            currency_symbol=currencys.get('symbol','N/A')
            print(currency_name)
            print(currency_symbol)
def display_curency_info_dollar_symbol(country_data):
    for country in country_data:
        country_name=country.get('name','N/A')
        currencies=country.get('currencies',{})
        # print(country_name)
        for name_of_currency,currencys in currencies.items():
            # currency_name=currencys.get('name','N/A')
            currency_symbol=currencys.get('symbol','N/A')
            if currency_symbol=='$':
                print(country_name)
                break
def display_curency_info_euro_symbol(country_data):
    for country in country_data:
        country_name=country.get('name','N/A')
        currencies=country.get('currencies',{})
        # print(country_name)
        for name_of_currency,currencys in currencies.items():
            # currency_name=currencys.get('name','N/A')
            currency_symbol=currencys.get('symbol','N/A')
            if currency_symbol=='ē':
                print(country_name)
                break
    
url="https://restcountries.com/v3.1/all"
country_data=fetch_data(url)
display_country_info(country_data)
display_curency_info_dollar_symbol(country_data)
display_curency_info_euro_symbol(country_data)

