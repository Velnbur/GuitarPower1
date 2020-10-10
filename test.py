import requests
from tkinter import *

root = Tk()

response = requests.get('http://localhost:8000/articles/api/list')
json_response = response.json()[1]['image']

print(json_response)
root.mainloop()