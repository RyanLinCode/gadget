from dice import Dice

dice_x=Dice()
dice_y=Dice()

results = []

for roll_num in range(100):
    result = dice_x.roll() + dice_y.roll()
    results.append(result)

    # print(results)

max_result=dice_x.num_sides+dice_y.num_sides
frequencies=[]

for vaule in range(1,max_result):
    frequencie=results.count(vaule)
    frequencies.append(frequencie)

# print(frequencies)