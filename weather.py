'''import requests
import json

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/316321'
response = requests.get(url)
#print(response)
'''

from gpiozero import CPUTemperature

cpu = CPUTemperature()
print(cpu.temperature)
