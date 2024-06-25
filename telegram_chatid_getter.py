# Get Token
import argparse
import requests

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Telegram API Wrapper')

    # Add the token argument
    parser.add_argument('-t','--token', type=str, help='API token')
    parser.add_argument('-c', '--channel', action='store_true', help='Channel flag')

    # Parse the arguments
    args = parser.parse_args()

    # Get the token from the command line argument
    token = args.token
    channel = args.channel

    if token:
        address = f"https://api.telegram.org/bot{token}/getUpdates"

        response = requests.get(address)
        json_resp = response.json()

        if channel:
            for result in json_resp['result'][::-1]:
                if 'my_chat_member' in result:
                    chatid = result['my_chat_member']['chat']['id']
                    break
        else:
            chatid = json_resp['result'][-1]['message']['chat']['id']
        print("chat id: " + str(chatid))
    else:
        print("Please provide a token.")
    