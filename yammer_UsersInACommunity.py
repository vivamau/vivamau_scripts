import requests
# go here to create a token for your app
# https://www.yammer.com/client_applications
token = "MYTOKENGOESHERE!"

# this is the community ID
groupID = "78686445568"

page = 1
pagesize = 50
endpoint = "https://www.yammer.com/api/v1/users/in_group/{}.json?page={}".format(groupID,page)
headers = {"Authorization": "Bearer " + token}

data = requests.get(endpoint, headers=headers).json()

numberofpages = data['total_count']//pagesize
count = 0
for x in range(numberofpages+1):
	# print("THIS IS PAGE {}".format(page))
	page = page + 1

	for i in data['users']:
		count = count + 1
		print(i["email"] + ";")
	endpoint = "https://www.yammer.com/api/v1/users/in_group/{}.json?page={}".format(groupID,page)
	data = requests.get(endpoint, headers=headers).json()
print ("number of users: {}".format(count))
