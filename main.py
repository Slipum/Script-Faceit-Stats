import os
import requests


def main():
    c = str(input('Enter faceit username: '))
    response = requests.get(
        'https://www.faceit.com/api/users/v1/nicknames/' + c)

    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()  # Преобразуем ответ в JSON
        new_res = requests.get('https://www.faceit.com/api/stats/v1/stats/time/users/' +
                               data['payload']['id'] + '/games/cs2?game_mode=5v5')
        if new_res.status_code == 200:
            new_data = new_res.json()
            i6 = c2 = c3 = c4 = 0
            for item in new_data:
                i6 += int(item['i6'])
                c2 += float(item['c2'])
                c3 += float(item['c3'])
                c4 += int(item['c4'])
            avg = i6 / 100
            kd = c2 / 100
            kr = c3 / 100
            hs = c4 / 100

            os.system('cls' if os.name == 'nt' else 'clear')

            print(c)
            print('elo:', data['payload']['games']['cs2']['faceit_elo'])
            print('lvl:', data['payload']['games']['cs2']['skill_level'])
            print('avg:', avg)
            print('k/d:', '%.2f' % (kd))
            print('k/r:', '%.2f' % (kr))
            print('hs:', hs)
        else:
            print(f"Ошибка при получении статистики: {new_res.status_code}")
    else:
        print(f"Ошибка: {response.status_code}")

    # Добавляем выбор между выходом и повторным исполнением
    choice = input(
        "\nChoose an action:\n1. Exit the application\n2. Get statistics\nYour choice: ")
    if choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


if __name__ == "__main__":
    main()
