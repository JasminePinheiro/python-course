import requests as req

BASE_URL = 'https://api.exchangeratesapi.io/v1/'
KEY = '6e724f76ea7a28eaa84ebea663caf6d5'

def get_symbols_supported():
    params = {
        "access_key": KEY
    }
    response = req.get(BASE_URL + 'symbols', params=params)
    data = response.json()
    return data['symbols']

def get_exchange_rate(base,  symbols):
    params = {
        "access_key": KEY,
        "base": base,
        "symbols": ','.join(symbols)
    }
    response = req.get(BASE_URL + 'latest', params=params)
    data = response.json()
    return data['rates']

list_rate = ["AED", "AFN", "ALL"]

print(get_exchange_rate('EUR', list_rate))

# def max_variables():
#     return 
    # return max(len(get_symbols_supported()), len(list_rate))


# print(max_variables())


def get_max_rates(base, symbols):
    params = {
        "access_key": KEY,
        # "base": base,
        # "symbols": ','.join(symbols),
        "start_date": 2024-10-18,
        "end_date": 2024-10-25
    }
    response = req.get(BASE_URL + 'timeseries', params=params)
    data = response.json()
    return data['timeseries']

print(get_max_rates('EUR', list_rate))

print(get_max_rates())
