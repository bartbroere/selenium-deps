"""

"""
import tarfile

import wget


def main():
    """

    :return:
    """
    wget.download(
        "https://github.com/mozilla/geckodriver/releases/download"
        "/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz"
    )
    wget.download(
        'https://ftp.mozilla.org/pub/firefox/releases/67.0b6/linux-x86_64/'
        'en-US/firefox-67.0b6.tar.bz2'
    )
    tarfile.open('geckodriver-v0.24.0-linux64.tar.gz').extractall()
    tarfile.open('firefox-67.0b6.tar.bz2').extractall()


if __name__ == '__main__':
    main()
