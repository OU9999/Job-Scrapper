def tax_cal(money):
    return money*0.35

def pay_tax(tax):
    print("세금은",tax,"입니다.")

to_pay=tax_cal(15000)
pay_tax(to_pay)