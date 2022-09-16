"""
Coded by Dpr
https://github.com/c99tn
https://t.me/+7wraokmFiCcxOTk0
Join Our Telegram Channel For More Great Stuff //
"""
from ast import arg
import requests
import socket
import ipaddress
import smtplib
from multiprocessing.dummy import Pool as ThreadPool 
import time
from termcolor import colored
import os
import sys

socket.setdefaulttimeout(.3)
os.system('clear')
myemail = 'your@email.com'
print(colored("""\Join us .. https://t.me/+7wraokmFiCcxOTk0                              

                                   ;:     ,:;+*%%SS%*:                                    
                               ;: :S%*;+*?%SSSSS%*:,                                      
                          ,: ,:%%??S%SSSSSSSS?*;,                                         
                    ,,    ,%+?%SSSSSSSSSSSSSS%%%%??*+;:,                                  
                   ;? :*%SSSSSSSSSSSSSSSSSSSSSSSSS%%?*;:,,                                
                   ?; ,,%SSSSSSSSS?:;+*?SS?**?S*;:,,                                      
                  :? +%%SS%SSSSSS%:     :+?*;,;**;,                                       
                  *+ %SSS?,;?%?++*:        :+**;;+?*:                                     
                 ,?, ;SS??  ;*   ,?,          :;+++???*+;::                    
                 ++ :%%:,?  :?    ;*                 ,;??+:,,,,                     
                ,?;;*?* ,?  ,?,    +*                   ,+**;,,                           
                ;?:+*:+ :*  ++      +*,                    :;++++;:,,                     
           ,:;+;;+:  ;:,* :*,         ,+*,                               
        ,:;;;::;;,  ,; *;,+,            ;*;              xSMTP Scanner                          
    ,,:;::, ,;;,    ,,:*,;,              ,;+;,         Multithreaded Version                                  
  ,::,,  ,:;:,       :?,,                  ,:++:,                                     
        ::,        :++,                       ,;+;,           Coded by Dpr                                    
                 :+;,                            ,::,           github.com/c99tn
""",'blue'))

"""
#Deprecated, to format input data logs from PortSpyder, shoutout my friend @xdavidhu
def format():
  print('Starting Format Now...')
  with open('filter.txt') as fil:
      f = open("list.txt", "a")
      for myStr in fil:
        if 'subnet' in myStr:
          print('skipped subnet..')
        else:
          urStr = myStr.replace(' - OPEN: ',':')
          splited = urStr.split(':')
          myIP = splited[0]
          ports = splited[1]
          myPorts = ports.split(' ')
          for port in myPorts:
            if port == myPorts[-1]:
              f.write(myIP+':'+port)
            else:
              f.write(myIP+':'+port+'\n')
  f.close()
  print('Done !')
 """

def scan(line):
  data = line.split(":")
  ip = data[0]
  port = int(data[1])
  try:
      with smtplib.SMTP(ip, port, timeout=0.5) as smtp:
          smtp.ehlo()
          subject = 'Email Tester !'
          body = 'Email delivered from', ip, 'with port', port
          msg = f'Subject: {subject}\n\n{body}'
          smtp.sendmail('Pedri <dpr@priv8shop.com>', myemail, msg)
          print(colored(('Good SMTP Devlivered to '+str(myemail)+' '+str(ip)+':'+str(port)),'green'))
          f = open("smtp.txt", "a")
          rz = ip + ":" + str(port)
          f.write(rz)
          f.write("\n")
          f.close()
  except Exception as e:
      print(colored('Bad SMTP Dead!'+ip+':'+str(port)+' -- '+str(e),'red'))

def listenn(line):
  data = line.split(":")
  ip = data[0]
  port = int(data[1])
  DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  rez = DEVICE_SOCKET.connect_ex((str(ip),int(port)))
  if rez == 0:
    info = str(ip)+':'+str(port)
    notif = str(port)+' is open on '+str(ip)
    print(colored(notif,'green'))
    f = open("list.txt", "a")
    f.write(info+"\n")
    DEVICE_SOCKET.close()
  else:
    info = str(port)+' is closed on '+str(ip)
    print(colored(info,'red'))

def domainASN():
  print(colored('Enter your website (without http:// ):','green'))
  url = input('> ')
  try:
        ip_addr = socket.gethostbyname(url)
  except:
          print(colored('Host not found !', 'red'))
          sys.exit()
  asn_fetch = requests.get('https://ipinfo.io/'+ip_addr+'/org?token=c8bb8b5ed87127')
  asn = (asn_fetch.text)
  
  print(colored(asn , 'blue'))
  myasn = asn.split(' ')[0]
  try:
    res = requests.get('https://api.hackertarget.com/aslookup/?q='+myasn)
    print(colored("IP Ranges found: \n", 'magenta'))
    print(res.text+'\n') 
  except:
    print(colored("Dead host maybe!","red"))
    sys.exit()
  with open("ranges.txt", 'a') as f:
    f.write(res.text+'\n')
  print(colored('Success, Ranges saved in ./ranges.txt','green'))

