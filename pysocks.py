import requests
import sqlite3

con = sqlite3.connect('onions.db')
con.row_factory = sqlite3.Row
db = con.cursor()
onions = db.execute('select address from Onions')

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

rows = onions.fetchall()
for row in rows:
  ping = requests.get(url=row[0],proxies=proxies)
  print(ping.status_code)