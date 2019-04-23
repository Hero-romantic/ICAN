from abc import ABCMeta, abstractmethod
# 主题
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass
# 真实主题
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self):
        self.account = self.card  # 假定卡号就是账户
        return self.account
    def __hasFunds(self):
        print("银行：核对账户", self.__getAccount(), "一百万")
        return True
    def setCard(self, card):
        self.card = card
    def do_pay(self):
        if self.__hasFunds():
            print("银行:商家付款")
            return True
        else:
            print("银行::对不起，没钱")
            return False
# 代理
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input("代理:输入卡号")
        self.bank.setCard(card)
        return self.bank.do_pay()
# 客户端
class You:
    def __init__(self):
        print("You: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    def __del__(self):
        if self.isPurchased:
            print("你: 这车我买了")
        else:
            print("你: 我应该赚更多的钱:(")
you = You()
you.make_payment()

