def pay(usage):
    br = 0.6

    if usage < 100:
        return usage * br * 0.8
    elif 100 <= usage <= 150:
        return usage * br
    elif 150 < usage <= 250:
        return 150 * br + (usage - 150) * br * 1.3
    else:
        return 150 * br + 100 * br * 1.3 + (usage - 250) * br * 1.5


if __name__ == "__main__":
    usage = float(input("请输入本月用电量(度): "))
    bill = pay(usage)
    print(f"本月用电量: {usage}度")
    print(f"应缴电费: {bill:.2f}元")
