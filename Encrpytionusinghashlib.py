
import hashlib


"""
Available hashing algorithms in hashlib but this program is limited to some Algorithms only.  : 
sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5()
"""


str = input("Enter the string/password you want to encrypt :  ")

n = int(input("""Enter algorithm to implement on the input : 
1. SHA
2.SHA256
3.SHA512
4.BLAKE2B
5.MD5
"""))

if n==1:

    result = hashlib.sha1(str.encode())
    
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of SHA is : ")
    print(result.hexdigest())

  
elif n==2:
    result = hashlib.sha256(str.encode())
  
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of SHA256 is : ")
    print(result.hexdigest())

elif n==3:
    result = hashlib.sha512(str.encode())
  
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of SHA512 is : ")
    print(result.hexdigest())

elif n==4:
    result = hashlib.blake2b(str.encode())
  
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of BLAKE2B is : ")
    print(result.hexdigest())

else:
    result = hashlib.md5(str.encode())
  
    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of MD5 is : ")
    print(result.hexdigest())
