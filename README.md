# SSH-BRUTEFORCE

#Gerekli Kütüphaneleri

pip install argparse

pip install paramiko

#Kullanımı

-k = kullanıcı adı veya kullanıcı dosyası 

-p = şifre veya şifre dosyası

-ip = hedefin ip adresi
	
-b = banner için saniye 
	
Örnek Kullanımı
	
	python3 ssh.py -k deneme -p password.txt -ip 192.168.1.1 -b 200
