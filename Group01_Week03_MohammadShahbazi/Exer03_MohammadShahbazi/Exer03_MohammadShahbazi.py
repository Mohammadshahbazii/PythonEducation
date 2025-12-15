problem_time = [55,40,28,35,8,30,60,12,45,25]

complicated_times = 0

for item in problem_time :
    if item > 30 :
        complicated_times += item

hours = complicated_times // 60
minutes = complicated_times % 60 
print(f"{hours:02d}:{minutes:02d}")