import requests as reqs


def send_message(bot_token, receivers, message, verbose=False):

    send_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?"

    success = True

    for receiver in receivers:

        data = {
            'chat_id': receiver,
            'parse_mode': "HTML",
            'text': message
        }

        response = reqs.post(send_message_url, data=data).json()

        if verbose:
            print(f"Message{' ' if response['ok'] else ' not '}sent to {receiver}.")

        success = success and response['ok']

    return success
