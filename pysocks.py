import requests
import sqlite3

con = sqlite3.connect('onions.db')
con.row_factory = sqlite3.Row
db = con.cursor()
onion_address = db.execute('SELECT address FROM Onions')

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

rows = onion_address.fetchall()

for row in rows:
  res = "Offline"
  try:
    ping = requests.get(url=row[0],proxies=proxies)
    res = ping.status_code
    if res == 200:
      query="UPDATE Onions SET status=?,status_nb=? WHERE address=?"
      values=('online','status1', row[0])
      db.execute(query,values)
      con.commit()
    else: 
      ping.raise_for_status()
    continue
  except:
      query="UPDATE Onions SET status=?,status_nb=? WHERE address=?"
      values=('offline','status0', row[0])
      db.execute(query,values)
      con.commit() 
  finally:
    if ping.history:
        for redirects in ping.history:
          print("Request was redirected: ", redirects.status_code, redirects.url, "Final destination: ", ping.status_code, ping.url)
    else:
        print(res)


