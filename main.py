import os
import requests
import questionary

os.system('cls' if os.name == 'nt' else 'clear')


def player(username, k=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    response = requests.get(
        'https://www.faceit.com/api/users/v1/nicknames/' + username)

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

            res = f"Statistic {username}'s \n\n" \
                f"{'elo:':<20} {data['payload']['games']['cs2']['faceit_elo']}\n" \
                  f"{'lvl:':<20} {data['payload']['games']['cs2']['skill_level']}\n" \
                f"{'avg:':<20} {avg}\n" \
                f"{'k/d:':<20} {kd:<20.2f}\n" \
                f"{'k/r:':<20} {kr:<20.2f}\n" \
                f"{'hs:':<20} {hs}"

            if k == 1:
                return {
                    'username': username,
                    'elo': data['payload']['games']['cs2']['faceit_elo'],
                    'lvl': data['payload']['games']['cs2']['skill_level'],
                    'avg': avg,
                    'kd': kd,
                    'kr': kr,
                    'hs': hs
                }
            else:
                return res

        else:
            questionary.press_any_key_to_continue().ask()
            return f"Error when retrieving statistics: {new_res.status_code}"
    else:
        questionary.press_any_key_to_continue().ask()
        return f"Error: {response.status_code}"


def compare_players():
    os.system('cls' if os.name == 'nt' else 'clear')
    player1 = str(input('Enter first faceit username: '))
    player2 = str(input('Enter second faceit username: '))

    stats1 = player(player1, 1)
    stats2 = player(player2, 1)

    if isinstance(stats1, dict) and isinstance(stats2, dict):
        comparison = f"Comparison between {player1} and {player2}:\n\n" \
            f"{'username:':<20} {player1:<20} {player2}\n" \
            f"{'elo:':<20} {stats1['elo']:<20} {stats2['elo']}\n" \
            f"{'lvl:':<20} {stats1['lvl']:<20} {stats2['lvl']}\n" \
            f"{'avg:':<20} {stats1['avg']:<20} {stats2['avg']}\n" \
            f"{'k/d:':<20} {stats1['kd']:<20.2f} {stats2['kd']:<20.2f}\n" \
            f"{'k/r:':<20} {stats1['kr']:<20.2f} {stats2['kr']:<20.2f}\n" \
            f"{'hs:':<20} {stats1['hs']:<20} {stats2['hs']}"
        return comparison
    else:
        return "Error retrieving player statistics."


def main():
    while True:
        answer = questionary.select(
            "Choose an action:",
            choices=[
                "Get a player's stats",
                "Compare two players stats",
                "Exit the application"
            ]
        ).ask()

        if answer == "Get a player's stats":
            username = str(input('Enter faceit username: '))
            print(player(username, 0))
        elif answer == "Compare two players stats":
            print(compare_players())
        else:
            break


if __name__ == "__main__":
    main()
