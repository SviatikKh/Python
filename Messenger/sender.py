import requests

print("Введіть ім'я")
username = input()
print('Введіть пароль')
password = input()

while True:
    text = input()

    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'username': username, 'password': password, 'text': text}
    )
    # print(response.status_code)
    # print(response.text)
    # print(response.json())
    if response.status_code == 200:
        print('Повідомлення надіслано')
        print()