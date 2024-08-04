# https://gist.github.com/nullpos/d6a10e1f4b1f906d8b6d
# そもそもhttp://e.mjv.jp/0/log/archived.cgi?"が死んでいるので、

import gzip
import os

# -*- coding: utf-8 -*-
import re

# import urllib
import urllib.request

archive_url = "http://e.mjv.jp/0/log/archived.cgi?"
plain_url = "http://e.mjv.jp/0/log/plainfiles.cgi?"


def gz(filename):
    """Gzipファイルに変換して元のファイルを削除する."""
    f_in = open("./log/" + filename + ".xml", "rb")
    f_out = gzip.open("./log/" + filename + ".mjlog", "wb")
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
    os.remove("./log/" + filename + ".xml")
    return


def download():
    """ログファイルをダウンロードする."""
    f_url = open("urls.txt")
    for row in f_url:
        urlidand = re.sub(r".*log\=(.*)\n", r"\1", row)
        urlid = re.sub(r"(.*)&.*", r"\1", urlidand)
        f_in = open("./log/" + urlidand + ".xml", "w")
        text = urllib.request.urlopen(archive_url + urlid).read()

        if len(text) < 10:
            text = urllib.request.urlopen(plain_url + urlid).read()
        f_in.write(text)
        f_in.close()
        print(urlidand)
        gz(urlidand)
    f_url.close()
    return


if __name__ == "__main__":
    download()
