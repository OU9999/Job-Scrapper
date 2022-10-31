# my_name = "eugene"
# my_age = 24
# my_color_eyes = "black"

# print("Hello i'm {my_name}, my age is {my_age}, my eye is {my_color_eyes}")
# print(f"Hello i'm {my_name}, my age is {my_age}, my eye is {my_color_eyes}")

######################################################################################################################################

#return은 함수를 kill 한다 return 이후의 줄은 무시
def make_juice(fruit):
    return f"{fruit} juice"
    print("응가추가")

def add_ice(juice):
    return f"ice {juice}"

def add_sugar(iced_juice):
    return f"sugar {iced_juice}"

juice = make_juice("apple")
print(juice)
cold_juice = add_ice(juice)
print(cold_juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)