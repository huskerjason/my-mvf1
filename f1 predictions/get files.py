import requests


path = r'/home/jovyan/Formula 1/data/'


url = 'https://www.formula1.com/en/results.html/2023/team.html'
response = requests.get(url)
if response.status_code == 200:
    with open(path + 'teams.html', 'wb') as f:
        f.write(response.content)
    print('Team file saved successfully.')
else:
    print(f'Team Error: {response.status_code}')


url = 'https://www.formula1.com/en/results.html/2023/drivers.html'
response = requests.get(url)
if response.status_code == 200:
    with open(path + 'drivers.html', 'wb') as f:
        f.write(response.content)
    print('Driver file saved successfully.')
else:
    print(f'Driver Error: {response.status_code}')


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS_G-12KfdrW-nYsfi8--SCdOSylVL6IVWdiJKJC1bMbb5YMNUGdZaAh04oeVbDyKHmsj_OjM_JvRUo/pub?gid=0&single=true&output=csv'
response = requests.get(url)
if response.status_code == 200:
    with open(path + 'predictions.csv', 'wb') as f:
        f.write(response.content)
    print('Predictions file saved successfully.')
else:
    print(f'Predictions Error: {response.status_code}')
