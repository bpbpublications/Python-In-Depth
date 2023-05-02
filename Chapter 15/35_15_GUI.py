############################################################################################
#    Python in-depth
#
#    Chapter 15
#
#        Python GUI
#
#    Example of a Calculator GUI using tkinter
#
#    Author: Ahidjo Ayeva
###########################################################################################
import sys
import tkinter as tk



class Model():
    def __init__(self):
        self.ops = [ "+", "-", "*", "/"]

    def compute(self, target):
        text = target.get()
        for op in self.ops:
            if op in text:
                param = str(text).split(op)
                if op == "+":
                    return (float(param[0].replace(",", ".")) + float(param[1].replace(",", ".")))
                if op == "*":
                    return (float(param[0].replace(",", ".")) * (float(param[1].replace(",", "."))))
                if op == "-":
                    return (float(param[0].replace(",", ".")) - float(param[1].replace(",", ".")))
                if op == "/":
                    return (float(param[0].replace(",", ".")) / float(param[1].replace(",", ".")))


class View():

    def __init__(self):
        self.master = tk.Tk()
        self.display = tk.Entry(self.master, width=32)
        self.display.focus_set()
        self.master.title("Python in-depthh - GUI example - Calculator ")
        self.display.pack()

        self.operator = tk.Frame(self.master)
        self.operator.pack(fill=tk.BOTH, expand=1,  side="right")
        tk.Button(self.operator, text="+", width=4, height=2).grid(row=0, column=0)
        tk.Button(self.operator, text="-", width=4, height=2).grid(row=0, column=1)
        tk.Button(self.operator, text="*", width=4, height=2).grid(row=1, column=0)
        tk.Button(self.operator, text="/", width=4, height=2).grid(row=1, column=1)
        tk.Button(self.operator, text="(", width=4, height=2).grid(row=2, column=0)
        tk.Button(self.operator, text=")", width=4, height=2).grid(row=2, column=1)
        tk.Button(self.operator, text="=", width=12, height=2).grid(row=3, column=0, columnspan=2)

        self.digit = tk.Frame(self.master)
        self.digit.pack(fill=tk.BOTH, expand=1, side="top")
        tk.Button(self.digit, text="1", width=8, height=2).grid(row=0, column=0)
        tk.Button(self.digit, text="2", width=8, height=2).grid(row=0, column=1)
        tk.Button(self.digit, text="3", width=8, height=2).grid(row=0, column=2)
        tk.Button(self.digit, text="4", width=8, height=2).grid(row=1, column=0)
        tk.Button(self.digit, text="5", width=8, height=2).grid(row=1, column=1)
        tk.Button(self.digit, text="6", width=8, height=2).grid(row=1, column=2)
        tk.Button(self.digit, text="7", width=8, height=2).grid(row=2, column=0)
        tk.Button(self.digit, text="8", width=8, height=2).grid(row=2, column=1)
        tk.Button(self.digit, text="9", width=8, height=2).grid(row=2, column=2)


        self.mixed = tk.Frame(self.master)
        self.mixed.pack(fill=tk.BOTH,side="bottom")

        tk.Button(self.mixed, text=",", width=8, height=2).grid(row=1, column=0)
        tk.Button(self.mixed, text="0", width=8, height=2).grid(row=1, column=1)
        tk.Button(self.mixed, text="C", width=2, height=2).grid(row=1, column=2)
        tk.Button(self.mixed, text="R", width=2, height=2).grid(row=1, column=3)


class Controller():

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.setUp()

    def setUp(self):

        display = self.view.display

        digits = self.view.digit.children
        digits['!button']['command'] = lambda:self.digit_onclick(display, digits['!button']['text'])
        digits['!button2']['command'] = lambda:self.digit_onclick(display, digits['!button2']['text'])
        digits['!button3']['command'] = lambda:self.digit_onclick(display, digits['!button3']['text'])
        digits['!button4']['command'] = lambda:self.digit_onclick(display, digits['!button4']['text'])
        digits['!button5']['command'] = lambda:self.digit_onclick(display, digits['!button5']['text'])
        digits['!button6']['command'] = lambda:self.digit_onclick(display, digits['!button6']['text'])
        digits['!button7']['command'] = lambda:self.digit_onclick(display, digits['!button7']['text'])
        digits['!button8']['command'] = lambda:self.digit_onclick(display, digits['!button8']['text'])
        digits['!button9']['command'] = lambda:self.digit_onclick(display, digits['!button9']['text'])

        operators = self.view.operator.children
        operators['!button']['command'] = lambda:self.operator_onclick(display, operators['!button']['text'])
        operators['!button2']['command'] = lambda:self.operator_onclick(display, operators['!button2']['text'])
        operators['!button3']['command'] = lambda:self.operator_onclick(display, operators['!button3']['text'])
        operators['!button4']['command'] = lambda:self.operator_onclick(display, operators['!button4']['text'])
        operators['!button5']['command'] = lambda:self.operator_onclick(display, operators['!button5']['text'])
        operators['!button6']['command'] = lambda:self.operator_onclick(display, operators['!button6']['text'])
        operators['!button7']['command'] = lambda:self.result_onclick(display)

        mixed = self.view.mixed.children
        mixed['!button']['command'] = (lambda:self.digit_onclick(display, mixed['!button']['text']))
        mixed['!button2']['command'] = (lambda:self.digit_onclick(display, mixed['!button2']['text'] ))
        mixed['!button3']['command'] = (lambda:self.delete(display))
        mixed['!button4']['command'] = (lambda:self.reset(display))

    def digit_onclick(self, target, elt):
        if "=" in target.get():
            target.delete(0,tk.END)
        target.insert(tk.END, elt)

    def operator_onclick(self, target, elt):
        if "=" in target.get():
            t = target.get().split(' ')[1]
            target.delete(0,tk.END)
            target.insert(tk.END,t)
        target.insert(tk.END, elt)

    def result_onclick(self, target):
        result = self.model.compute(target)
        target.delete(0,tk.END)
        target.insert(0, '= ' + str(result))  

    def reset(self, target):
        target.delete(0,tk.END)
        target.insert(0, '')

    def delete(self, target):
        if "=" in target.get():
            target.delete(0,tk.END)
        else:
            txt = target.get()[:-1]
            target.delete(0,tk.END)
            target.insert(0, txt)


if __name__ == '__main__':

    controller = Controller()
    try:
        controller.view.master.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)