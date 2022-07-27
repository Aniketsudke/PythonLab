import pandas as pd

social = pd.Series(['Whatsapp', 'Facebook' , 'Instagram', 'Snapchat', 'Twitter', 'Telegram'])

print("Pandas Series and type")
print(social)

print("Convert Pandas Series to Python list")
print(social.tolist())
print(type(social.tolist()))