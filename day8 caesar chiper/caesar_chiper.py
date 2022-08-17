letters =list("abcdefghijklmnopqrstuvwxyz")
continue_caesar =1

def encryption_caesar_chiper (message, shift_num) :
    encrypt_message=[]
    for i in list(message):
        if i in letters:
            index = letters.index(i)+shift_num%len(letters)
            if (index > len(letters)-1):
                index= index-len(letters)
            encrypt_message.append(letters[index])
    print(str(''.join(encrypt_message)))

def decryption_caesar_chiper(message, shift_num):
    dencrypt_message=[]
    for i in list(message):
        if i in letters:
            index = letters.index(i)-shift_num%len(letters)
            if (index<0):
                index= len(letters)+index
            dencrypt_message.append(letters[index])
    print(str(''.join(dencrypt_message)))

def caesar_chiper (message, shift_num, mode) :
    result_message=[]
    if mode == "decode" :
        shift_num *= -1
    for i in list(message):
        if i in letters:
            index = (letters.index(i)+shift_num)%len(letters)
            result_message.append(letters[index])
        else: 
            result_message.append(i)
    print(str(''.join(result_message)))



while continue_caesar:
    mode = input('type "encode" to encrypt, type "decode" to decrypt\n')
    message = input("Type your message: \n")
    shift_num = input("Type your shift number:\n")
    # if mode == "encode" :
    #     encryption_caesar_chiper(message, int(shift_num))
    # if mode =="decode":
    #     decryption_caesar_chiper(message, int(shift_num))
    caesar_chiper(message,int(shift_num),mode)
    try_again = input("Do you want to continue, yes or not?\n")
    if(try_again == "yes" ) :
        continue_caesar =1
    else: 
        continue_caesar=0

