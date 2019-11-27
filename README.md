# ftpcli
FTP Client with Python

You can operate FTP like a shell.

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
