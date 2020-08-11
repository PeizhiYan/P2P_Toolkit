from AES import AES256
import mainView

password = 'yanpeizhi'
aes256 = AES256(password) # create AES256 object
msg = 'hello world!!!\nfrom yanpeizhi'
encrypted = aes256.encrypt(msg)
print(aes256.decrypt(encrypted))


#mainView.start()


import hostView
hv = hostView.View()
