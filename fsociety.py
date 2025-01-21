import sys
import getpass
import time 

credentials = {
    "mr_robot":"i am a bug",
    "darlene":"let go",
    "eliot":"i am lonely",
}

entry = False

def login():
    defined = False
    usr_name = input("Enter Username: ")
    pswrd = getpass.getpass("Enter Password: ")
    if usr_name in credentials and credentials[usr_name] == pswrd:
        defined = True
        print()
        print(f"Welcome {usr_name}")
        time.sleep(1.00)
    else:
        print("Not a valid Username and Password")

    if defined:
        return True
    else:
        return False

entry = login()

if entry:
    #this loading_bar is made by chatgpt so...i dont get credit for it.
    def loading_bar(total, prefix='Doing Job,Please wait.', suffix='Complete', length=50, fill='█'):
      for i in range(total + 1):
          percent = ("{0:.1f}").format(100 * (i / float(total)))
          filled_length = int(length * i // total)
          bar = fill * filled_length + '-' * (length - filled_length)
          sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
          sys.stdout.flush()
          time.sleep(0.1) 
      print() 
      print("Done!")

    loading_bar(100)
    print()
    time.sleep(5.00)

    print("|-----------------------------------------------------------|")
    print("                      | WELCOME   TO |                       ")
    print()
    print('''

   .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `XER0'
    
    ''')

    print("What would you like to do?")
    print('''
    1.Check for RootKit in the Root partition of system.
    2.Connect to Allsafe Server(cs30).
    3.Hack Nasa.
    ''')
    hk_cmd = input("Enter S.Number: ")

    if hk_cmd == "1":
        hunt = input("Would you like to Run the modified version of RKhunter?(y/n)")
        if hunt == "y":
            print("Executing Huntdown,please wait.")
            time.sleep(0.5)
            loading_bar(100)
            time.sleep(1.00)
            print()
            print("Searching through file system for potential threats...")
            time.sleep(3.00)
            print("Finishing up...")
            time.sleep(3.00)
            print("Huntdown Complete,Nothing was found.")
            time.sleep(1.00)
            print("Exting script...")
            time.sleep(5.00)

        else:
            print("Aborted.")

    elif hk_cmd == "2":
        print("Connecting to cs30...")
        loading_bar(100)
        time.sleep(0.5)
        print("Caution!Honey-pot detected,disconnecting from server...")
        time.sleep(2.00)
        print("Success,exiting script.")
        time.sleep(3.00)

    elif hk_cmd == "3":
        print('Bro,Are you Dumb? Even a 5 year old can hack NASA,Do it yourself :D')
        
    else:
        print("Enter Valid Input.")
else:
    print("Access denied")
    