"""
print(colored('','green'))
uncomment to scan for some env paths on ports 80 443 ;P
need help? https://t.me/dpr52

def checkEnv(line):
  data = line.split(":")
  ip = data[0]
  try:
    res = requests.get('http://'+ip+'/.env')
    if 'DB_HOST' in res.text:
      print(colored('Env found:'+str(ip)+'/.env \n', 'green'))
      with open("env.txt", 'a') as f:
        f.write(str(ip)+'/.env \n')
    else:
      print(colored('Nothing BRo:'+str(ip)+'\n', 'red'))
  except:
    print(colored("Dead host maybe!","red"))
"""

## Menu
ans=True
while ans:
    print(colored('[- xSMTP Scanner -]','red'))
    print (colored("""
[1] - Get IP Ranges From a Website (ASN FETCH)
[2] - Check IP Ranges (Listen For SMTP Ports)
[3] - Mass Scan SMTPs
[4] - Help

[5] - Update
[6] - Exit
    """,'cyan'))
    ans=input("> ") 
    if ans=="1": 
      domainASN()
    #########################################################
    elif ans=="3":
      print(colored("""Enter Your Email address to test the SMTP servers :""",'green'))
      print(colored("""Important: Dont use Gmail ! Use Yandex or Protonmail for best results """,'red'))
      myemail = input('> ')
      print(colored("""How many threads to use ?
(Recommended : 50)""",'green'))
      tr2 = input('> ')
      lines = []
      with open('list.txt') as top:
        for line in top:
          lines.append(line)
      print('Scanning '+ str(len(lines)))
      time.sleep(2)
      pool = ThreadPool(int(tr2))
      results = pool.map(scan, lines)
      pool.close() 
      pool.join()

      with open("list.txt", 'r+') as f:
        f.truncate(0)
      print('Done')
    #########################################################
    elif ans=="2":
      print(colored("""[1] - Listen For Recommended Ports [2525,587]
[2] - Listen For All Ports [25,2525,465,587]
      """,'green'))
      method = input('> ')
      print(colored("""How many threads to use ?
(Recommended : 50)""",'green'))
      tr1 = input('> ')
      with open("ranges.txt", "r") as f:
        lines = f.readlines()
      with open("ranges.txt", "w") as f:
          for line in lines:
              noalpha = any(c.isalpha() for c in line)
              if (':' not in line) and (not noalpha):
                  f.write(line)

      #range = input('give ip range list:\n')
      print(colored('Collecting all Hosts in your Ranges.. Please Wait','blue'))
      if method == '1':
        ports = [2525,587]
      elif method == '2':
        ports = [25,2525,465,587]
      inp = []
      cip = 0
      with open('ranges.txt') as ranges:
        for range in ranges:
          range.replace("\n", "")
          for ip in ipaddress.IPv4Network(range.strip()):
            for port in ports:
              inp.append(str(ip)+':'+str(port))
              cip += 1
      print(colored(str(cip)+' Hosts collected !','blue'))
      time.sleep(2)
      pool = ThreadPool(int(tr1))
      results = pool.map(listenn, inp)
      pool.close() 
      pool.join()
      with open("ranges.txt", 'r+') as f:
        f.truncate(0)
      print(colored('Done, Hosts saved in ./list.txt','green'))
    #########################################################
    elif ans=="6":
      print('Goodbye...')
      sys.exit()
    #########################################################
    elif ans=="5":
      print(colored("""Clone from the official repo : https://github.com/c99tn/xSMTP
and run git pull to fetch and download latest updates to xSMTP!
Want to be notified on latest updates and new tools/auto shell bots ? 
join our telegram channel: https://t.me/+7wraokmFiCcxOTk0
Want to get in touch ? dm me on telegram @dpr52
      """,'magenta'))
    #########################################################
    elif ans=="4":
      print(colored('Quota Limit Reached Error ?','blue'))
      print(colored("""
This happens when you request too many ASN lookups in a single day, you will have to wait
and try again later or use your own ip ranges !
      """,'cyan'))
      print(colored('How to get good IP Ranges for SMTP ?','blue'))
      print(colored("""
Shodan, leakix, ip2info, ASN reverse .... Cant say more !
      """,'cyan'))
      print(colored('I dont recieve SMTP Test to my email ?','blue'))
      print(colored("""
Not all SMTPs deliver to your inbox, check spam folder and try to use one of the recommmended
email providers such as Yandex or Protonmail
      """,'cyan'))
      print(colored('Can I use this on a network I dont own ?','blue'))
      print(colored("""
No and this is illegal !I'm not responsible for anything you do with this tool, 
so please only use it for good and educational purposes.
      """,'cyan'))
      
    #########################################################
    elif ans=="/.!#xz":
      print('scanning Env now')
      lines = []
      with open('list.txt') as top:
        for line in top:
          lines.append(line)
      print('Scanning '+ str(len(lines)))
      time.sleep(20000)
      with open("list.txt", 'r+') as f:
        f.truncate(0)
      print('Done')