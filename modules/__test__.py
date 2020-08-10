from AES import AES256


password = 'yanpeizhi'

aes256 = AES256(password) # create AES256 object

msg = 'hello world!!!\nfrom yanpeizhi'


encrypted = aes256.encrypt(msg)

print(aes256.decrypt(encrypted))