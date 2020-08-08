from pynput.mouse import Controller
mouse = Controller()
while True:
    print(mouse.position)