#测试工厂模式

#定义车工厂类
class Carfactory:
    #定义生产汽车的方法
    def creatcar(self,brand):
        if brand=="奔驰":
            return Benz()
        elif brand=="宝马":
            return BMW()
        elif brand=="比亚迪":
            return BYD()
class Benz:
    print("奔驰大G")
class BMW:
    print("宝马X6")
class BYD:
    print("SUV宋")
#创建工厂对象
factory=Carfactory()
c1=factory.creatcar("奔驰")
c2=factory.creatcar("宝马")
c3=factory.creatcar("比亚迪")
print(c1)
print(c2)
print(c3)