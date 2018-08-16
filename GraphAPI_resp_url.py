# Python 3.4
# -*- coding: utf-8 -*-
# OS: OS 10
# IDE: Sublime Text

import requests
import json
import pandas as pd
# import csv

url = 'https://graph.facebook.com/v2.10/%201759525920983198?fields=posts&access_token='
response = requests.get(url)
html = json.loads(response.text)
print(type(html))
post1 = html['posts']['data'][2]['message']
post2 = html['posts']['data'][3]['message']
post3 = html['posts']['data'][4]['message']
print(type(post1))
print(post1)

# post1_df = pd.DataFrame.from_dict(data = post1)
# post2_df = pd.DataFrame.from_dict(data = post2)
# post3_df = pd.DataFrame.from_dict(data = post3)

# post1_df = post1_df.set_index('created_time')

