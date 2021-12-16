import requests
import sqlite3

con = sqlite3.connect('onions.db')
con.row_factory = sqlite3.Row
db = con.cursor()
onions = db.execute('SELECT address FROM Onions')

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

rows = onions.fetchall()
for row in rows:
  ping = requests.get(url=row[0],proxies=proxies)
  res = ping.status_code
  print(res)
  if res == 200:
    query="UPDATE Onions SET status=?,status_nb=?"
    values=(res,'status1')
    db.execute(query,values)
    con.commit()