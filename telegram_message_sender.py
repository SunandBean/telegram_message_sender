# Send message
import argparse
import asyncio
import telegram
import platform

async def sendMessage(token, chatid, message):
    bot = telegram.Bot(token)
    await bot.send_message(chat_id=chatid, text=message)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Telegram API Wrapper')

    # Add the required token argument
    parser.add_argument('-t','--token', type=str, required=True, help='API token')
    # Add the required chatid argument
    parser.add_argument('-i','--chatid', type=str, required=True, help='Chat ID')
    # Add the required message argument
    parser.add_argument('-m','--message', type=str, required=True, help='Message to send')

    try:
        # Parse the arguments
        args = parser.parse_args()

        # Get the token from the command line argument
        token = args.token
        chatid = args.chatid
        message = args.message

        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(sendMessage(token, chatid, message))
    except argparse.ArgumentError as e:
        # Display the error message if any required argument is missing
        parser.print_usage()
        print(e)