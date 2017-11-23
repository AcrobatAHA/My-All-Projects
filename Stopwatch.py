import simplegui



interval = 100
count = 0
total_stops = 0
succes_stops = 0
stop = True



def format(t):
    tenth_sec = (t) % 10
    sec = int(t / 10) % 10
    minutes = int(t / 600) % 600
    ten_min = int(t / 100) % 6
    string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return string
pass
    

def Start():
    global count, stop
    stop = False
    timer.start()
    
def Stop():
    global total_stops, succes_stops, stop
    if stop == False :
        if count % 10 == 0 and count != 0 :
            succes_stops += 1
            total_stops += 1
        elif count != 0 :
            total_stops += 1
    stopped = True
    timer.stop()
    
def Reset():
    global count, succes_stops, total_stops
    count = 0
    stop = True
    total_stops = 0
    succes_stops = 0
    timer.stop()


def tick():
    global count
    count += 1


def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(succes_stops) + '/' + str(total_stops), (190,30), 24, "pink")
    

frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('green')


frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)


frame.start()
Reset()