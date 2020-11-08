from random import randrange as rnd, choice
import tkinter as tk
import math
import time

#print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
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
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...
        self.f1_on = 0
        self.f1_power = 20
        self.f2_on = 0
        self.f2_power = 10
        self.an = 1

    def fire1_start(self, event):
        self.f2_on = 1
        
    def fire1_end(self, event):
        """Выстрел мячом.
        Это новый тип снаряда!!!
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls1, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 0
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f1_power * math.cos(self.an)
        new_ball.vy = - self.f1_power * math.sin(self.an)
        balls1 += [new_ball]
        self.f1_on = 0
        self.f1_power = 20

    def targetting1(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f1_on:
            canv.itemconfig(self.id, fill='brown')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f1_power, 20) * math.cos(self.an),
                    450 + max(self.f1_power, 20) * math.sin(self.an)
                    )

    def power_up1(self):
        if self.f1_on:
            if self.f1_power < 100:
                self.f1_power += 1
            canv.itemconfig(self.id, fill='brown')
        else:
            canv.itemconfig(self.id, fill='black')

    def fire2_start(self, event):
        self.f2_on = 1
        
    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls2, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls2 += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting2(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up2(self):
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
        self.new_target()
        vx = self.vx = rnd(2, 20)
        vy = self.vy = rnd(2, 20)
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.id = canv.create_oval(0,0,0,0)                                                                   
    # self.id_points = canv.create_text(30,30,text = self.points,font = '28')
    # self.new_target()
    
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(300, 740)
        y = self.y = rnd(100, 550)
        r = self.r = rnd(10, 30)
        color = self.color = choice(['blue', 'green', 'brown', 'yellow', 'black', 'white', 'pink'])
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
id_points = canv.create_text(30,30,text = '',font = '28')
g1 = gun()
bullet = 0
balls1 = []
balls2 = []
points = 0

def new_game(event=''):
    global gun, screen1, balls1, balls2, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls1 = []
    balls2 = []
    
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting2)

    canv.bind('<Button-3>', g1.fire1_start)
    canv.bind('<ButtonRelease-3>', g1.fire1_end)
    canv.bind('<Motion>', g1.targetting1)
    
    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls1 or balls2:
        if t1.live > 0 :
            t1.target_move()
        if t2.live > 0 :
            t2.target_move()
            
        for b in balls1:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(id_points, text = str(points))
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                canv.itemconfig(id_points, text = str(points))
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-3>', '')
                canv.bind('<ButtonRelease-3>', '')
                canv.itemconfig(screen1, text='')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел(-а)/(-ов)')
        for b in balls2:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(id_points, text = str(points))
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                canv.itemconfig(id_points, text = str(points))
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел(-а)/(-ов)')
                
        for i in range(len(balls1)):
              if balls1[i].live <= 0:
                balls1[i].delete()
                balls1[i] = None 
        balls1 = [ball for ball in balls1 if ball is not None]

        for i in range(len(balls1)):
              if balls2[i].live <= 0:
                balls2[i].delete()
                balls2[i] = None 
        balls2 = [ball for ball in balls2 if ball is not None]
        
        canv.update()
        time.sleep(0.03)
        g1.targetting1()
        g1.power_up1()
        g1.targetting2()
        g1.power_up2()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(100, new_game)


new_game()

root.mainloop()