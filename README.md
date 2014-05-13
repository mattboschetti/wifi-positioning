wifi-positioning
================

### Intro
Reads SSID, BSSID and 4 wifi RSSI at each specific location. Output the content to a csv file named map.csv

### Files
- map.py - Used to generate the fingerprint map (wifi rssi reads have to be done at 4 different angles)
- read.py - Used to read the RSSI fingerprint at specific locations
- Home Wifi Measurements.xlsx - spreadsheet that contains the logic to calculate the approximate location
- floorplan.jpg - floorplan used for reference to capture the wifi rssi and the approximate locations
 - In Red: Measured WIFI for fingerprint map
 - In Black: 'Unkwown' Locations
  
### Needed Improvements
- Euclidean distance algorithm for location matching could be improved, by using Weighted KNN instead of KNN
- More readings for RSSI should be captured (mean value) for an unknown location
