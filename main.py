import rp2
import network
import ubinascii
from machine import Pin
import machine
import urequests as requests
import time
from secrets import secrets
import socket
import utime

# Set up GPIO pins for LEDs
L1_RED_PIN = machine.Pin(0, machine.Pin.OUT)
L1_YELLOW_PIN = machine.Pin(1, machine.Pin.OUT)
L1_GREEN_PIN = machine.Pin(2, machine.Pin.OUT)
L2_RED_PIN = machine.Pin(3, machine.Pin.OUT)
L2_YELLOW_PIN = machine.Pin(4, machine.Pin.OUT)
L2_GREEN_PIN = machine.Pin(5, machine.Pin.OUT)
L3_RED_PIN = machine.Pin(6, machine.Pin.OUT)
L3_YELLOW_PIN = machine.Pin(22, machine.Pin.OUT)
L3_GREEN_PIN = machine.Pin(8, machine.Pin.OUT)
L4_RED_PIN = machine.Pin(9, machine.Pin.OUT)
L4_YELLOW_PIN = machine.Pin(10, machine.Pin.OUT)
L4_GREEN_PIN = machine.Pin(11, machine.Pin.OUT)
button_pin = machine.Pin(21, Pin.IN)
trigger_pin4 = machine.Pin(15, Pin.OUT)
echo_pin4 = machine.Pin(13,Pin.IN)

def default_led_pattern():
    
        #Lane 1 clear
        # Lane 1: Green
        L1_RED_PIN.value(0)
        L1_YELLOW_PIN.value(0)
        L1_GREEN_PIN.value(1)
        # Lane 2: Red
        L2_RED_PIN.value(0)
        L2_YELLOW_PIN.value(1)
        L2_GREEN_PIN.value(0)
        # Lane 3: Red
        L3_RED_PIN.value(1)
        L3_YELLOW_PIN.value(0)
        L3_GREEN_PIN.value(0)
        # Lane 4: Red
        L4_RED_PIN.value(1)
        L4_YELLOW_PIN.value(0)
        L4_GREEN_PIN.value(0)
        time.sleep(5)
        
        # clear lane 2
        
         # Lane 1: Green
        L1_RED_PIN.value(1)
        L1_YELLOW_PIN.value(0)
        L1_GREEN_PIN.value(0)
        # Lane 2: Red
        L2_RED_PIN.value(0)
        L2_YELLOW_PIN.value(0)
        L2_GREEN_PIN.value(1)
        # Lane 3: Red
        L3_RED_PIN.value(0)
        L3_YELLOW_PIN.value(1)
        L3_GREEN_PIN.value(0)
        # Lane 4: Red
        L4_RED_PIN.value(1)
        L4_YELLOW_PIN.value(0)
        L4_GREEN_PIN.value(0)
        time.sleep(5)
        
        
        # clear lane 3
        
         # Lane 1: Green
        L1_RED_PIN.value(1)
        L1_YELLOW_PIN.value(0)
        L1_GREEN_PIN.value(0)
        # Lane 2: Red
        L2_RED_PIN.value(1)
        L2_YELLOW_PIN.value(0)
        L2_GREEN_PIN.value(0)
        # Lane 3: Red
        L3_RED_PIN.value(0)
        L3_YELLOW_PIN.value(0)
        L3_GREEN_PIN.value(1)
        # Lane 4: Red
        L4_RED_PIN.value(0)
        L4_YELLOW_PIN.value(1)
        L4_GREEN_PIN.value(0)
        time.sleep(5)
        
        # clear lane 4
        
         # Lane 1: Green
        L1_RED_PIN.value(0)
        L1_YELLOW_PIN.value(1)
        L1_GREEN_PIN.value(0)
        # Lane 2: Red
        L2_RED_PIN.value(1)
        L2_YELLOW_PIN.value(0)
        L2_GREEN_PIN.value(0)
        # Lane 3: Red
        L3_RED_PIN.value(1)
        L3_YELLOW_PIN.value(0)
        L3_GREEN_PIN.value(0)
        # Lane 4: Red
        L4_RED_PIN.value(0)
        L4_YELLOW_PIN.value(0)
        L4_GREEN_PIN.value(1)
        time.sleep(5)
        return

