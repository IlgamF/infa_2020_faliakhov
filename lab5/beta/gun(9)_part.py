from random import randrange as rnd, choice
import tkinter as tk
from tkinter import * 
import math
import time

#print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.create_rectangle(0, 0, 800, 500, fill='lightblue')
canv.create_rectangle(0, 500, 800, 600, fill='grey')
canv.pack(fill=tk.BOTH, expand=1)

x = 0
y = 0
color = 'red'

class ball():
    def __init__(self, x, y, color):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 15
        self.vy = 15
        self.color = color
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 100

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.g = -1.1
        self.x += self.vx
        self.y -= self.vy - 0.5*self.g**2
        self.vx += 0
        self.vy += self.g
        self.live += -1
        self.set_coords()

        if self.x+self.r <= 0: 
            self.vx = -self.vx
        if self.x+self.r >= 800:
            self.vx = -self.vx
        if self.y+self.r <= 0:
            self.vy = -self.vy
        if self.y+self.r >= 600:
            self.vy = -self.vy
        
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if ((obj.x - self.x) **2  + (obj.y - self.y)**2 <= (self.r + obj.r) ** 2):
            return True
        else:
            return False
    def delete(self):
        canv.delete(self.id)
        
class target():
    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        color = (['white'])
        self.new_target(color)
        vx = self.vx = rnd(2, 20)
        vy = self.vy = rnd(2, 20)
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.id = canv.create_oval(0,0,0,0)                                                                   
    # self.id_points = canv.create_text(30,30,text = self.points,font = '28')
    # self.new_target()

    def new_target(self, color):
        """ Инициализация новой цели. """
        x = self.x = rnd(50, 700)
        y = self.y = rnd(50, 400)
        r = self.r = rnd(20, 30)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def new_target1(self, color):
        """ Инициализация новой новой цели. """
        x = self.x = rnd(100, 699)
        y = self.y = rnd(100, 499)
        r = self.r = rnd(10, 15)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        
    def target_move(self):
        '''Движение чёрного шарика'''
        x = self.x
        y = self.y
        r = self.r
  
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, x-r, y-r, x+r, y+r)

        if self.x+self.r <= 50: 
            self.vx = -self.vx
        if self.x+self.r >= 750:
            self.vx = -self.vx
        if self.y+self.r <= 50:
            self.vy = -self.vy
        if self.y+self.r >= 450:
            self.vy = -self.vy

    def target1_move(self):
        '''Движение белого шарика'''
        x = self.x
        y = self.y
        r = self.r

        if self.x+self.r <= 100:
            self.x += 100
        if self.x+self.r >= 700:
            self.x += -100
        else:
            self.x += choice([-50, -45, -40, -35, -30, 30, 35, 40, 45, 50])
        if self.y+self.r <= 100:
            self.y += 100
        if self.y+self.r >= 450:
            self.y += -100
        else:
            self.y += choice([-50, -45, -40, -35, -30, 30, 35, 40, 45, 50])

        canv.coords(self.id, x-r, y-r, x+r, y+r)
        
    def hit(self):
        """Попадание шарика в цель."""
        global points
        canv.coords(self.id, 0, 0, 0, 0)
        points +=1

    def bomb(self):
        global bombs
        canv.after(1000, t2.bomb)
        new_bomb = ball(self.x, self.y, 'green')
        new_bomb.vx = 0
        new_bomb.vy = self.vy
        new_bomb.r += 20
        new_bomb.live = 100
        bombs += [new_bomb]
        canv.coords(new_bomb,
                self.x - new_bomb.r,
                self.y - new_bomb.r,
                self.x + new_bomb.r,
                self.y + new_bomb.r)

    def delete(self):
        canv.delete(self.id)

t1 = target()
t2 = target()
bombs = []

def new_game(event=''):
    '''Функция самой игры'''
    global gun, screen1, balls, balls1, bullet
    t1.new_target1('white')
    t2.new_target('black')
    t1.live = 1
    t2.live = 1
    root.after(1000, t2.bomb)
    while t1.live or t2.live or balls1 or balls:
        if t1.live > 0 :
            t1.target1_move()
        if t2.live > 0 :
            t2.target_move()
        for b in bombs:
            b.move()
        for i in range(len(bombs)):
              if bombs[i].live <= 0:
                  bombs[i].delete()
                
        canv.update()
        time.sleep(0.03)
    canv.itemconfig(screen1, text='')
    root.after(100, new_game)

new_game()

root.mainloop()

