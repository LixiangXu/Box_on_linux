from boxsdk import OAuth2, Client
import os

access_token = None
refresh_token = None
def store_tokens(access, refresh):
	access_token = access
	refresh_token = refresh

client_id = os.environ['box_client_id'] # put your box client id here if not using environment variable
client_secret = os.environ['box_client_secret'] # put your box client secret here if not using environment variable

oauth = OAuth2(client_id=client_id,
			client_secret=client_secret)
auth_url, csrf_token = oauth.get_authorization_url('http://localhost:4684') # make sure the port number is same as the one when you set up box app redirect URI
print("here is the url: ", auth_url)
print("open the link above, grant access, run local http server with: python3 -m http.server 4684")
code = input("input the code: ")
access_token, refresh_token = oauth.authenticate(code)
print("access token: ", access_token)
print("refresh token: ", refresh_token)
print("type: oauth.refresh(oauth.access_token) to refresh tokens")
with open('boxtoken.txt', 'w') as f:
	f.write("access token: " + access_token)
	f.write("refresh token: " + refresh_token)

client = Client(oauth)
