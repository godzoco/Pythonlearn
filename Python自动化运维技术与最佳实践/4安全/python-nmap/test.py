import sys
import nmap
import ansible

a=nmap.PortScanner()
a.scan('111.13.101.208','80')
#Nmap -p 80 111.13.101.208
