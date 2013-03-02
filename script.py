# SIEVE CHALLENGE
# Gabriel Vieira

from price import Price
import requests

BASE_URL = 'http://hughes.sieve.com.br:9090/'

LEVEL_PATHS = range(1, 5) + ['5%2525']

USER_AGENTS = {
  'Chrome': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
  'Opera': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
  'Internet Explorer': 'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
  'Firefox': 'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
  'Safari': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
  'Android': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
  'BlackBerry': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+',
  'Windows Phone': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)' }

HEADERS = { 
  'Host': 'hughes.sieve.com.br:9090',
  'User-Agent': USER_AGENTS['Firefox'],
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'pt-br,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate',
  'Connection': 'keep-alive'}
  
COOKIES = {'d53db4de415c4e858dc761595623a898':'+', '18':'+', 'cade-meu-cookie': '"esta aqui"'}

def send_request(path, method='GET', headers=HEADERS, cookies=COOKIES):
  return requests.__getattribute__(method.lower())(path, headers=headers, cookies=cookies)

def run_level(n):
  level_path = 'level' + str(LEVEL_PATHS[n])
  response_text = send_request(BASE_URL + level_path).text
  price = Price.parse(response_text)
  print "NIVEL {!s}: {}\nTexto: {}\nPreco: R${}\n\n".format(n+1, BASE_URL + level_path, response_text, price)

# Script starts here:

print "DESAFIO SIEVE - Gabriel Vieira\n"

for n in range(0, 5):
  run_level(n)
