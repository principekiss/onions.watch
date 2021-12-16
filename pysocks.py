import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
{% for onion in onions %}
  data = requests.get("{{ onion['address'] }}",proxies=proxies)
  print(data)
{% endfor %}
