from random import randrange as rnd, choice
import tkinter as tk
from tkinter import * 
import math
import time

#print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.title('Россия vs UFO')
root.geometry('500x400')
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

        self.up = canv.create_rectangle(self.x1 - 10, self.y1, self.x2 - 5, self.y1 + 5, fill='white')
        self.middle = canv.create_rectangle(self.x1 - 10, self.y1 + 5, self.x2 - 5, self.y1 + 10, fill='blue')
        self.down = canv.create_rectangle(self.x1 - 10, self.y1 + 10, self.x2 - 5, self.y1 + 15, fill='red')
        
    def gun_move_right(self, event=0):
        if self.x2 <= 785:
            self.x1 += 10
            self.x2 += 10
            canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )
            canv.coords(self.up, self.x1 - 10, self.y1, self.x2 - 5, self.y1 + 5)
            canv.coords(self.middle, self.x1 - 10, self.y1 + 5, self.x2 - 5, self.y1 + 10)
            canv.coords(self.down, self.x1 - 10, self.y1 + 10, self.x2 - 5, self.y1 + 15)

    def gun_move_left(self, event=0):
        if self.x1 >= 15:
            self.x1 -= 10
            self.x2 -= 10
            canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )
            canv.coords(self.up, self.x1 - 10, self.y1, self.x2 - 5, self.y1 + 5)
            canv.coords(self.middle, self.x1 - 10, self.y1 + 5, self.x2 - 5, self.y1 + 10)
            canv.coords(self.down, self.x1 - 10, self.y1 + 10, self.x2 - 5, self.y1 + 15)

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
        new_ball = ball(self.x1, self.y1, 'red')
        new_ball.r += 10
        if (event.x-self.x1) >= 0:
            self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
        else:
            self.an = math.pi + math.atan((event.y-self.y1) / (event.x-self.x1))
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
        new_ball = ball(self.x1, self.y1, 'red')
        new_ball.r += 0
        if (event.x-self.x1) >= 0:
            self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
        else:
            self.an = math.pi + math.atan((event.y-self.y1) / (event.x-self.x1))
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
            canv.itemconfig(self.id, fill='pink')
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
            canv.itemconfig(self.id, fill='pink')

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
        x = self.x = rnd(50, 769)
        y = self.y = rnd(50, 469)
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

    def bomb1(self, event=0):
        global bombs
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

    def bomb2(self, event=0):
        global bombs
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

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        m = []
        for i in bombs:
            if (obj.x1 - i.x) **2  + (obj.y1 - i.y)**2 <= (i.r)**2:
                m.append(1)
            else:
                m.append(0)
        if 1 in m:
            return True
        else:
            return False  
        
    def delete(self):
        canv.delete(self.id)

points = 0
g1 = gun()
t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
id_points = canv.create_text(30, 30, text='', font='28')
bullet = 0
balls = []
balls1 = []
bombs = []



def start():
    root.geometry('800x600')
    b1.destroy()
    fra1.destroy()
    rules1.destroy()
    rules2.destroy()
    rules3.destroy()
    rules4.destroy()
    rules5.destroy()
    rules6.destroy()
    rules7.destroy()
    rules8.destroy()
    rules9.destroy()
    new_game()
    finish()
    
fra1 = Frame(root, width=600, height=600, bg="white")
fra1.place(x=0, y=0)

b1 = Button(text='Начать', width=70, height=6)
b1.config(command=start)
b1.place(x=0, y=0)

