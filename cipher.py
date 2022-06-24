# user input of string to encode and offset to be used for cipher encodint
def cCipher(user_string,offset1):
    if type(user_string) != str:
        print("The input is not a string")
        return
    offset = int(offset1)
    mod_string = ""  # declaring a null string to store coded characters.
#       core logic for function cCipher
#       each character of input string is converted to UNICODE 
#       and incremented by user defined offset.
#       chr built in function used to convert UNICODE of modified/coded charater.
#       The Modified character are added to the null string variable 'mod_string'
#
    for i in range(len(user_string)):
        mod_string = chr(ord(user_string[i])+offset) + mod_string
#       since the characters are stored in reverse order printing from last to first character 
#       for desired result        
    print(mod_string[-1::-1])    
    
# Test cases for the Spring board project
(cCipher('abc', 1))
(cCipher('123', 3))
(cCipher('143Hg!)>#', 2))
(cCipher("Here's 2 U MRS Robinson", 1)) 
(cCipher(44, 3))
