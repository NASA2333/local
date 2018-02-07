'''
#企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
# def Bonus(monthly_profit):
#     if monthly_profit<=10:
#         bonus = monthly_profit*0.1
#         return bonus
#     elif monthly_profit >=10 and monthly_profit <20:
#         bonus = 10*0.1+(monthly_profit-10)*0.075
#         return bonus
#     elif monthly_profit >=20 and monthly_profit <40:
#         bonus = 10*0.1+(20-10)*0.075+(monthly_profit-20)*0.05
#         return bonus
#     elif monthly_profit >=40 and monthly_profit <60:
#         bonus = 10*0.1+(20-10)*0.075+(40-20)*0.05+(monthly_profit-40)*0.03
#         return bonus
#     elif monthly_profit >=60 and monthly_profit <100:
#         bonus = 10*0.1+(20-10)*0.075+(40-20)*0.05+(60-40)*0.03+(monthly_profit-60)*0.015
#         return bonus
#     elif monthly_profit >=100:
#         bonus = 10*0.1+(20-10)*0.075+(40-20)*0.05+(60-40)*0.03+(100-60)*0.015+(monthly_profit-100)*0.01
#         return bonus
#     else:
#         print("月利润输入不正确，请重新输入")
#
#
# if __name__=="__main__":
#      monthly_profit = int(input("请输入月利率，单位万元"))
#      bonus = Bonus(monthly_profit)
#      print("当前月利率为 %s万元,应发放奖金总数为 %s万元"%(monthly_profit,bonus))
# [0,100000,200000,400000]


monthly_profit1 = [100,60,40,20,10,0]
list1 = [0.01,0.015,0.03,0.05,0.075,0.1]

monthly_profit = int(input("请输入月利率"))
b = 0
for i in range(len(monthly_profit1)):
    if monthly_profit>=monthly_profit1[i]:
        b1 = (monthly_profit-monthly_profit1[i])*list1[i]
        b = b+b1
        monthly_profit= monthly_profit1[i]
print("应发年终奖%s万元"%b)
