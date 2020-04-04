#/usr/bin/python
try:
	import hashlib
	from termcolor import colored
	import sys
	import os
except ModuleNotFoundError:
	print("missing module installation started")
	os.system("pip3 install termcolor")
	os.system("pip3 install termcolor")
	os.system("pip3 install hashlib")
	os.system("pip install hashlib")
	os.system("clear")
	print("please try again")

def bye():
	print("system terminated..")
	sys.exit()


def usage():
	print(sys.argv[0],"""[options] [values]
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
	{} --md5Decode 21232f297a57a5a743894a0e4a801fc3 --password /usr/share/wordlists/rockyou.txt
	{} --sha1Decode 21232f297a57a5a743894a0e4a801fc3 -p /usr/share/wordlists/rockyou.txt
	{} --md5Decode admin      ==========> 21232f297a57a5a743894a0e4a801fc3
	{} --sha256Decode admin   ==========> 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
	""".format(sys.argv[0],sys.argv[0],sys.argv[0],sys.argv[0]))
	sys.exit(1)


def encodeEt():
	if sys.argv[1] in ["--md5Encode"]:
		karakter = sys.argv[2]
		hashjob = hashlib.md5()
		hashjob.update(karakter.encode())
		print(colored(hashjob.hexdigest(),"blue"))

	elif sys.argv[1] in ["--sha1Encode"]:
		karakter = sys.argv[2]
		hashjob = hashlib.sha1()
		hashjob.update(karakter.encode())
		print(colored(hashjob.hexdigest(),"blue"))
	elif sys.argv[1] in ["--sha224Encode"]:
		karakter = sys.argv[2]
		hashjob = hashlib.sha224()
		hashjob.update(karakter.encode())
		print(colored(hashjob.hexdigest(),"blue"))
	elif sys.argv[1] in ["--sha256Encode"]:
		karakter = sys.argv[2]
		hashjob = hashlib.sha256()
		hashjob.update(karakter.encode())
		print(colored(hashjob.hexdigest(),"blue"))
	elif sys.argv[1] in ["--sha512Encode"]:
		karakter = sys.argv[2]
		hashjob = hashlib.sha512()
		hashjob.update(karakter.encode())
		print(colored(hashjob.hexdigest(),"blue"))
	else:
		print("incorrect parameter:",sys.argv[1])

def tryOpen(wordlist):
	global pass_file
	try:
		pass_file = open(wordlist,"r",encoding="utf-8")
	except:
		print("password file not found")
		sys.exit(0)



def decodeEt():
	pass_hash = sys.argv[2]
	wordlist = sys.argv[4]
	tryOpen(wordlist)
	if sys.argv[1] in ["--md5Decode"]:
		if sys.argv[3] in ["-p","--password"]:
			for word in pass_file:
				print(colored("[?] I'am trying: {}".format(word.strip("\n")),"red"))
				enc_word = word.encode("utf-8")
				md5digest = hashlib.md5(enc_word.strip()).hexdigest()
				if md5digest == pass_hash:
					print(colored("[+] Password: {}".format(word), "blue"))
					exit(0)
			print(colored("[!!] Password Not file","red"))

	elif sys.argv[1] in ["--sha1Decode"]:
		if sys.argv[3] in ["-p","--password"]:
			for word in pass_file:
				print(colored("[?] I'am trying: {}".format(word.strip("\n")),"red"))
				enc_word = word.encode("utf-8")
				md5digest = hashlib.sha1(enc_word.strip()).hexdigest()
				if md5digest == pass_hash:
					print(colored("[+] Password: {}".format(word), "blue"))
					exit(0)
			print(colored("[!!] Password Not file","red"))

	elif sys.argv[1] in ["--sha224Decode"]:
		if sys.argv[3] in ["-p","--password"]:
			for word in pass_file:
				print(colored("[?] I'am trying: {}".format(word.strip("\n")),"red"))
				enc_word = word.encode("utf-8")
				md5digest = hashlib.sha224(enc_word.strip()).hexdigest()
				if md5digest == pass_hash:
					print(colored("[+] Password: {}".format(word), "blue"))
					exit(0)
			print(colored("[!!] Password Not file","red"))

	elif sys.argv[1] in ["--sha256Decode"]:
		if sys.argv[3] in ["-p","--password"]:
			for word in pass_file:
				print(colored("[?] I'am trying: {}".format(word.strip("\n")),"red"))
				enc_word = word.encode("utf-8")
				md5digest = hashlib.sha256(enc_word.strip()).hexdigest()
				if md5digest == pass_hash:
					print(colored("[+] Password: {}".format(word), "blue"))
					exit(0)
			print(colored("[!!] Password Not file","red"))

	elif sys.argv[1] in ["--sha512Decode"]:
		if sys.argv[3] in ["-p","--password"]:
			for word in pass_file:
				print(colored("[?] I'am trying: {}".format(word.strip("\n")),"red"))
				enc_word = word.encode("utf-8")
				md5digest = hashlib.sha512(enc_word.strip()).hexdigest()
				if md5digest == pass_hash:
					print(colored("[+] Password: {}".format(word), "blue"))
					exit(0)
			print(colored("[!!] Password Not file","red"))
	else:
		print("incorrect parameter:",sys.argv[1] or sys.argv[4])
		usage()
		bye()

def main():
	try:
		if len(sys.argv) >=4:
			decodeEt()
		elif len(sys.argv) ==3:
			encodeEt()
		elif len(sys.argv) ==1:
			usage()
	except KeyboardInterrupt:
		print("\nsistem durduruldu...")
		sys.exit(0)
main()
