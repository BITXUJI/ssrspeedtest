import base64
import qrcode
import os
import json
from sys import argv
from datetime import datetime

def nowtime():
	now=datetime.now()
	date_time=now.strftime("%Y%m%d%H%M%S")
	return date_time
def config2ssrlink(ssr_config):
	main_part= ssr_config['server'] + ":" + ssr_config['server_port'] + ":" + ssr_config['protocol'] + ":" + ssr_config['method'] + ":" + ssr_config['obfs'] + ":" + base64.urlsafe_b64encode(ssr_config['password'].encode(encoding="utf-8")).decode().replace('=','')
	param_str = 'obfsparam=' + base64.urlsafe_b64encode(ssr_config['obfsparam'].encode(encoding="utf-8")).decode().replace('=','')\
	+'&remarks=' + base64.urlsafe_b64encode(ssr_config['remarks'].encode(encoding="utf-8")).decode().replace('=','')\
	+'&group=' + base64.urlsafe_b64encode(ssr_config['group'].encode(encoding="utf-8")).decode().replace('=','')
	ssr_link = "ssr://"+base64.urlsafe_b64encode((main_part + "/?" + param_str).encode(encoding="utf-8")).decode().replace('=','');
	return ssr_link

def json2ssrlink_txt(jsonfile):
	ssr_configs=[]
	ssrlist=[]
	with open(jsonfile)as json_file:
		data=json.load(json_file)
	for x in data['configs']:
		ssr_configs.append(x)
	for x in ssr_configs:
		ssrlist.append(config2ssrlink(x))
	with open('temp/ssr'+nowtime()+'.txt','w') as file:
		for listitem in ssrlist:
			file.write("%s\r"%listitem)

def ssrlink2qrcode(ssrlink):
	qr = qrcode.QRCode(
		version=1,
    	error_correction=qrcode.constants.ERROR_CORRECT_M,
    	box_size=8,
    	border=4,
    	)
	filename = 'temp/qrcode'+nowtime()+'.png'
	qr.add_data(ssrlink)
	qr.make(fit=True)
	img = qr.make_image()
	img.save(filename)

if __name__ == "__main__":
	if len(argv)>1 and '.json' in argv[1]:
		print(argv[1])
		file_path=argv[1]
		print("Start converting the json file")
		json2ssrlink_txt(file_path)
		print("Successfully generate the .txt file\n")
	elif len(argv)==1:
		ssrlink=input("请输入ssr链接，生成qrcode：")
		ssrlink2qrcode(ssrlink)
		print("generation complete!")