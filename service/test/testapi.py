import requests
print("\n------")    
print("home")
r = requests.get("http://localhost:5000/")
print("result %s " % (r.content))

print("\n------")    
print("illegal resource")
payload = {"type": 0}
r = requests.put("http://localhost:5000/api/", json = payload)
print("result %s " % (r.content))

print("\n------")    
print("illegal type")
payload = {"type": 1}
r = requests.put("http://localhost:5000/api/V0.2/trip/start", json = payload)
print("result %s " % (r.content))

    
# 0
#
print("\n------")    
print("Test 0")
payload = {"type": 0}
r = requests.put("http://localhost:5000/api/V0.2/trip/start", json = payload)
print("result %s " % (r.content))


# 1
#
print("\n------")    
print("Test 1")
payload = {"type": 1,"data": {"time": 1497346079, "data": [{"id": 213,"value": 100.0}, {"id": 191,"value": 13.269914626196}, {"id": 2015,"value": 8.0}, {"id": 2018,"value": 51.5626308108108}, {"id": 2019,"value": 5.00934432432432}, {"id": 276, "value": 1234}]}}
r = requests.put("http://localhost:5000/api/V0.1/trip/advice/speed", json = payload)
print("result %s " % (r.content))

# 2
#
print("\n------")    
print("Test 2")
payload = {"type": 2}
r = requests.put("http://localhost:5000/api/V0.1/trip/advice/park", json = payload)
print("result %s " % (r.content))


# 2
#
print("\n------")    
print("Test 3")
payload = {"type": 3}
r = requests.put("http://localhost:5000/api/V0.1/trip/advice/charge", json = payload)
print("result %s " % (r.content))
