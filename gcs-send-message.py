# google space web-hook 을 이용해 message 보내기

import httplib2
import json
import argparse


def send(
    target_web_hook_url: str,
    message: str
):
    """
    google space web-hook 을 이용한 단순 메시지 전송
    """
    web = httplib2.Http()
    headers = {
        'Content-Type': 'application/json; characterset=UTF-8'
    }
    body = {
        'text': message
    }
    web.request(
        uri=target_web_hook_url,
        method='POST',
        headers=headers,
        body=json.dumps(body),
    )

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog=f'{__file__}',
        description=f'sending simple texr message to google space',
        epilog=f'string input always must be quoted by \''
    )
    parser.add_argument('webhook_url')
    parser.add_argument('message')

    args = parser.parse_args()
    send(args.webhook_url, args.message)
    quit(0)
