print("lets go for set our 20 ml pipet full by 3ml drops step by step : ")

current_volume = 0
while current_volume < 20 :
    current_volume += 3
    if current_volume > 20 :
        break
    print("current volume is : ", current_volume, " ml")

print("you have reached the maximum volume of pipet !")