import requests

def get_exchange_rate(from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    return data['rates'][to_currency]

def currency_converter():
    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * rate

    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

currency_converter()
