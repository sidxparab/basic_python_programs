import requests
import sys
import argparse

found_subdomains=[]

parser=argparse.ArgumentParser()
parser.add_argument('-d', '--domain', type=str, required=True, help='Specify the main domain')
parser.add_argument('-w', '--wordlist', type=str, required=True, help='Specify the wordlist')
args=parser.parse_args()


file=open(args.wordlist,'r')
domains_list=file.readlines()


for line in domains_list:
	line=line.strip('\n')
	url=f"http://{line}.{args.domain}"
	try:
		requests.get(url)
	except requests.ConnectionError:
		pass 
	else:
		print("[+] New subdomain Found",url)
		found_subdomains.append(url)


with open("Found_subdomains.txt","w") as f:
	for line in found_subdomains:
		print(line,file=f)
