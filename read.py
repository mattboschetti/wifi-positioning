import subprocess
import numpy

def read_values():
	proc = subprocess.Popen(["airport -s | grep BlackPearl | awk '{ print $1, $2, $3 }'"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	ssid, bssid, rssi = out.split(" ")
	return (ssid, bssid, rssi)

def main():
	results = []
	to_continue = True

	while to_continue:
		position = raw_input('Position num: ')
		ssid, bssid, rssi = read_values()
		results.append((position, ssid, bssid, int(rssi.replace('\n',''))))

		if raw_input('Continue (y/n)? ') == 'n':
			save_results(results)
			raise SystemExit(0)

def save_results(results):
	f = open('read.csv', 'w')
	for r in results:
		pos, ssid, bssid, rssi = r
		f.write('{0},{1},{2},{3}\n'.format(pos, ssid, bssid, rssi))
	f.close()

if __name__ == '__main__':
	main()