#!/usr/bin/env python3

import time
import sqlite3
import requests
from os import path
from datetime import datetime
from watchpoints import watch

# connect to the sqlite database
# connection = sqlite3.connect("data.db")
# cursor = connection.cursor()

while True:
  uri = 'https://api.bittrex.com/v3/markets/ETH-USD/candles/MIDPOINT/DAY_1/recent'
  r = requests.get(uri)
  data = r.json()

  for i in data:
    print(i['startsAt'])
    time.sleep(1)

  # dt_startsAt = data["startsAt"]
  # dt_open = data["open"]
  # dt_high = data["high"]
  # dt_low = data["low"]
  # dt_close = data["close"]


  # cursor.execute("INSERT INTO tbl_eth_market(startsAt, open, high, low, close) values(dt_startsAt, dt_open, dt_high, dt_low, dt_close)")
  # connection.commit()
