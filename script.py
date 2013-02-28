# Challenge URL: hughes.sieve.com.br:9090/level0
import requests

def print_response(r):
	print 'STATUS CODE: '; print r.status_code
	print 'TEXT: '; print r.text
	print 'HEADERS: '; print r.headers
	print 'APPARENT ENCODING: '; print r.apparent_encoding
	print 'LINKS: '; print r.links
	print 'URL: '; print r.url
	print '--- --- ---\n\n'

def send_request(url, method, h, c):
	print "Sending " + method.upper() + " request to " + url + "\n"
	r = requests.__getattribute__(method)(url, headers=h, cookies=c)
	print_response(r)

BASE_URL = "http://hughes.sieve.com.br:9090/"
urls = []

for i in range (1,6):
	urls.append(BASE_URL + "level" + str(i))

user_agents = {
        'Chrome': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
        'Opera': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Internet Explorer': 'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
        'Firefox': 'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
        'Safari': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
        'Android': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'BlackBerry': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+',
        'Windows Phone': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)' }


headers = {
	'Host': 'hughes.sieve.com.br:9090',
	'User-Agent': user_agents['Firefox'],
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'pt-br,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'keep-alive',
	'Referer': 'http://hughes.sieve.com.br:9090'}
# Note: testei com cookie versao 0 (esta%20aqui) antes e nao funcionou. Logo deve ser versao 1.
cookie = {'d53db4de415c4e858dc761595623a898':'+', '18':'+', 'cade-meu-cookie': '"esta aqui"'}

#print 'SEM HEADERS OU COOKIES' + "\n\n"
#
#for url in urls:
#	r = requests.get(url)
#	print 'URL: ' + url
#	print_response(r)
#	print "--- --- ---\n"

print 'COM HEADERS/COOKIES' + "\n\n"

for url in urls:
	r = requests.get(url, headers=headers, cookies=cookie)
	print 'URL: ' + url
	print_response(r)


#url_lvl5 = BASE_URL + "level5%2525"
print "\n\n\nLEVEL 5\n\n"
send_request(BASE_URL + "level5%2525", "get", headers, cookie)

#headers['X-Requested-With'] = 'XMLHttpRequest'
#headers['X-Forwarded-For'] = 'hughes.sieve.com.br:9090'
#send_request(url_lvl5, 'get', headers, cookie)

#for method in ["get", "head", "post", "put", "delete", "options", "patch"]:
#	send_request(url_lvl5, method, headers, cookie)

#print "\nFaking User Agents:\n\n"

#for user_agent in user_agents.keys():
#	print "Pretending to be " + user_agent + "...\n"
#	headers['User-Agent'] = user_agents[user_agent]
#	send_request(url_lvl5, "get", headers, cookie)

