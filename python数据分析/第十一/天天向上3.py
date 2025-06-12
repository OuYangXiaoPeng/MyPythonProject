dayup = 1.0
dayfactory = 0.01

for i in range(365):
    if i % 7 in [0, 6]:
        dayup = dayup * (1 - dayfactory)
    else:
        dayup = dayup * (1 + dayfactory)

print("工作日的力量:{:.2f}".format(dayup))
