print("""
________           .__                        _________.__            ____  .__      
\______ \  _____   |  |    ____ _______      /   _____/|__|  ____    / ___\ |  |__   
 |    |  \ \__  \  |  |  _/ __ \\_  __ \     \_____  \ |  | /    \  / /_/  >|  |  \  
 |    `   \ / __ \_|  |__\  ___/ |  | \/     /        \|  ||   |  \ \___  / |   Y  \ 
/_______  /(____  /|____/ \___  >|__|       /_______  /|__||___|  //_____/  |___|  / 
        \/      \/            \/                    \/          \/               \/  
                                                                                     """)
with open("code1.txt","r") as c:  #command to open a file
    lines=c.readlines()
    for line in lines:
        l=line.split(" ")
        print(f" ip address: {l[0]}\n date and time: {l[3]}\n Time zone: {l[4]}\n calling data from server: {l[5]}\n path: {l[6]}\n protocol: {l[7]}\n status code: {l[8]}\n package size in bytes: {l[9]}\n User agent details: {l[11]}{l[12]}{l[13]}{l[14]}".replace('"',''))
