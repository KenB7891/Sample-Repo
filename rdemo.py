import requests

# Downloads and saves image in local directory
r = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png', 'wb') as f:
    f.write(r.content)


# Check website status
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.status_code)
print(r.ok)
print(r.headers)


# GET example
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
print(r.url)


# POST example
payload = {'username': 'Ken', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()
print(r.text)
print(r.json())
print(r_dict['form'])


# AUTH example
r = requests.get('http://httpbin.org/basic-auth/ken/testing',
                 auth=('ken', 'testing'))
print(r.text)
print(r)


# Timeout Example
r = requests.get('http://httpbin.org/delay/1', timeout=3)

print(r)
