# Requests is a simple, yet elegant, HTTP library.

import requests

# 1. Sending a GET Request
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    print("GET request successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to GET: {response.status_code}")

# 2. Sending a POST Request
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
if response.status_code == 201:
    print("POST request successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to POST: {response.status_code}")

# 3. Sending PUT Request
update_data = {
    'id': 1,
    'title': 'foo updated',
    'body': 'bar updated',
    'userId': 1
}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=update_data)
if response.status_code == 200:
    print("PUT request successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to PUT: {response.status_code}")

# 4. Sending DELETE Request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print("DELETE request successful")
else:
    print(f"Failed to DELETE: {response.status_code}")

# 5. Sending a GET Request with Parameters
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
if response.status_code == 200:
    print("GET request with parameters successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to GET with parameters: {response.status_code}")

# 6. Handling JSON Response
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    post = response.json()
    print(f"Post title: {post['title']}")
else:
    print(f"Failed to GET: {response.status_code}")

# 7. Handling HTTP Errors
response = requests.get('https://jsonplaceholder.typicode.com/invalid-url')
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

# 8. Adding Headers
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
if response.status_code == 200:
    print("GET request with headers successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to GET with headers: {response.status_code}")

# 9. Basic Authentication
response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
if response.status_code == 200:
    print("GET request with basic auth successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to GET with basic auth: {response.status_code}")

# 10. Timeout
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=0.001)
except requests.exceptions.Timeout:
    print("The request timed out")

# 11. Session Object
with requests.Session() as session:
    session.headers.update({'User-Agent': 'my-app/0.0.1'})
    response = session.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        print("GET request with session successful")
        print(response.json())  # Print the JSON response
    else:
        print(f"Failed to GET with session: {response.status_code}")

# 12. Uploading a File
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
if response.status_code == 200:
    print("File upload successful")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to upload file: {response.status_code}")

# 13. Downloading a File
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)
if response.status_code == 200:
    with open('downloaded_post.txt', 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    print(f"Failed to download file: {response.status_code}")

