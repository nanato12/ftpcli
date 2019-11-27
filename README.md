# ftpcli

[![PyPi](https://img.shields.io/pypi/v/ftpcli.svg)](https://pypi.org/project/ftpcli)
[![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/github/license/nanato12/ftpcli)](https://img.shields.io/github/license/nanato12/ftpcli)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square)](https://paypal.me/bluesquarejb/100)

FTP Client with Python

You can operate FTP like a shell.

## install

```shell
pip install ftpcli
```

## use

```python
from ftpcli import FTP

ftp = FTP(server, account, password)

ftp.pwd()
# /

ftp.ls()
# ['index.html', 'css', '.htaccess', 'test']

ftp.cd('css')
ftp.ls()
# ['style.css', 'reset.css', 'main.css']

ftp.pwd()
# /css/

ftp.mkdir('aaaa')
ftp.ls()
# ['style.css', 'reset.css', 'main.css', 'aaaa']

ftp.rm('aaaa')
ftp.ls()
# ['style.css', 'reset.css', 'main.css']

ftp.cd('../')
ftp.download('css')
# download: [Success] /css/style.css
# download: [Success] /css/reset.css
# download: [Success] /css/main.css
```
