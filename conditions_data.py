import bme280
import smbus2
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as paho
from time import sleep
import random
import board
import adafruit_tcs34725

broker="172.24.1.99"
mqttport=1883

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

def on_publish(client, userdata, result):
    print("data published \n")
    pass

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

client1=paho.Client("bme280")
client1.connect(broker, mqttport)
client1.on_publish = on_publish
client1.loop_start()


while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    lux = sensor.lux
    #print("Lux: ", lux, "\n")
    hum=str(humidity)
    pres=str(pressure)
    temp=str(ambient_temperature)
    lu=str(lux)
    hum=hum[0:5]
    pres=pres[0:7]
    temp=temp[0:5]
    msg=hum+","+pres+","+temp+","+lu
    print(msg)
    ret=client1.publish("testto", msg)
    #client.publish(topic, msg)
    sleep(1)





#172.24.1.99
