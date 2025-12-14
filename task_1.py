from itertools import count

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count=0
while True:
    a=money_capital+salary
    if a>=spend:
        money_capital=a-spend
        count+=1
        spend*=(1+increase)
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", count)