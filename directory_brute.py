import requests 
import argparse
import sys


parser=argparse.ArgumentParser()
parser.add_argument('-w', '--wordlist', type=str, required=True,help='Switch for wordlist')
parser.add_argument('-u', '--url',type=str, required=True, help='Switch for adding URL')
args=parser.parse_args()

print('[+] Wordlist:',args.wordlist)
print('[+] URL:',args.url)

my_header={
	'User-Agent':'I am testing'
}


file=open(args.wordlist,'r')
endpoints_list=file.readlines()



if ('http' in args.url) or ('https' in args.url):
	pass
else:
	print('Mention the protocol')
	sys.exit()

try:
	for directory in endpoints_list:
		directory=directory.strip("\n")
		r=requests.get(args.url+'/'+directory,headers=my_header)
		if (r.status_code !=404):
			print("[+] Found", args.url+'/'+directory, ":", r.status_code)
except:
	print("Error Occured")
