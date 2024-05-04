#As a point of creativity I've added a color system to mark the results
#that will appear. This way, all the minimum rates are in red,
#all the maximum rates are in green and the average calculation is in blue. 
#Another thing I thought would be interesting was to make it clear which years are
#available in the file that python is reading, so it's easier to understand in which
#year starts and which year ends.

highest_expectancy = float(0)
lowest_expectancy = float(99999)
user_choice_highest = float(0)
user_choice_lowest = float(99999)
average = []
vermelho= ("\033[1;31m")
verde= ("\033[1;32m")
azulclaro= ("\033[1;34m")
branco=('\033[1;30m')

choice = int(input("Enter the year of interest (1543-2019): "))
with open ("life-expectancy.csv") as data_analysis:
    next(data_analysis)
    for line in data_analysis:
        data = line.strip().split(",")
        Entity = data[0]
        year = int(data[2])
        number = float(data[3])
        #print(f"Entity: {data[0]}, Code: {data[1]}, Year: {data[2]}, Life expectancy: {data[3]} (years)")
        if number > highest_expectancy:
            highest_expectancy = number
            country_highest = Entity
            year_highest = year
        if number < lowest_expectancy:
            lowest_expectancy = number
            country_lowest = Entity
            year_lowest = year
        if choice == year:
            average.append(number)
            if number > user_choice_highest:
                user_choice_highest = number
                user_country_highest = Entity
            if number < user_choice_lowest:
                user_choice_lowest = number
                user_country_lowest = Entity
print(f"{branco}")
print(f"The average life expectancy across all countries was:{azulclaro} {sum(average) / len(average):.2f} {branco}")
print(f"The max life expectancy was in:{verde} {user_country_highest} with {user_choice_highest} {branco}")
print(f"The min life expectancy was in:{vermelho} {user_country_lowest} with {user_choice_lowest} {branco}")
print()
print(f"The overall max life expectancy is:{verde} {highest_expectancy} from {country_highest} in {year_highest} {branco}")
print(f"The overall min life expectancy is:{vermelho} {lowest_expectancy} from {country_lowest} in {year_lowest} {branco} ")
print()

