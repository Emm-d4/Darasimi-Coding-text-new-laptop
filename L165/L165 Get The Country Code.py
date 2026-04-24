country_code = {'India' : '0091',
                'Australia' : '0025',
                'United Kingdom' : '0044'             
}

# search dictionary for country code of United Kingdom
print("Country code for United Kingdom -")
print(country_code.get('United Kingdom', 'Not Found' ))

print()

# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))