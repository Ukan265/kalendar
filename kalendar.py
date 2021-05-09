import calendar
yil=int(input("Yilni kiriting:"))
oy=int(input("Qaysi oy kerak:(Iltimos son ko'rinishida yozing!)"))
kun = int(input("qaysi kun kerak:"))
print(calendar.month(yil, oy,kun))
