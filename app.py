import google.generativeai as genai
while True:
 text= str(input())
 genai.configure(api_key="AIzaSyDNcp_JDchji_PfU6mKwjCz2SxGBj0a4Ow")
 model = genai.GenerativeModel("gemini-1.5-flash")
 response = model.generate_content(text)
 print(response.text)