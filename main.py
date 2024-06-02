import os,sys,time
import cmd

info = """
            MUSLIMHACKER COUMMUNITY
    creators : bd-haker,arman,oniyom,cipher,no rulese
    MHCbotnet v1.0
    A powerfull bot net
    fb : https://www.facebook.com/people/Muslim-hackers-community/100091591027804/
    telegram : https://t.me/M_H_C_BD
    Join our team! 
"""
print(info)
#print("\033[0;91m hi \033[0m")
bot = cmd.bot()
cmd1 = cmd.AI()
dos = cmd.get()
main = int(input("\n\nSelect number\n\n(1) start bot net\n(2) dos attack\n(3) BR313 DDOS attack (MHC_BD parsonal ddos script)\n(0) exit \n\nEnter number : "))
if main==1:
    bot1 = bot.find()
    if bot1:
        if "host" in bot1:
            print("\n\nFound command for bot net!",bot1)
            cmd1.analysis(bot1)
    else:
        print("\n\nNot found bot net start command!")
elif main==2:
    dos.cmd()
elif main==3:
    dos.cmd()
elif main==0:
    print("\n\n TNX for using our tools")
    sys.exit()

