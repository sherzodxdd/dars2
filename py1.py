# def yigindi(son1, son2):
#     natija = son1 + son2
#     return f"Yig'indi: {natija}"

# son1 = int(input("Sonni kiriting: "))
# son2 = int(input("Sonni kiriting: "))

# print(yigindi(son1, son2))

# --------------------------------------------------

# def yosh_hisobla(t_yil):
#     natija = 2025 - t_yil
#     if natija <= 5:
#         return f"Assolomu alaykum siz {natija} yoshda ekansiz \nQalaysiz baby?"
#     else:
#         return f'Assolomu alaykum siz {natija} yoshda ekansiz'
# yosh = int(input("yoshingizni kiriting: "))

# print(yosh_hisobla(yosh))

def calculator(son1, son2, belgi):
    if belgi == "+":
        return f"Yig'indi: {son1 + son2}"
    elif belgi == "-":
        return f"Ayirma: {son1 - son2}"
    elif belgi == "*":
        return f"Kopaytma: {son1 * son2}"
    elif belgi == "/":
        return f"Bo'linma: {son1 / son2}"
    else:
        return f"Qiymat xato kiritildi"
son1 = float(input("1-Sonni kiriting: "))
son2 = float(input("2-Sonni kiriting: "))
belgi = input("belgini kiriting: ")

print(calculator(son1, son2, belgi))