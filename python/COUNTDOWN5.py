from guizero import App, Text, TextBox, PushButton
def count():
    t = Min*60
    time = t+Sec
    timel = Text(app, Test="")
    timels = Text(app, Text="")
    while (time>1):  
        timel.value = MIN.value
        tilels.value = SEC.value
        time = time - 1
app = App(title="Count Down")
MIn = Text(app, text="Min")
Min = TextBox(app)
SEc = Text(app, text="Sec")
Sec = TextBox(app)
Start = PushButton(app, command=count, text="Start")
app.display()
