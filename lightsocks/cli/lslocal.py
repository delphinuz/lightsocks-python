import argparse


def main():
    parser = argparse.ArgumentParser(
        description='A light tunnel proxy that helps you bypass firewalls')
    parser.add_argument(
        '--version',
        action='store_true',
        default=False,
        help='show version information')

    proxy_options = parser.add_argument_group('Proxy options')

    proxy_options.add_argument(
        '-c', metavar='CONFIG', help='path to config file')
    proxy_options.add_argument(
        '-u',
        metavar='URL',
        help='url contains server address, port and password')
    proxy_options.add_argument(
        '-s', metavar='SERVER_ADDR', help='server address')
    proxy_options.add_argument(
        '-p',
        metavar='SERVER_PORT',
        type=int,
        help='server port, default: 8388',
        default=8388)
    proxy_options.add_argument(
        '-b',
        metavar='LOCAL_ADDR',
        help='local binding address, default: 127.0.0.1',
        default='127.0.0.1')
    proxy_options.add_argument(
        '-l',
        metavar='LOCAL_PORT',
        type=int,
        help='local port, default: 1080',
        default=1080)
    proxy_options.add_argument('-k', metavar='PASSWORD', help='password')

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
