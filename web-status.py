import httplib2
import argparse
from typing import Optional


def get_status(
    url: str,
    timeout_seconds: Optional[int] = None,
) -> bool:
    web = httplib2.Http(
        timeout=timeout_seconds
    )
    try:
        response, content = web.request(
            uri=url,
            method='GET'
        )
        return response.status
    except:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog=f'{__file__}',
        description=f'check the web response is valid(status 20x)',
        epilog=f'string input always must be quoted by \''
    )
    parser.add_argument('url')

    args = parser.parse_args()
    status = get_status(args.url)
    if status is None:
        status = -1
    quit(status)
