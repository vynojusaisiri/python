from threading import MyThread
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("child class")
t=MyThread()
t.start()
for i in range(5):
    print("main class")