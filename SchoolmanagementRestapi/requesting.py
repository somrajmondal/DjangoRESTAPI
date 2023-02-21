import json
import requests

# For get request
# url= "http://127.0.0.1:8000/books/2/"
# res = requests.get(url)
# data=res.json()
# print(data)

# for post request
url= "http://127.0.0.1:8000/books/2/"
data = {
    'title':'New Book two',
    'author': 'New author two',
    'published_date': '2022-02-17'
}
header = {"Content-Type":"application/json"}
# # files={"image":open('D:\SOMRAJ\DjangoRestAPI\SchoolmanagementRestapi\media\somraj.png',"rb"),
# #        "PDF": open('D:\SOMRAJ\DjangoRestAPI\SchoolmanagementRestapi\media\mypdf.pdf','rb')
# #        }
res=requests.post(url,data=json.dumps(data),headers=header)
data=res.json()
print(data)

#for delete
# url= "http://127.0.0.1:8000/books/3"
# res=requests.delete(url)
# print(res.status_code)


# For PUT request
# url = "http://127.0.0.1:8000/books/2/"
#
# data = {
#     'title':'New Book two',
#     'author': 'New author two',
#     'published_date': '2022-02-17'
# }
# header = {"Content-Type":"application/json"}
# res = requests.put(url, data=json.dumps(data), headers=header)
# print(res.json())