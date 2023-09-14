class bankaccount:
  def __init__(self,__accountno, __accountname, initiate_balance=0.0):
   self.__accountno =__accountno     
   self.__accountname= __accountname
   self.__accountbalance=initiate_balance
  def deposit (self,amount):
    if amount>0:
      self.__accountbalance+=amount
      print("deposit amount₹{}. account balance ₹{}".format(amount,self.__accountbalance))
    else:
      print("invalid deposit amount {}".format(amount))
  def withdraw (self,amount):
      if amount > 0 and amount>=self.__accountbalance :
        self.__accountbalance-=amount
        print("withdraw amount ,₹{}.New balance ₹{}".format(amount,self.__accountbalance))
      else:
       print("invalid amount")
  def display_balance(self):
    print("Account balance .Account Name{}.Account Number{}. Account balance{}".format(self.__accountname,self.__accountno,self.__accountbalance))
account =bankaccount (1245780,"Bharath",5000.0)
account.display_balance()
account.deposit(2000)
account.withdraw(1500)
account.display_balance()