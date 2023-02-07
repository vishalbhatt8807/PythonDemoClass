'''By Default a thread will generate when we execute a instance its called Main thread. This is a simple main thread create and execute
one after one now to convert into multithread import Thread and pass argument as Thread with class and instrad of run has to call
start method and just remember use run as method because start has backend run method. still few output is coming like
"Hello studentHi employee" which is called collision to remove this we use sleep also define in between start methods. Now spuppose
you want to print at the end of execute as "Bye" so that has to do via join()'''

from threading import *
from time import sleep

class student(Thread):
    def run(self):
        for i in range(10):
            print("Hellostudent")
            sleep(1)
class employee(Thread):
    def run(self):
        for i in range(10):
            print("Hiemployee")
            sleep(1)

t1 = student()

t2 =  employee()
t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")