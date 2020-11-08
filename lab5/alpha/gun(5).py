from random import randrange as rnd, choice
import tkinter as tk
from tkinter import * 
import math
import time

#print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
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
        self.y1 = 450
        self.x2 = 50
        self.y2 = 420
        self.id = canv.create_line(self.x1,self.y1,self.x2,self.y2,width=7) # FIXME: don't know how to set it...
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
        new_ball = ball()
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
        new_ball = ball()
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
            self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, self.x1) * math.cos(self.an),
                    self.y1 + max(self.f2_power, self.x1) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

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
        x = self.x = rnd(300, 740)
        y = self.y = rnd(100, 550)
        r = self.r = rnd(20, 30)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def new_target1(self, color):
        """ Инициализация новой цели. """
        x = self.x = rnd(100, 700)
        y = self.y = rnd(100, 500)
        r = self.r = rnd(10, 15)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        
    def target_move(self):
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
        if self.y+self.r >= 550:
            self.vy = -self.vy

    def target1_move(self):
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
        if self.y+self.r >= 500:
            self.y += -100
        else:
            self.y += choice([-50, -45, -40, -35, -30, 30, 35, 40, 45, 50])

        canv.coords(self.id, x-r, y-r, x+r, y+r)

    def hit(self):
        """Попадание шарика в цель."""
        global points
        canv.coords(self.id, 0, 0, 0, 0)
        points += 1

    def delete(self):
        canv.delete(self.id)


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
id_points = canv.create_text(30, 30, text='', font='28')
g1 = gun()
bullet = 0
balls = []
balls1 = []
points = 0

def new_game(event=''):
    global gun, screen1, balls, balls1, bullet
    t1.new_target1('white')
    t2.new_target('black')
    bullet = 0
    balls = []
    balls1 = []
    
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    
    canv.bind('<Button-3>', g1.fire1_start)
    canv.bind('<ButtonRelease-3>', g1.fire1_end)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls1 or balls:
        if t1.live > 0 :
            t1.target1_move()
        if t2.live > 0 :
            t2.target_move()
        for b in balls:
            b.move()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                canv.itemconfig(id_points, text = str(points))
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел(-а)/(-ов)')
        for i in range(len(balls)):
              if balls[i].live <= 0:
                balls[i].delete()
                balls[i] = None
        balls = [ball for ball in balls if ball is not None]
        
        for b in balls1:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(id_points, text = str(points))
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-3>', '')
                canv.bind('<ButtonRelease-3>', '')
                canv.itemconfig(screen1, text='')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел(-а)/(-ов)')
        for i in range(len(balls1)):
              if balls1[i].live <= 0:
                balls1[i].delete()
                balls1[i] = None 
        balls1 = [ball for ball in balls1 if ball is not None]
        
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(100, new_game)

new_game()

root.mainloop()
