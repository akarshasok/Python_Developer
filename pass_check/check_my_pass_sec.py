import requests
import hashlib
import sys
url='https://api.pwnedpasswords.com/range/'#+'password123' #always run passwords through a hash generator not plain text
url1 = 'https://api.pwnedpasswords.com/range/'+'BAB12' #first 5 digits of hash gen passwords
res1=requests.get(url1)
 #res400 means an error
def req_api_data(query_char): #takes in your password character and raises an error if it is not 200 which is not normal, otherwise returns the response
    res = requests.get(url+query_char)
    if res.status_code != 200:
        raise  RuntimeError(f'{res.status_code} error')
    return res

def get_password_leak_count(hashes,hash_to_check):   #this is to check your responses against the tail you safe keep and see if it matches.
    #if there is a match we take the count of it which means your passwords been tried by hackers.
    hashes = (line.split(":") for line in hashes.text.splitlines())  #immutable tuple #splitlines as responses are divided by lines
    for h,count in hashes:
        if h==hash_to_check:
            return count

    return 0
#kanonymity : tracks u but never know who you are. Using the first 5 characters of your hash gen
def pwned_api_check(password):    #takes in your password and hashes it. we seperate the first 5 to check and remaining safe.
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5,last=sha1password[:5],sha1password[5:]
    response = req_api_data(first5)
    #print(response.text)
    return get_password_leak_count(response,last)

def main(args):
    # for i in args:    #for a list of consecutive passwords entered in command line
    #     count = pwned_api_check(i)
    with open(args) as my_file: #we are adding passwords in a textfile for added security
        passes=my_file.read().splitlines()
        for i in passes:
            count=pwned_api_check(i)
            if count:
                print(f"{i} as part of password with {count} hacks already is a bad idea")
            else:
                print(f"{i} have a strong password")
        return "done"
if __name__ == '__main__': #protects users from accidentally invoking the script when they didn't intend to.
    # main(sys.argv[1:])
    main(sys.argv[1])