rules1 = Label(root, text='Инопланетяне напали на Россию!\nТвоя задача - защитить русскую землю,\n уничтожить всех врагов!,', font="Arial 15", bg="white", fg="blue")
rules7 = Label(root, text='Игра на двоих: один за Россию, другой за НЛО', font="Arial 15", bg="white", fg="blue")
rules8 = Label(root, text='НЛО может кидать бомбочки с помощью "a" и "d"', font="Arial 15", bg="white", fg="blue")
rules2 = Label(root, text='Пушка может стрелять', font="Arial 15", bg="white", fg="blue")
rules9 = Label(root, text='с помощью правой и левой кнопок мыши', font="Arial 15", bg="white", fg="blue")
rules3 = Label(root, text='Каждый инопланетянин погибает', font="Arial 15", bg="white", fg="blue")
rules4 = Label(root, text='только от одного вида снарядов', font="Arial 15", bg="white", fg="blue")
rules5 = Label(root, text='Используй стрелки, чтобы двигать пушку', font="Arial 15", bg="white", fg="blue")
rules6 = Label(root, text='Чтобы начать, нажми "начать"', font="Arial 15", bg="white", fg="blue")
rules1.place(x=65, y=100)
rules7.place(x=35, y=150)
rules8.place(x=25, y=175)
rules2.place(x=125, y=200)
rules9.place(x=60, y=225)
rules3.place(x=90, y=250)
rules4.place(x=90, y=275)
rules5.place(x=60, y=300)
rules6.place(x=100, y=325)


def konec():
    quit()

def finish():
    root.geometry('500x300')
    fra2 = Frame(root, width=600, height=600, bg="white")
    fra2.place(x=0, y=0)
    b2 = Button(text='Конец', width=70, height=6)
    b2.config(command=konec)
    b2.place(x=0, y=0)
    rules6 = Label(root, text='Ты уничтожил всех инопланетян\n и спас Россию!\n Молодец!!!', font="Arial 15", bg="white", fg="blue")
    rules6.place(x=100, y=100)

def lose():
    root.geometry('550x300')
    fra3 = Frame(root, width=650, height=600, bg="white")
    fra3.place(x=0, y=0)
    b3 = Button(text='Конец', width=77, height=6)
    b3.config(command=konec)
    b3.place(x=0, y=0)
    rules7 = Label(root, text='Ты не справился', font="Arial 15", bg="white", fg="blue")
    rules8 = Label(root, text='Из-за тебя инопланетяне захватили Россию и весь мир', font="Arial 15", bg="white", fg="blue")
    rules9 = Label(root, text='молодец, ага!!!', font="Arial 15", bg="white", fg="blue")
    rules7.place(x=180, y=110)
    rules8.place(x=20, y=135)
    rules9.place(x=185, y=160)
    
def new_game(event=''):
    '''Функция самой игры'''
    global gun, screen1, balls, balls1, bullet, bombs
    t1.new_target1('white')
    t2.new_target('black')
    bullet = 0
    balls = []
    balls1 = []
    bombs = []
    
    '''Связываем функции пушки с кнопками'''
    canv.bind('<Button-1>', g1.fire2_start)                          
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<Button-3>', g1.fire1_start)
    canv.bind('<ButtonRelease-3>', g1.fire1_end)
    
    canv.focus_set()
    canv.bind('<Right>', g1.gun_move_right)
    canv.bind('<Left>', g1.gun_move_left)

    canv.bind('d', t1.bomb1)
    canv.bind('a', t2.bomb2)
    
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls1 or balls:
        if t1.live > 0 :
            t1.target1_move()
        if t2.live > 0 :
            t2.target_move()
        if t1.hittest(g1):
            lose()
        if t2.hittest(g1):
            lose()
        for b in bombs:
            b.move()
        for i in range(len(bombs)):
            if bombs[i].live <= 0:
                bombs[i].delete()
                bombs[i] = None 
        bombs = [bomb for bomb in bombs if bomb is not None]
    
        '''Белый шарик связан с правой кнопкой - номер 2?'''
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
                canv.itemconfig(screen1, text='Ты уничтожил НЛО за ' + str(bullet) + ' выстрел(-а)/(-ов)')
        for i in range(len(balls1)):
            if balls1[i].live <= 0:
                balls1[i].delete()
                balls1[i] = None 
        balls1 = [ball for ball in balls1 if ball is not None]

        '''Черный шарик связан с левой кнопкой мыши - номер 1'''
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
                canv.itemconfig(screen1, text='Ты уничтожил НЛО за ' + str(bullet) + ' выстрел(-а)/(-ов)')
        for i in range(len(balls)):
            if balls[i].live <= 0:
                balls[i].delete()
                balls[i] = None
        balls = [ball for ball in balls if ball is not None]
                
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)


root.mainloop()
