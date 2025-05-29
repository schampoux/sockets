#!/home/spunion/.virtualenvs/sockets/bin/python

import urllib.request, urllib.error, urllib.parse 
from base64 import encodebytes

# Two ways to handle basic authentication. 
    # 1: handler, opener, install opener. 
    # 2: HTTP client request with auth headers. 

# NOTE: must start server on localhost before trying to ping it. 
        # > sudo python3 -m http.server 80
        # default port is 80, we don't specify this below in URL


LOGIN = 'test_user'
PASSWD = 'password'
URL = 'http://127.0.0.1' # or http://localhost
REALM = 'Secure Archive'

def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urllib.parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return(url) 

def request_version(url):
    request = urllib.request.Request(url) 
    b64str = encodebytes(
        bytes('%s:%s' % (LOGIN, PASSWD), 'utf-8'))[:-1]
    request.add_header("Authorization", "Basic %s" % b64str)
    return request

if __name__ == "__main__":
    for approach in ('handler', 'request'):
        print("********Using %s approach" % approach)
        url = eval('%s_version' % approach)(URL)
        f=urllib.request.urlopen(url)
        print(str(f.readline(), 'utf-8'))
        f.close()

