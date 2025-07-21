import requests
import json

# Test the lesson endpoint
print("Testing lesson endpoint...")
response = requests.get("http://localhost:8000/lesson/pythagorean-theorem")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("✅ Lesson endpoint works!")
else:
    print(f"❌ Lesson endpoint failed: {response.text}")

# Test the execute_step endpoint
print("\nTesting execute_step endpoint...")
response = requests.post(
    "http://localhost:8000/lesson/pythagorean-theorem/execute_step",
    json={"step_index": 0},
    headers={"Content-Type": "application/json"}
)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("✅ Execute step endpoint works!")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
else:
    print(f"❌ Execute step endpoint failed: {response.text}") 