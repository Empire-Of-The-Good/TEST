import requests

def dow(name, link):
    #downoload ico for app
    try:
        response = requests.get(url=link)
        with open(name, 'wb') as file:
            file.write(response.content)
            file.close()
    except:
        return f'Sorry happen error\nStatus INTERNET: False'

print('Hello, world!')
a = input('Your nick&: ')
print(f'Hello, {a}!')
dow(input('Name file with extension for example: Myphoto.png\n', input('Link to download file:\n')))