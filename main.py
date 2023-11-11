import requests
from datetime import date

TOKEN = 'sofslav22alin1902'
USER_NAME = 'via4eslav'
pixela_endpoint = 'https://pixe.la/v1/users'
DATE = date.today()
user_params = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":'yes',
    "notMinor":'yes'
}
response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'
pixel_post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graphprog"
graph_config = {
    'id':'graphprog',
    'name':'proggraph',
    'unit':'day',
    'type':'int',
    'color':'shibafu'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# DATE.strftime('%Y%m%d')
post_pixels_conf = {
    'date': '20231110',
    'quantity': input('How many lines do you write today ')
}
response = requests.post(url=graph_endpoint,json = graph_config,headers=headers)
print(response.text)


response = requests.post(url = pixel_post_endpoint,json=post_pixels_conf,headers = headers)
print(response.text)
# /v1/users/<username>/graphs/<graphID>
put_update = {
    'date':'20231110',
    'quantity':'22'
}
datee = '20231110'
response = requests.post(url=pixel_post_endpoint,json = put_update,headers=headers)
#
pixel_post_delete = f"{pixela_endpoint}/{USER_NAME}/graphs/graphprog/20231111"
response = requests.delete(url=pixel_post_delete,headers=headers)
print(response.text)