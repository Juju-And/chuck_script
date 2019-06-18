import requests
from slackclient import SlackClient


def get_jokes():
    input_text = "Jeżeli chcesz kolejny dowcip, wpisz 'next'. Aby zakończyć wpisz 'q': "
    players_choice = None

    slack_token = os.environ.get('SLACK_TOKEN')
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel="#random",
        text=input_text,
    )
    while not players_choice == "q":
        if players_choice is None:
            r = requests.get('http://api.icndb.com/jokes/random')
            total_json = r.json()
            joke = total_json['value']['joke']
            print(joke)

            players_choice = input(input_text)
            slack_token = os.environ.get('SLACK_TOKEN')
            sc = SlackClient(slack_token)
            sc.api_call(
                "chat.postMessage",
                channel="#random",
                text=joke,
            )
        elif players_choice == "next":
            r = requests.get('http://api.icndb.com/jokes/random')
            total_json = r.json()
            joke = total_json['value']['joke']
            print(joke)
            players_choice = input(input_text)
        else:
            print("Input jest nieprawidłowy")
            players_choice = input(input_text)


print(get_jokes())
