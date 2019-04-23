#单例模式
class Mysingleton:
    #这个类创建的单例，通常用属性保存
    object=None
    #加标记，保证初始化一次
    __init_flag=True
    def __new__(cls, *args, **kwargs):
        #cls(当前类对象)，判断cls下的属性是否为空
        if cls.object==None:
            #调用obj父类的创建方式，然后传进类
            cls.object=object.__new__(cls)
        return cls.object
    #属性重写
    def __init__(self,name):
        if Mysingleton.__init_flag==True:
            print("初始化")
            Mysingleton.__init_flag=False
            self.name=name
a=Mysingleton("姚")
b=Mysingleton("曾")
print(a)
print(b)
