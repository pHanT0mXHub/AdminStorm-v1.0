import sys
import os
import socket
import httplib

if sys.platform == "linux" or sys.platform == "linux2":
    cl = "clear"
else:
    cl = "cls"
os.system(cl)

def banner():
    
    print "\t\t*********************************************"
    print "\t\t*                                           *"
    print "\t\t*   AdminStorm v1.0 coded by: pHaNtOm_X     *"                                       
    print "\t\t*                                           *"
    print "\t\t*      Usage: ./AdminStorm.py <site>        *"
    print "\t\t*                                           *"
    print "\t\t*********************************************"
    
if len(sys.argv) < 2:
    banner()
    print "\n[-] No site selected!"
else:

    try:
        banner()
        val = 0
        
        #Filter for: "http://","https://" and "/"
        tar = sys.argv[1]
        tar = tar.replace("http://" , "")
        tar = tar.replace("https://" , "")
        tar = tar.replace("/" , "")

        #...                    
        print "\n[!] Site:",tar
        
        #Site source goes here
        source = raw_input("\n[+] Enter site source(e.g:.asp):")
        
        #Load file for bruteforce
        pages = open("admins.txt" , "r")
        pages = pages.readlines()

        print "\n[+]", len(pages) , "admin panles loaded ..."
        #Just a little check...
        if len(source) < 3:
            print "\n[!] Invalid source..."
            sys.exit(1)
            
        #Let's roll    
        else:
            print "\n[+] Scanning started..."
            print "-" * 60
            for admin in pages:
                admin = admin.replace("\n","")
                admin = admin.replace(".%EXT%",source)
                admin = "/" + admin
                conn = httplib.HTTPConnection(tar)
                conn.request("GET",admin)
                resp = conn.getresponse()
                resp.read
                
                if resp.status == 200:
                    print "\n[!] Admin page found: " , tar+admin
                    val = val + 1
                    print "\n[+]" , val ,"admin pages found"
                    
                    
    except(httplib.HTTPResponse , socket.error):
        print "\n[-] Connection error!"
    except IOError:
        print "\n[-] Can't open file"
    except KeyboardInterrupt:
        print "\n[+] Interrupted by user!"
