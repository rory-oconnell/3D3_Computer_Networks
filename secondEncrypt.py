def SecondEncrypt(message):
    key = int(input('what is the numeric key?\n'))

    words = message.split(' ')
    new_string = []
    temp= ''
    for i in words:
        for j in i:
        
            num = ord(j) + key
            char = chr(num)   
            temp = temp + char
        temp = temp + ' ' # see if we wanna keep this 
    new_string.append(temp[::-1]) 

    reverse = ''.join(reversed(new_string))
    return(reverse)

def SecondDecrypt(message):
    key = int(input('what is the numeric key?\n'))
    temp2=''
    decrypt =[]
    for i in message:
        for j in i:
                if j != ' ':
                    num = ord(j) - key 
                    char = chr(num)
                    temp2 = temp2 + char 
                else:
                    temp2 = temp2 + ' '
    
    decrypt.append(temp2[::-1])  
    straight = ''.join((decrypt))
    return(straight)

message = "Hello World"
cipher = SecondEncrypt(message)
print(cipher)
decrypt = SecondDecrypt(cipher)
print(decrypt)