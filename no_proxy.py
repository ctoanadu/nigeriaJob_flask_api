import requests
session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5://localhost:9150' #9150 for browser; 9050 for TOR service
session.proxies['https'] = 'socks5://localhost:9150'