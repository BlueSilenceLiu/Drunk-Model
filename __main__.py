"""
Suppose that a drunk drank too much and could not go along a straight line.
He starts his 'journey' from a street lamp.
Suppose his moving follows the following rules:

1.Turn to a random direction.
2.Move forward for 1 metre.
3.Back to 1.

Suppose after a n times' moving,
His distance to the street lamp is L.
What is the numerical relation between n and L?

Because the moving have a random progress,
The L is unpredictable.                 _
So we can only say the relation between L (the average value of all possible L-s) and n.

After calculation we found out that:
_    _
L = √n
Now This model is used to calculate if this is right.

Also, this model can also explain the Brown Motion.
"""
DOC = """Suppose that a drunk drank too much and could not go along a straight line.
He starts his 'journey' from a street lamp.
Suppose his moving follows the following rules:

1.Turn to a random direction.
2.Move forward for 1 metre.
3.Back to 1.

Suppose after a n times' moving,
His distance to the street lamp is L.
What is the numerical relation between n and L?

Because the moving have a random progress,
The L is unpredictable.                 _
So we can only say the relation between L (the average value of all possible L-s) and n.

After calculation we found out that:
_     _
L = √n
Now This model is used to calculate if this is right.

Also, this model can also explain the Brown Motion.
"""

from tkinter import *
from turtle import *
import random as r
import math as m
import time as t


# class 'drunk'
class Drunk(Turtle):
    def __init__(self):
        super().__init__()
        self.pd()
        self.shape("circle")
        self.turtlesize(0.1)
        self.speed(0)

    def step(self, length):
        self.rt(r.random()*360)
        self.fd(length)

    def steps(self, times):
        for i in range(times):
            self.step(100)


# emulate
def main(*args):
    c1 = t.perf_counter()
    del args
    global times_box, emulate_id
    data.delete(1.0, END)
    data.insert(INSERT, "√n:" + str(m.sqrt(int(times_box.get()))) + "\n")
    data.update()
    dist_sum = 0
    # create turtle window again.
    try:
        tester = Turtle()
        tester.hideturtle()
        # Here it will raise a Terminator error.
    except Terminator:
        tester = Turtle()
        tester.hideturtle()
        del tester
        # Force it to create the window again.
        # The good news is that it is no matter which function it use,
        # unless the one does not connect with the Screen().
    for i in range(100):
        Screen().title("emulating...(" + int(i/10) * ">" + (10-int(i/10))*"=" + str(i) + "/100)")
        drunk = Drunk()
        drunk.steps(int(times_box.get()))
        dist_sum += drunk.distance(0, 0) / 100
        del drunk
    data.insert(INSERT, "_\nL:" + str(dist_sum / 100)
                + "\n\nDifference:" + str(abs(m.sqrt(int(times_box.get())) - (dist_sum / 100))))
    data.insert(INSERT, "\n\nDifference Percentage:"
                + str(abs(m.sqrt(int(times_box.get())) - (dist_sum / 100)) / dist_sum * 10000) + "%")
    data.update()
    Screen().title("Emulation Finished! Window Close In 3 secs.")
    t.sleep(1)
    Screen().title("Emulation Finished! Window Close In 2 secs.")
    t.sleep(1)
    Screen().title("Emulation Finished! Window Close In 1 secs.")
    t.sleep(1)
    Screen().bye()
    c2 = t.perf_counter()
    emulate_id += 1
    print("emulate[", emulate_id, "] = {")
    print("\ttime:", c2 - c1 - 3, ",")
    print("\tmoveTimes:", times_box.get(), ",")
    print("\tmoveTimesSquareRoot:", m.sqrt(int(times_box.get())), ",")
    print("\taverageDistance:", dist_sum / 100)
    print("};")

def exc(*args):
    del args
    global top
    top.destroy()

def show_inf():
    global DOC
    inf_window = Tk()
    inf_window.title("Information")
    inf_box = Text(inf_window)
    inf_box.insert(INSERT, DOC)
    inf_exc_btn = Button(inf_window,
                         command=inf_window.destroy,
                         text="Close",
                         width=8,
                         height=1)
    inf_box.pack()
    inf_exc_btn.pack()

def resetFocus(*args):
    del args
    global inf
    inf.focus_set()


print("inf = {"
      "\n\tname:Drunk Model;"
      "\n\tversion:1.2.1;"
      "\n\trecent-update-tick:1625655871;"
      "\n\trecent-update-time:Wed Jul 7 19:04:31 2021"
      "\n}")
emulate_id = 0
# GUI data display

# create tkinter objects
top = Tk()
top.title("Drunk Model")
data = Text(top, width=50, height=7)
times_box_outer_box = Frame()
inf = Label(times_box_outer_box, text="n=", height=1)
times_box = Entry(times_box_outer_box)
times_box.insert(INSERT, "2")
btn_box = Frame()
stt_btn = Button(btn_box,
                 command=main,
                 text="start▶",
                 width=10,
                 height=1)
ext_btn = Button(btn_box,
                 command=exc,
                 text="close❌",
                 width=10,
                 height=1)
inf_btn = Button(btn_box,
                 command=show_inf,
                 text="❓",
                 width=3,
                 height=1)

# locate tkinter objects
data.pack()
times_box_outer_box.pack()
inf.pack(side=LEFT)
times_box.pack(side=RIGHT)
btn_box.pack()
stt_btn.pack(side=LEFT)
ext_btn.pack(side=LEFT)
inf_btn.pack(side=LEFT)

data.bind("<FocusIn>", resetFocus)
times_box.bind("<Return>", main)
top.bind("<Escape>", exc)

top.mainloop()
