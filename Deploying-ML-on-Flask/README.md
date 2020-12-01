1. run our API `predict.py`
2. With our API running execute the code to call it.
```python
import requests

data = {"area": 3300}
response = requests.post("http://127.0.0.1:5000/", json =data )
print("Price of the house should be "+ str(response.json()))
```
the output on our terminal is
```python
Price of the house should be [[647429.9937772247]]
```