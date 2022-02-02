import urllib
import urllib.request



try:

    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('deu certo')
else:
    print('deu ruim ')