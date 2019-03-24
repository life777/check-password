import requests
import sys
from os import linesep
from hashlib import sha1

def request_passwords(hash_start):
    try:
        req = requests.get(f"https://api.pwnedpasswords.com/range/{hash_start}")

        if req.ok:
            return req.text
    except:
        print("Can't get request from server, check connection")

    return ""

def match_hash(hash, list_of_hashes):
    hashs_list = hashes.split(linesep)
    matched = next(filter(lambda hash: hash.find(rest) != -1, hashs_list), None)

    if matched == None:
        return None
    
    hash_parts = matched.strip().split(":")

    if len(hash_parts) < 2
        return None
    
    return hash_parts[1]


def check_password(password):
    hash_start = password[:5]
    rest = password[5:]
    
    list_of_hashes = request_passwords(hash_start).split(linesep)
    times = match_hash(rest, list_of_hashes)

    if times != None:
        print(f"Your password compromised {times} times")
    else:
        print(f"it's ok to use it")

if __name__ == "__main__":
    args = sys.argv

    if len(args) >= 2 and len(args[1]) > 0:
        sha_hash = sha1(args[1].encode()).hexdigest().upper()
        check_password(sha_hash)
    else:
        print("Enter password that you want to check")
else:
    print("This tool doesn't work as module")