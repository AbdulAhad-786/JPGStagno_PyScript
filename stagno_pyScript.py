from cryptography.fernet import Fernet
import pyfiglet,os

def encryption(data):
    key=Fernet.generate_key()
    with open('key','wb') as k:
        k.write(key)
        k.close()
    enc=Fernet(key)   
    # msg=msg.encode() 
    cipher_txt=enc.encrypt(data)
    return cipher_txt

def Decryption(cipher_txt,ASE_key):
    key=ASE_key
    dec=Fernet(key)
    # cipher_txt=cipher_txt.encode()    
    plaintxt=dec.decrypt(cipher_txt)
    plaintxt=plaintxt.decode()
    return plaintxt

def encode_steg(message,path):
    curntdir=os.getcwd()
    with open(path,'a') as f:
        f.write(str(message))
        f.close()
        print(f"Your key is Stored at {curntdir}")

def decode_steg(path,k_path):
    with open(path,'rb') as f:
        data=str(f.read()).split('\\x')[-1][5:-3].encode()
    with open(k_path,'rb') as f:    
        key=f.read()
    print("-"*80)
    print(f"Your Secret Message is : {Decryption(data,key)}")
    print("+"*80+"\n") 

def main():
    print(pyfiglet.figlet_format("S t e G n o M S G", font = "digital" ))
    print("-"*50+"By Abdul Ahad")
    opt=input("Please Choose your Option \n \t I. Press E for hide your data. \n \t II. Press D for show your data. \n \t else Q for Quit from the program.\n \n \t Type Here :  ")
    if opt.lower()=='e':
        path=input("Enter your Image Path syntax(dir/dir/filename_with_extentions): ").replace(" ","").replace("'","")
        msg_Input=encryption(input("Enter your secret message : ").encode())
        encode_steg(msg_Input,path)
    elif opt.lower()=='d':
        path=input("Enter your Image Path syntax(dir/dir/filename_with_extentions): ").replace(" ","").replace("'","")
        k_path=input("Enter your key Path syntax(dir/dir/file): ").replace(" ","").replace("'","")
        decode_steg(path,k_path)
    elif opt.lower()=='q':
        exit(0)
    

if __name__=="__main__":
    main()