# def lastCharater(text):
#     return len(text) > 0 and text[-1] == ";"
     
# print(lastCharater("hello;"))
# Check if the string is not empty AND last character is a colon
# a code that will add space to that if its passs option 1 using elif 



def Lastcharacer(text):
    # Check if the last character is a colon
    if len(text) > 0 and text[-1] == ";":
        return text +" "  
    elif len(text) == 0:
        return text 
    else:
        return text  
print(Lastcharacer("Hellojuma;"))