def ulane4():
    
        #Lane 4 clear on high density
        # Lane 1: Green
        L1_RED_PIN.value(0)
        L1_YELLOW_PIN.value(1)
        L1_GREEN_PIN.value(0)
        # Lane 2: Red
        L2_RED_PIN.value(1)
        L2_YELLOW_PIN.value(0)
        L2_GREEN_PIN.value(0)
        # Lane 3: Red
        L3_RED_PIN.value(1)
        L3_YELLOW_PIN.value(0)
        L3_GREEN_PIN.value(0)
        # Lane 4: Red
        L4_RED_PIN.value(0)
        L4_YELLOW_PIN.value(0)
        L4_GREEN_PIN.value(1)
        time.sleep(10)
        
        # clear lane 1
        
         # Lane 1: Green
        L1_RED_PIN.value(0)
        L1_YELLOW_PIN.value(0)
        L1_GREEN_PIN.value(1)
        # Lane 2: Red
        L2_RED_PIN.value(0)
        L2_YELLOW_PIN.value(1)
        L2_GREEN_PIN.value(0)
        # Lane 3: Red
        L3_RED_PIN.value(1)
        L3_YELLOW_PIN.value(0)
        L3_GREEN_PIN.value(0)
        # Lane 4: Red
        L4_RED_PIN.value(1)
        L4_YELLOW_PIN.value(0)
        L4_GREEN_PIN.value(0)
        time.sleep(3)
        
        
        # clear lane 2
        
         # Lane 1: Green
        L1_RED_PIN.value(1)
        L1_YELLOW_PIN.value(0)
        L1_GREEN_PIN.value(0)
        # Lane 2: Red
        L2_RED_PIN.value(0)
        L2_YELLOW_PIN.value(0)
        L2_GREEN_PIN.value(1)
        # Lane 3: Red
        L3_RED_PIN.value(0)
        L3_YELLOW_PIN.value(1)
        L3_GREEN_PIN.value(0)
        # Lane 4: Red
        L4_RED_PIN.value(1)
        L4_YELLOW_PIN.value(0)
        L4_GREEN_PIN.value(0)
        time.sleep(3)
        
        # clear lane 3
        
         # Lane 1: Green
        L1_RED_PIN.value(1)
        L1_YELLOW_PIN.value(0)
        L1_GREEN_PIN.value(0)
        # Lane 2: Red
        L2_RED_PIN.value(1)
        L2_YELLOW_PIN.value(0)
        L2_GREEN_PIN.value(0)
        # Lane 3: Red
        L3_RED_PIN.value(0)
        L3_YELLOW_PIN.value(0)
        L3_GREEN_PIN.value(1)
        # Lane 4: Red
        L4_RED_PIN.value(0)
        L4_YELLOW_PIN.value(1)
        L4_GREEN_PIN.value(0)
        time.sleep(3)
        return


def lane1():
    
            L1_RED_PIN.value(0)
            L1_YELLOW_PIN.value(0)
            L1_GREEN_PIN.value(1)
            # Lane 2: Red
            L2_RED_PIN.value(1)
            L2_YELLOW_PIN.value(0)
            L2_GREEN_PIN.value(0)
            # Lane 3: Red
            L3_RED_PIN.value(1)
            L3_YELLOW_PIN.value(0)
            L3_GREEN_PIN.value(0)
            # Lane 4: Red
            L4_RED_PIN.value(1)
            L4_YELLOW_PIN.value(0)
            L4_GREEN_PIN.value(0)
            time.sleep(5)
            return

def lane2():
    
            L1_RED_PIN.value(1)
            L1_YELLOW_PIN.value(0)
            L1_GREEN_PIN.value(0)
            # Lane 2: Red
            L2_RED_PIN.value(0)
            L2_YELLOW_PIN.value(0)
            L2_GREEN_PIN.value(1)
            # Lane 3: Red
            L3_RED_PIN.value(1)
            L3_YELLOW_PIN.value(0)
            L3_GREEN_PIN.value(0)
            # Lane 4: Red
            L4_RED_PIN.value(1)
            L4_YELLOW_PIN.value(0)
            L4_GREEN_PIN.value(0)
            time.sleep(5)
            return

