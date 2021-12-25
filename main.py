from tkinter import *
import sys
import pygame
from tkinter import PhotoImage
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

with open("Travel.txt") as f:
    lines = f.readlines()

class Main(Frame):
    curState = 0
    destination = [i for i in range(8)]
    nName = []
    n = []
    nNum = 0

    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startMenu()
        pygame.mixer.init()
        pygame.mixer.music.load("_Main_Theme.mp3")
        pygame.mixer.music.play(loops=0)

    def startMenu(self):
        self.exitImage = PhotoImage(file="_Exit.png")
        self.BG_MainLabel = PhotoImage(file="_BG_MainWindow.png")
        self.buttonMenuImage1 = PhotoImage(file="_Button_Menu_Start.png")
        self.buttonMenuImage2 = PhotoImage(file="_Button_Menu_Level.png")
        self.buttonMenuImage3 = PhotoImage(file="_Button_Menu_Exit.png")

        btn = Button(root, image=self.buttonMenuImage1,
                     command=lambda: self.closeMenu(btn, btn2, btn3),
                     bg="#555")
        btn2 = Button(root, image=self.buttonMenuImage2,
                      command=lambda: sys.exit(),
                      bg="#555")
        btn3 = Button(root, image=self.buttonMenuImage3,
                      command=lambda: sys.exit(),
                      bg="#555")
        btn.place(x=screenWidth * 0.41, y=screenHeight * 0.47, width=screenWidth * 0.157,
                  height=screenHeight * 0.079)
        btn2.place(x=screenWidth * 0.41, y=screenHeight * 0.58, width=screenWidth * 0.157,
                   height=screenHeight * 0.079)
        btn3.place(x=screenWidth * 0.41, y=screenHeight * 0.7, width=screenWidth * 0.157,
                   height=screenHeight * 0.079)

    def closeMenu(self, a, b, c):
        a.destroy()
        b.destroy()
        c.destroy()
        canvas1.create_image(0, 0, anchor="nw", image=Bg_Main_With_Text)
        self.startQuest()

    def startQuest(self):
        self.img = PhotoImage(file="_BG_MainWindow.png")
        self.Bg_Main = PhotoImage(file="_BG_Main.png")
        self.ImgRestartButton = PhotoImage(file = "_Restart_Button.png")
        canvas1.create_image(0, 0, image=self.Bg_Main,
                             anchor="nw")
        self.exitButton = Button(root, image=self.exitImage,
                                 command=lambda: sys.exit(),
                                 bg="#555")
        self.textMainWindow = Label(root,
                                    text="text",
                                    image=self.img,
                                    font=("Calibri", 13)
                                    )
        self.restartButton = Button(root, command=lambda: self.restart(),
                                    image = self.ImgRestartButton,
                                    bg="#555")
        self.textIcon = Label(root,
                              text="default",
                              font=("Calibri", 13)
                              )

        self.textMainWindow.place(x=screenWidth * 0.05, y=screenHeight * 0.05, width=screenWidth * 0.6,
                                  height=screenHeight * 0.5)
        self.textIcon.place(x=screenWidth * 0.4, y=screenHeight * 0.6, width=screenWidth * 0.4,
                                  height=screenHeight * 0.3)
        self.exitButton.place(x=screenWidth * 0.95, y=screenHeight * 0.05, width=screenWidth * 0.038,
                                  height=screenHeight * 0.065)
        self.restartButton.place(x=screenWidth * 0.95, y=screenHeight * 0.15, width=screenWidth * 0.038,
                                  height=screenHeight * 0.065)
        self.buttonAnswer1 = Button(root, text="1", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[0]),
                                    bg="#555", anchor="n")
        self.buttonAnswer2 = Button(root, text="2", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[1]),
                                    bg="#555", anchor="n")
        self.buttonAnswer3 = Button(root, text="3", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[2]),
                                    bg="#555", anchor="n")
        self.buttonAnswer4 = Button(root, text="3", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[3]),
                                    anchor="n")
        self.buttonAnswer5 = Button(root, text="3", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[4]),
                                    anchor="n")
        self.buttonAnswer6 = Button(root, text="3", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[5]),
                                    anchor="n")
        self.buttonAnswer7 = Button(root, text="3", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[6]),
                                    anchor="n")
        self.buttonAnswer8 = Button(root, text="3", font=("Vladimir Script", 13),
                                    command=lambda: self.readTextByCurrentState(self.destination[7]),
                                    anchor="n")
        self.readStart()
        self.readTextByCurrentState(0)

    def restart(self):
        self.clearStart()
        self.readStart()
        self.readTextByCurrentState(0)

    def changeButtonText(self, numOfAnswer, line):
        if numOfAnswer == 1:
            self.buttonAnswer1["text"] = line
            self.buttonAnswer1.place(x=screenWidth * 0.05, y=screenHeight * 0.58, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 2:
            self.buttonAnswer2["text"] = line
            self.buttonAnswer2.place(x=screenWidth * 0.05, y=screenHeight * 0.625, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 3:
            self.buttonAnswer3["text"] = line
            self.buttonAnswer3.place(x=screenWidth * 0.05, y=screenHeight * 0.67, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 4:
            self.buttonAnswer4["text"] = line
            self.buttonAnswer4.place(x=screenWidth * 0.05, y=screenHeight * 0.715, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 5:
            self.buttonAnswer5["text"] = line
            self.buttonAnswer5.place(x=screenWidth * 0.05, y=screenHeight * 0.76, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 6:
            self.buttonAnswer6["text"] = line
            self.buttonAnswer6.place(x=screenWidth * 0.05, y=screenHeight * 0.805, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 7:
            self.buttonAnswer7["text"] = line
            self.buttonAnswer7.place(x=screenWidth * 0.05, y=screenHeight * 0.85, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)
        elif numOfAnswer == 8:
            self.buttonAnswer8["text"] = line
            self.buttonAnswer8.place(x=screenWidth * 0.05, y=screenHeight * 0.895, width=screenWidth * 0.3,
                                     height=screenHeight * 0.045)

    def readTextByCurrentState(self, CurState):
        flag = 0
        mainText = ""
        numOfAnswers = 0
        I = 0
        for line in lines:
            if flag == 21:
                if (line[:1] == ">"):
                    if (int(self.n[I]) < int(line[1:-1])):
                        self.disableButton(numOfAnswers)
                if (line[:1] == "<"):
                    if (int(self.n[I]) > int(line[1:-1])):
                        self.disableButton(numOfAnswers)
                flag = 2
            if flag == 20:
                for i in range(self.nNum):
                    if (self.nName[i] == line[:-1]):
                        flag = 21
                        I = i
            if (flag > 0) and (line[:2] == "&&"):
                self.im = Image.open('_BG_MainWindow.png').convert('RGB')
                self.im = self.im.resize((int(screenWidth * 0.6), int(screenHeight * 0.5)), Image.ANTIALIAS)
                draw = ImageDraw.Draw(self.im)
                pixellat = ImageFont.truetype("arial.ttf", 14)
                draw.text((40, 30), mainText, (0, 0, 0), font=pixellat)
                self.im.save('_BG_Main_Window_With_Text.png')
                self.img = PhotoImage(file="_BG_Main_Window_With_Text.png")
                self.textMainWindow["image"] = self.img
                if (line[-2:-1] == '!'):
                    self.destination[numOfAnswers] = line[2:-2]
                else:
                    self.destination[numOfAnswers] = line[2:-1]
                numOfAnswers = numOfAnswers + 1
                if (line[-2:-1] == '!'):
                    flag = 20
                else:
                    flag = 2
            if (flag == 1) and (line[:2] != "$$"):
                mainText += line
            if (line[:2] == "##") and (str(CurState) == line[2:-1]):
                flag = 1
                self.activateButtons()
            if (flag == 2) and (line[:2] != "&&") and (line[:2] != "##"):
                self.changeButtonText(numOfAnswers, line)
            if (flag == 2) and (line[:2] == "##"):
                flag = 0
                self.disableButtons(numOfAnswers)
                numOfAnswers = 0
            if (flag == 11):
                temp = int(self.n[I])
                if (line[:1] == "+"):
                    temp += int(line[1:-1])
                if (line[:1] == "-"):
                    temp -= int(line[1:-1])
                if (line[:1] == "*"):
                    temp *= int(line[1:-1])
                if (line[:1] == "/"):
                    temp /= int(line[1:-1])
                self.n[I] = str(temp)
                self.writeStartCon()
                flag = 1
            if (flag == 10):
                for i in range(self.nNum):
                    if (self.nName[i] == line[:-1]):
                        flag = 11
                        I = i
            if (line[:2] == "$$") and (flag < 10) and (flag > 0):
                flag = 10
        self.endGameCheck()

    def endGameCheck(self):
        flag = 0
        for line in lines:
            if flag == 3:
                flag = 1
            if line[:-1] == "&Условия поражения&":
                flag = 1
            if line[:-1] == "&Конец условий поражения&":
                break
            if (flag == 2):
                if (line[:1] == ">"):
                    if int(self.n[I]) > int(line[1:-1]):
                        self.clearStart()
                        self.readStart()
                        self.readTextByCurrentState(10)
                if (line[:1] == "<"):
                    if int(self.n[I]) < int(line[1:-1]):
                        self.clearStart()
                        self.readStart()
                        self.readTextByCurrentState(10)
                flag = 3
            if (flag == 1) and (line[:-1] != "&Условия поражения&"):
                for i in range(self.nNum):
                    if self.nName[i] == line[:-1]:
                        flag = 2
                        I = i

    def clearStart(self):
        self.n.clear()
        self.nNum = 0
        self.nName.clear()

    def activateButtons(self):
        self.buttonAnswer1['state'] = 'normal'
        self.buttonAnswer2['state'] = 'normal'
        self.buttonAnswer3['state'] = 'normal'
        self.buttonAnswer4['state'] = 'normal'
        self.buttonAnswer5['state'] = 'normal'
        self.buttonAnswer6['state'] = 'normal'
        self.buttonAnswer7['state'] = 'normal'
        self.buttonAnswer8['state'] = 'normal'

    def disableButton(self, numOfButtons):
        if numOfButtons == 1:
            self.buttonAnswer1['state'] = 'disabled'
        if numOfButtons == 2:
            self.buttonAnswer2['state'] = 'disabled'
        if numOfButtons == 3:
            self.buttonAnswer3['state'] = 'disabled'
        if (numOfButtons == 4):
            self.buttonAnswer4['state'] = 'disabled'
        if (numOfButtons == 5):
            self.buttonAnswer5['state'] = 'disabled'
        if (numOfButtons == 6):
            self.buttonAnswer6['state'] = 'disabled'
        if (numOfButtons == 7):
            self.buttonAnswer7['state'] = 'disabled'
        if (numOfButtons == 8):
            self.buttonAnswer8['state'] = 'disabled'

    def disableButtons(self, numOfButtons):
        if (numOfButtons < 1):
            self.buttonAnswer1.place_forget()
        if (numOfButtons < 2):
            self.buttonAnswer2.place_forget()
        if (numOfButtons < 3):
            self.buttonAnswer3.place_forget()
        if (numOfButtons < 4):
            self.buttonAnswer4.place_forget()
        if (numOfButtons < 5):
            self.buttonAnswer5.place_forget()
        if (numOfButtons < 6):
            self.buttonAnswer6.place_forget()
        if (numOfButtons < 7):
            self.buttonAnswer7.place_forget()
        if (numOfButtons < 8):
            self.buttonAnswer8.place_forget()

    def readStart(self):
        flag = 0
        for line in lines:
            if flag == 3:
                flag = 1
            if line[:-1] == "&Новые переменные&":
                flag = 1
            if line[:-1] == "&Конец новых переменных&":
                flag = 0
            if (flag == 2):
                self.n.append(line[:-1])
                flag = 3
            if (flag == 1) and (line[:-1] != "&Новые переменные&"):
                self.nName.append(line[:-1])
                flag = 2
                self.nNum += 1
        self.writeStartCon()

    def writeStartCon(self):
        makeText = ""
        for i in range(self.nNum):
            makeText += self.nName[i]
            makeText += " = "
            makeText += self.n[i]
            makeText += "\n"
        self.im2 = Image.open('_BG_MainWindow.png').convert('RGB')
        self.im2 = self.im2.resize((int(screenWidth * 0.4), int(screenHeight * 0.3)), Image.ANTIALIAS)
        draw = ImageDraw.Draw(self.im2)
        pixellat = ImageFont.truetype("arial.ttf", 14)
        draw.text((30, 20), makeText, (0, 0, 0), font=pixellat)
        self.im2.save('_BG_Main_Window_With_Text.png')
        self.img2 = PhotoImage(file="_BG_Main_Window_With_Text.png")
        self.textIcon["image"] = self.img2


if __name__ == '__main__':
    root = tk.Tk()
    screenHeight = root.winfo_screenheight()
    screenWidth = root.winfo_screenwidth()
    screenResolution = str(screenWidth) + "x" + str(screenHeight)
    root.geometry(screenResolution)
    root.title("Super Quest")
    root.resizable(False, False)
    Bg_Main_With_Text = PhotoImage(file="_BG_Main_With_Text.png")
    canvas1 = Canvas(root, width=screenWidth,
                     height=screenHeight)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=Bg_Main_With_Text,
                         anchor="nw")
    app = Main(root)
    app.pack()
    root.mainloop()

f.close()
