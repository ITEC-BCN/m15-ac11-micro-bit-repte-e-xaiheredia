from microbit import *

x = 2
y = 2
MAX_TEMP = 50


def grafica_temperatura():
    temperatura = temperature()  
    display.clear()  
    display.plot_bar_graph(temperatura, MAX_TEMP)  

def moure_gota():
    global x, y  
    
    acc_x = accelerometer.get_x()
    acc_y = accelerometer.get_y()
    
    if acc_x <= -150 and x > 0:
        x -= 1
    elif acc_x >= 150 and x < 4:
        x += 1
    
    if acc_y <= -150 and y > 0:
        y -= 1
    elif acc_y >= 150 and y < 4:
        y += 1
    
    display.set_pixel(x, y, 9)
    sleep(50)
    display.set_pixel(x, y, 0)

while True:
    grafica_temperatura()
    moure_gota()
    sleep(200)  