def lane3():
    
            L1_RED_PIN.value(1)
            L1_YELLOW_PIN.value(0)
            L1_GREEN_PIN.value(0)
            # Lane 2: Red
            L2_RED_PIN.value(1)
            L2_YELLOW_PIN.value(0)
            L2_GREEN_PIN.value(0)
            # Lane 3: Red
            L3_RED_PIN.value(0)
            L3_YELLOW_PIN.value(0)
            L3_GREEN_PIN.value(1)
            # Lane 4: Red
            L4_RED_PIN.value(1)
            L4_YELLOW_PIN.value(0)
            L4_GREEN_PIN.value(0)
            time.sleep(5)
            return
        
def lane4():
    
            L1_RED_PIN.value(1)
            L1_YELLOW_PIN.value(0)
            L1_GREEN_PIN.value(0)
            # Lane 2: Red
            L2_RED_PIN.value(1)
            L2_YELLOW_PIN.value(0)
            L2_GREEN_PIN.value(0)
            # Lane 3: Red
            L3_RED_PIN.value(1)
            L3_YELLOW_PIN.value(0)
            L3_GREEN_PIN.value(0)
            # Lane 4: Red
            L4_RED_PIN.value(0)
            L4_YELLOW_PIN.value(0)
            L4_GREEN_PIN.value(1)
            time.sleep(5)
            return

def measure_distance(trigger_pin, echo_pin):
    # Generate a pulse to trigger the ultrasonic sensor
    trigger_pin.low()
    utime.sleep_us(2)
    trigger_pin.high()
    utime.sleep_us(5)
    trigger_pin.low()

    # Measure the duration of the echo pulse
    while echo_pin.value() == 0:
        pulse_start = utime.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = utime.ticks_us()

    # Calculate the distance based on the pulse duration
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 0.034 / 2  # Speed of sound in cm/us divided by 2 (round trip)

    return distance

# Set country to avoid possible errors
rp2.country('IN')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# If you need to disable powersaving mode
# wlan.config(pm = 0xa11140)

# See the MAC address in the wireless chip OTP
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

# Other things to query
# print(wlan.config('channel'))
# print(wlan.config('essid'))
# print(wlan.config('txpower'))

# Load login data from different file for safety reasons
ssid = secrets['ssid']
pw = secrets['pw']


wlan.connect(ssid, pw)

# Wait for connection with 10 second timeout
timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)

        
wlan_status = wlan.status()

if wlan_status != 3:
    raise RuntimeError('Wi-Fi connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    
# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)


# Listen for connections
while True:
    try:
        # Read the button state
        button_state = button_pin.value()
        print(button_state)
        if button_state == 1:
            print("Override Mode")
            L1_RED_PIN.value(1)
            L1_YELLOW_PIN.value(0)
            L1_GREEN_PIN.value(0)
            # Lane 2: Red
            L2_RED_PIN.value(1)
            L2_YELLOW_PIN.value(0)
            L2_GREEN_PIN.value(0)
            # Lane 3: Red
            L3_RED_PIN.value(1)
            L3_YELLOW_PIN.value(0)
            L3_GREEN_PIN.value(0)
            # Lane 4: Red
            L4_RED_PIN.value(1)
            L4_YELLOW_PIN.value(0)
            L4_GREEN_PIN.value(0)
            time.sleep(1)
            
            while(button_state == 1):
                print(button_state)
                cl, addr = s.accept()
                print('Client connected from', addr)
                r = cl.recv(1024)
                # print(r)
                
                r = str(r)
                l1 = r.find('?lane=1')
                l2 = r.find('?lane=2')
                l3 = r.find('?lane=3')
                l4 = r.find('?lane=4')
                print('lane_1 = ', l1)
                print('lane_2 = ', l2)
                print('lane_3 = ', l3)
                print('lane_4 = ', l4)
                
                if l1 > -1:
                    print('LANE 1')
                    lane1()
                if l2 > -1:
                    print('LANE 2')
                    lane2()
                if l3 > -1:
                    print('LANE 3')
                    lane3()
                if l4 > -1:
                    print('LANE 4')
                    lane4()
                    
                response = get_html('index.html')
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(response)
                cl.close()
                button_state = button_pin.value()
                
        default_led_pattern()
#         distance4 = measure_distance(trigger_pin4, echo_pin4)            
#         print("Distance Sensor 4:", distance4, "cm")
#         if distance4 < 5 :
#                 ulane4()
        
        
            
            
    except OSError as e:
        cl.close()
        print('Connection closed')