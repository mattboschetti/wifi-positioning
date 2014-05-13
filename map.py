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
		angles = []
		ssid = ''
		bssid = ''
	
		for n in range(4):
			print('Angle {0}'.format(n))
			ssid, bssid, rssi = read_values()
			angles.append(int(rssi.replace('\n','')))
			if n != 3:
				raw_input('Turn yourself 90 degrees and press enter...')

		angles.append(numpy.mean(angles))
		results.append((position, ssid, bssid, angles))

		if raw_input('Continue (y/n)? ') == 'n':
			save_results(results)
			raise SystemExit(0)

def save_results(results):
	f = open('map.csv', 'w')
	for r in results:
		pos, ssid, bssid, angles = r
		f.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(pos, ssid, bssid, angles[0], angles[1], angles[2], angles[3], angles[4]))
	f.close()

if __name__ == '__main__':
	main()