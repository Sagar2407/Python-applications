import time
from datetime import datetime as dt
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

while True:
	if dt(dt.now().year,dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day,16):
		print("Working Hours...")

		with open (hosts_path, 'r+') as file:
			content = file.read()
			print(content)
			for website in websites_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()		#here content is a list
			file.seek(0)		# puth the pointer at the beginning of the file
			for line in content:
				if not any(website in line for website in websites_list):
					file.write(line)
			file.truncate()

		print("Enjoy")
	time.sleep(5)