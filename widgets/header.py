import subprocess

def draw_wifi(draw, x, y, width):
    wifiStrength = subprocess.run(['awk', 'NR==3 {print $3}', '/proc/net/wireless'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print("Wifi Stength: ", wifiStrength)

def print_header(draw, x, y, width):
    draw.rectangle([x,y,x+width, y+50], fill=0)
    draw_wifi(draw, x, y, width)
    
