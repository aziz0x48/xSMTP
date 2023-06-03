<h1 align="center">
  <br>
  <a href="https://github.com/c99tn/xSMTP"><img src="https://raw.githubusercontent.com/c99tn/xSMTP/main/bin/xsmtp.png" alt="" width="300" height="200"></a>
  <br> 
  xSMTP
  <br>
</h1>
<h4 align="center">xSMTP :mosquito: The One And Only Open-Relay SMTP Servers Scanner Tool On Github </h4>
<p align="center">
  <a href="https://github.com/c99tn/xSMTP">
    <img src="https://img.shields.io/badge/license-MIT-orange">
  </a>
  <a href="https://github.com/c99tn/xSMTP">
    <img src="https://img.shields.io/badge/release-v1.2-blue">
  </a>
  <a href="https://github.com/c99tn/xSMTP">
    <img src="https://img.shields.io/badge/python-3.10-green">
  </a>
    <a href="https://github.com/c99tn/xSMTP">
    <img src="https://img.shields.io/badge/build-passing-brightgreen">
  </a>
</p>

<!-- ![Screenshot from xSMTP sep16,2022](https://github.com/c99tn/xSMTP/blob/main/bin/screenshot.png?raw=true) -->

<p align="center">
<a href="#requirements-wrench">Requirements</a> ◦ 
<a href="#installation-package">Installation</a> ◦ 
<a href="#usage--rescue_worker_helmet">Usage</a> ◦
<a href="#disclaimer-bangbang">Disclaimer</a> ◦
<a href="#contact--speech_balloon">Contact</a>
</p>

**xSMTP** is a lightning fast, multithreaded scanner written in Python, capable of scanning massive network ranges and find open-relay and unsecured SMTP servers inside. ranges can be directly setted in the ranges.txt file or gathered by performing an ASN Lookup, the user can input any website in mind and the tool will make an API Call to external third party services ( <a href="">ipinfo.io</a> and <a href="">api.hackertarget.com</a> ) where all the IP Ranges of the website's ASN will be fetched and saved in ranges.txt file.

with the gathered ranges, xSMTP generates all available hosts and can perform a very fast check and see if hosts can listen on the most used smtp ports (2525,587..) and saves the good hosts on list.txt file, then a mass SMTP scan can be performed, where the tool will try to send a test email with the hosts gathered in list.txt containing the smtp info in the email body, if the smtp server is open-relay/unsecured!

obtained smtp will be in the following format:
```
IP:PORT

51.223.x.x:25
52.23.x.x:587
```
where the ip represents the smtp host followed by the smtp port, <ins>no auth or TLS connection is required</ins> , so you can set those off while sending with these smtps (if required by sending software set security to auto)

example of sending an email with open relay SMTP:


<p align="center"><img src="https://github.com/c99tn/xSMTP/blob/main/bin/test.gif?raw=true"></p>
  

# Requirements :wrench:
- Python v3.x+
- RDP/VPS ( <b>Optional - suitable for scanning massive networks 5M Hosts +</b> )

# Installation :package:
## Debian based systems:
```
$ sudo apt-get update && sudo apt-get install python3 python3-pip -y
$ git clone https://github.com/c99tn/xSMTP
$ cd xSMTP/
$ python3 -m pip install -r requirements.txt
```
## macOS / OSX:
```
$ brew install python3
$ git clone https://github.com/c99tn/xSMTP
$ cd xSMTP/
$ python3 -m pip install -r requirements.txt
```
## Windows:
```
- Download and install python
- Download or clone the repo
- cd xSMTP/
- pip install requirements.txt
- py xsmtp.py
```
# Usage  :rescue_worker_helmet:
## Start xSMTP with python3
```
python3 xsmtp.py
```
## Get IP Ranges from Website ASN
```
> 1
Enter a website url:
> some-domain.com
```
<p align="center"><img src="https://raw.githubusercontent.com/c99tn/xSMTP/main/bin/option1.gif"></p>



## Check IP Ranges
```
> 2   
[1] - Listen For Recommended Ports [2525,587]
[2] - Listen For All Ports [25,2525,465,587]
> 1
How many threads to use ?
(Recommended : 50)
> 50
```
<p align="center"><img src="https://raw.githubusercontent.com/c99tn/xSMTP/main/bin/option2.gif"></p>



## Scan SMTP
```
> 3
Enter your email 
> dpr@priv8toolz.com
Enter Threads
> 50
```
<p align="center"><img src="https://raw.githubusercontent.com/c99tn/xSMTP/main/bin/option3.gif"></p>



# Contact  :speech_balloon:
Got a question ?  
send me a dm on <a href="https://t.me/dpr52">Telegram</a>

# Disclaimer :bangbang:
xSMTP Bot was created for educational purposes only, Any actions and/or activities done using this bot is solely your responsibility.

## :ringed_planet: Join Our Channel To be Notified of Updates and New Releases :ringed_planet:

<br>
<p align="center">
<a href="https://t.me/+7wraokmFiCcxOTk0">
<img src="https://raw.githubusercontent.com/c99tn/Randoms/master/telegram_button_icon_151837.png?token=GHSAT0AAAAAABVX6V7OOUCJTCCDNVAXPHCMYYIHTNA" width="200" height="50">
</a>
</p>


# Legal
Copyright (c) 2022 by @c99tn. Some rights reserved.   
xSMTP is under the terms of the MIT License, following all clarifications stated in the license file.
