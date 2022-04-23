https://www.geeksforgeeks.org/how-to-create-a-programming-language-using-python/
import json
import requests
import re
import bs4
lisf = ['wgalileec70',
 'wgalileec100',
 'wgalileec64',
 'wgalileec29',
 'wgalileec28',
 'wgalileec66',
 'wgalileec61',
 'wgalileec23',
 'wgalileec20',
 'wgalileec21',
 'wgalileec27',
 'wgalileec62',
 'wgalileec63',
 'wgalileec60',
 'wgalileec65',
 'wgalileec67',
 'wgalileec26',
 'wgalileec24',
 'wgalileec25',
 'wgalileec22',
 'wgalileec58',
 'wgalileec59',
 'wgalileec54',
 'wgalileec55',
 'wgalileec56',
 'wgalileec57',
 'wgalileec50',
 'wgalileec51',
 'wgalileec52',
 'wgalileec53',
 'wgalileec38',
 'wgalileec39',
 'wgalileec30',
 'wgalileec33',
 'wgalileec32',
 'wgalileec35',
 'wgalileec34',
 'wgalileec19',
 'wgalileec36',
 'wgalileec47']
for i in lisf:
    try:
            headers = {
            "x-csrftoken": "a",
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchcsrftoken=a;scratchlanguage=ru;",
            "referer": "https://scratch.mit.edu",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
        }
            data = json.dumps({"username": i, "password": "123456"})

            request = requests.post(
            "https://scratch.mit.edu/login/", data=data, headers=headers
        )
            session_id = re.search('"(.*)"', request.headers["Set-Cookie"]).group()
            token = request.json()[0]["token"]


            headers = {
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchlanguage=en;permissions=%7B%7D;scratchsessionsid="+session_id+";",
            "referer": "https://scratch.mit.edu",

        }
            URL = 'https://scratch.mit.edu/accounts/password_change/'
            request = requests.get("https://scratch.mit.edu/csrf_token/", headers=headers)

            csrf_token = re.search(
            "scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]
            ).group(1)

            headers["referer"] = URL
            headers["Cookie"] = headers["Cookie"]+"scratchcsrftoken="+'"'+csrf_token+'"'+";"
            # Retrieve the CSRF token first
            login_data = {"old_password":"123456","new_password1":"kajmyfriend228", "new_password2":"kajmyfriend228", "csrfmiddlewaretoken":csrf_token}
            print(headers)
            r = requests.post(URL, data=login_data, headers=headers)
            print(r)
    except: pass
