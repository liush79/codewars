def michael_pays(costs):
    return round(costs if costs < 5 else costs - 10 if costs / 3.0 > 10 else costs - costs / 3.0, 2)


print michael_pays(15)  # 10
print michael_pays(4)   # 4
print michael_pays(30)  # 20
print michael_pays(80)  # 70
print michael_pays(22)  # 14.67
print michael_pays(5.9181)   # 3.95
print michael_pays(28.789)   # 19.19
print michael_pays(4.325)    # 4.33
