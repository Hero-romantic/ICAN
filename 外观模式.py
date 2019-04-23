class wakeup:
    def run(self):
        print("起床...")
class bursh:
    def run(self):
        print("刷牙... 洗脸...")
class go:
    def run(self):
        print("拿上书包...去教室")
##外观类中封装了对子系统的操作
class facade:
    def __init__(self):
        self.wakeup_1=wakeup()
        self.brush_2=bursh()
        self.go_3=go()
    def runall(self):
        self.wakeup_1.run()
        self.brush_2.run()
        self.go_3.run()
if __name__=="__main__":
     facade=facade()
     facade.runall()

