# Program kullanım talimatı
```root@kali:~/cryptology_cracking# python3 hashkır.py
hashkır.py [options] [values]
DECODES SERIES:
	--md5Decode    => md5    password decode
	--sha1Decode   => sha1   password decode
	--sha224Decode => sha224 password decode
	--sha256Decode => sha256 password decode
	--sha512Decode => sha512 password decode
	-p or --password => file path
ENCODES SERIES:
	--md5Encode    => md5    password encode
	--sha1Encode   => sha1   password encode
	--sha224Encoe  => sha224 password encode
	--sha256Encode => sha256 password encode
	--sha512Encode => sha512 password encode
EXAMPLES:
	hashkır.py --md5Decode 21232f297a57a5a743894a0e4a801fc3 --password rockyou.txt
	hashkır.py --sha1Decode 21232f297a57a5a743894a0e4a801fc3 -p rockyou.txt
	hashkır.py --md5Decode admin      ==========> 21232f297a57a5a743894a0e4a801fc3
	hashkır.py --sha256Decode admin   ==========> 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```
======================================================================================

#			Encode etme yolları
```EXAMPLES:
	hashkır.py --md5Decode admin      ==========> 21232f297a57a5a743894a0e4a801fc3
	hashkır.py --sha256Decode admin   ==========> 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
```
======================================================================================

#			Decode etme yolları
```Examples:

root@kali:~/cryptology_cracking# python3 hashkır.py --md5Decode 061fba5bdfc076bb7362616668de87c8 --password password.txt 
[?] I'am trying: 123456
[?] I'am trying: 12345
[?] I'am trying: 123456789
[?] I'am trying: password
[?] I'am trying: iloveyou
[?] I'am trying: princess
[?] I'am trying: 1234567
[?] I'am trying: rockyou
[?] I'am trying: 12345678
[?] I'am trying: abc123
[?] I'am trying: nicole
[?] I'am trying: daniel
[?] I'am trying: babygirl
[?] I'am trying: monkey
[?] I'am trying: lovely
[+] Password: lovely
```
