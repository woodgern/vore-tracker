import json
import requests
import subprocess

print('Hitting discord\'s API to determine how many shards are needed.')
key = ''
with open("key.txt", "r") as target:
	for line in target:
		line = line.strip()
		key = line

url = 'https://discordapp.com/api/v6/gateway/bot?token=' + key
response = requests.get(url)

processes = []
if (response.ok):
	jData = json.loads(response.content)
	shard_count = int(jData['shards'])
	for x in range(0, shard_count):
		processes.append(subprocess.Popen(['python', 'bot.py', str(x), str(shard_count)]))
	print("Launched processes")
	print(processes.pid)
else:
	print("Can't reach the Gateway endpoint. Giving up.")