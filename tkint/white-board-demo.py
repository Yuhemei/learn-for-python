from tkinter import *

class white_board:
    # Here we initiate with the line drawing tool, this is the tool currently used to draw
    drawing_tool = "line"
    # Here we have the dictionary with the used colors to paint!
    Colors = {'b': 'blue', 'r': 'red', 'g': 'green', 'o': 'orange', 'y': 'yellow', 'c': 'cyan', 'p': 'purple1',
              'd': 'black', 's': 'snow'}
    def __init__(self):
        self._init_whiteboard()
        self._init_item_button()
        # self._init_user_button()
        self._init_color_button()
        # self._init_drawing_area()
        self.color = 'b'
    def show_canvas(self):
        mainloop()
        raise Exception("Board Closed Ending Execution")

    # Here we initiate the whiteboard with Tk() and set it's dimensions
    def _init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('2000x1100')

    # ---------------------------------- Button functions ------------------------------------------
    # Here we have the buttons on the top of the whiteboard
    # Those buttons are responsible for changing the drawing tool as their name indicates
    # Every button pressed is a different drawing tool
    def _init_item_button(self):
        Button(self.myWhiteBoard, text='line', height=1, width=5, bg='dark goldenrod', font='Arial',
               command=lambda: self.set_drawing_tool('line')).place(x=70, y=0)
        Button(self.myWhiteBoard, text='rect', height=1, width=5, bg='saddle brown', font='Arial',
               command=lambda: self.set_drawing_tool('rectangle')).place(x=140, y=0)
        Button(self.myWhiteBoard, text='oval', height=1, width=5, bg='NavajoWhite4', font='Arial',
               command=lambda: self.set_drawing_tool('oval')).place(x=210, y=0)
        # Button(self.myWhiteBoard, text='text', height=1, width=5, bg='SteelBlue4', font='Arial',
        #        command=self.get_text_from_user).place(x=280, y=0)
        Button(self.myWhiteBoard, text='pencil', height=1, width=5, bg='DeepSkyBlue2', font='Arial',
               command=lambda: self.set_drawing_tool('pencil')).place(x=350, y=0)
        Button(self.myWhiteBoard, text='circle', height=1, width=5, bg='Turquoise2', font='Arial',
               command=lambda: self.set_drawing_tool('circle')).place(x=420, y=0)
        Button(self.myWhiteBoard, text='square', height=1, width=5, bg='CadetBlue1', font='Arial',
               command=lambda: self.set_drawing_tool('square')).place(x=490, y=0)
        Button(self.myWhiteBoard, text='eraser', height=1, width=5, bg='purple1', font='Arial',
               command=lambda: self.set_drawing_tool('eraser')).place(x=560, y=0)
        Button(self.myWhiteBoard, text='drag', height=1, width=5, bg='green', font='Arial',
               command=lambda: self.set_drawing_tool('drag')).place(x=630, y=0)
        # Button(self.myWhiteBoard, text='delALL', height=1, width=5, bg='snow', font='Arial',
        #        command=self.erase_all).place(x=700, y=0)

    # This is the own user button, it is used mostly as a display of the user name
    def _init_user_button(self):
        Button(self.myWhiteBoard, text=self.my_connexion.ID, height=1, width=5, bg='snow').place(x=1100, y=0)

    # This are the color buttons, they are responsible for changing the colors of the corresponding drawings
    def _init_color_button(self):

        Button(self.myWhiteBoard, height=1, width=5, bg='red',
               command=lambda: self.set_color('red')).place(x=1010,y=50)
        Button(self.myWhiteBoard, height=1, width=5, bg='orange',
               command=lambda: self.set_color('orange')).place(x=1010, y=100)
        Button(self.myWhiteBoard, height=1, width=5, bg='yellow',
               command=lambda: self.set_color('yellow')).place(x=1010, y=150)
        Button(self.myWhiteBoard, height=1, width=5, bg='green',
               command=lambda: self.set_color('green')).place(x=1010, y=200)
        Button(self.myWhiteBoard, height=1, width=5, bg='cyan',
               command=lambda: self.set_color('cyan')).place(x=1010, y=250)
        Button(self.myWhiteBoard, height=1, width=5, bg='blue',
               command=lambda: self.set_color('blue')).place(x=1010, y=300)
        Button(self.myWhiteBoard, height=1, width=5, bg='purple1',
               command=lambda: self.set_color('purple1')).place(x=1010, y=350)
        Button(self.myWhiteBoard, height=1, width=5, bg='black',
               command=lambda: self.set_color('black')).place(x=1010, y=400)
        Button(self.myWhiteBoard, height=1, width=5, bg='snow',
               command=lambda: self.set_color('snow')).place(x=1010, y=450)


if __name__ == '__main__':
    wb=white_board()
    wb.show_canvas()