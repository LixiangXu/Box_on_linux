from boxsdk import OAuth2, Client
import os
class BoxClient(object):
	def __init__(self):
		self.access_token = input("input the access token: ")
		self.refresh_token = input("input the refresh token: ")
		self.oauth = OAuth2(client_id=os.environ['box_client_id'],
			client_secret=os.environ['box_client_secret'],
			access_token=self.access_token,
			refresh_token=self.refresh_token)
		self.client = Client(self.oauth)

	def refresh(self):
		self.access_token, self.refresh_token = self.oauth.refresh(self.oauth.access_token)
		self.client = Client(self.oauth)
		print("access token: ", self.access_token)
		print("refresh token: ", self.refresh_token)
		return True
