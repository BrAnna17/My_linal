from math import*
import numpy as np
import matplotlib.pyplot as plt
g= 9.81
class System:
    def __init__(self):
        self.k=20#жесткость пружины, Н/м
        self.m1=1#масса грузика на пружине, кг
        self.m2=1#масса грузика на стержне, кг
        self.l=1#длина стержня, м
        self.fi0=radians(pi/3)#начальный угол отклонения стержня от вертикали, отчситывается по часовой стрелке
        self.x0=0#начальная икс-координата пружынного маятника
        self.fi0dot=radians(0)# -- это штрих, производная
        self.x0dot=0#
        self.dt=0.001#время между итерациями
        self.x=self.x0#текущая икс-координата пружынного маятника
        self.fi=self.fi0#текущий угол отклонения стержня
        self.t=1#конечное время
        self.xdot=self.x0dot#скорость бруска
        self.fidot=self.fi0dot#скорость грузика
        self.xdotdot=0
        self.fidotdot=0
    def linalequation(self):
        a1=self.m1+self.m2
        a2=self.m2*self.l*cos(self.fi)
        a3=a2
        a4=self.m2*self.l
        b1=self.m2*self.l*self.fi**2*sin(self.fi)+self.k*self.x
        b2=self.m2*self.l*self.xdot*self.fidot*(cos(self.fi)+sin(self.fi))+self.m2*g*self.l*sin(self.fi)
        A=np.array([[a1,a2],[a3,a4]])
        B=np.array([b1,b2])
        X=np.linalg.solve(A,B)#вектор углового ускорения и ускорения груза
        self.fidotdot=X[1]
        self.xdotdot=X[0]
        print(X)
    def solution(self):
        for i in range(0,ceil(self.t/self.dt),1):
           self.linalequation()
           self.xdot= self.xdot+self.xdotdot*self.dt
           self.fidot = self.fidot + self.fidotdot* self.dt
           self.x = self.x+self.xdot*self.dt
           self.fi = self.fi + self.fidot * self.dt
           self.x0=self.x
           self.x0dot=self.xdot
           self.fi0=self.fi
           self.fi0dot=self.fidot

a=System()
a.solution()
