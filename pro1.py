import requests

url = "https://api.apilayer.com/number_verification/validate?number={}"

phone_number = input("Enter phone number with country code: ")

formatted_url = url.format(phone_number)

headers= {
  "apikey": "0kYa9omOS4kikjBJhfc656LWunk5UUeG"
}

response = requests.get(formatted_url, headers=headers)

status_code = response.status_code
result = response.text
print(result)
