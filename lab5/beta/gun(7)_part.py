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
canv.create_rectangle(0, 0, 800, 500, fill='pink')
canv.create_rectangle(0, 500, 800, 600, fill='grey')
canv.pack(fill=tk.BOTH, expand=1)

x = 0
y = 0

class ball():
    def __init__(self, x, y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 2
        self.vx = 10
        self.vy = 10
        self.color = 'red'
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

class gun():
    def __init__(self):
        self.x1 = 20
        self.y1 = 530
        self.x2 = 50
        self.y2 = 500
        self.id = canv.create_line(self.x1, self.y1, self.x2, self.y2, width=7) # FIXME: don't know how to set it...
        self.f2_on = 0
        self.f2_power = 10
        self.an = 1

    def fire1_start(self, event):
        self.f2_on = 1
        
    def fire1_end(self, event):
        """Выстрел мячом.
        new bullet!!!
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls1, bullet
        bullet += 1
        new_ball = ball(self.x1, self.y1)
        new_ball.r += 10
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls1 += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
    
    def fire2_start(self, event):
        self.f2_on = 1
        
    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x1, self.y1)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.x-self.x1) >= 0:
                self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
            else:
                self.an = math.pi + math.atan((event.y-self.y1) / (event.x-self.x1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='green')
        canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        '''Усиление выстрела + окрашивание пушки в оранжевый'''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='green')

    def gun_move_right(self, event=0):
        if self.x2 <= 785:
            self.x1 += 10
            self.x2 += 10
            canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def gun_move_left(self, event=0):
        if self.x1 >= 15:
            self.x1 -= 10
            self.x2 -= 10
            canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def delete(self):
        canv.delete(self.id)

g1 = gun()
bullet = 0
balls = []
balls1 = []
points = 0

canv.focus_set()
canv.bind('d', g1.gun_move_right)
canv.bind('a', g1.gun_move_left)

canv.bind('<Button-1>', g1.fire2_start)                          
canv.bind('<ButtonRelease-1>', g1.fire2_end)
canv.bind('<Motion>', g1.targetting)

canv.bind('<Button-3>', g1.fire1_start)
canv.bind('<ButtonRelease-3>', g1.fire1_end)
