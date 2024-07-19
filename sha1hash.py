from urllib.request import urlopen
import hashlib
from termcolor import colored

# Get the SHA1 hash value from the user
sha1hash = input("[*] Enter SHA1 Hash Value: ")

# Fetch the password list from the URL
url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt'
passlist = str(urlopen(url).read(), 'utf-8')

# Iterate over each password in the list
for password in passlist.split('\n'):
    # Generate the SHA1 hash of the password
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    
    # Check if the generated hash matches the input hash
    if hashguess == sha1hash:
        print(colored("[+] The Password is: " + str(password), 'green'))
        quit()
    else:
        print("[-] Password guess " + str(password) + " does not match, trying next...")

# If no match is found
print("[-] Password not in password list")

