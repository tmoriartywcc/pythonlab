def main():

    population_file = open('USPopulation.txt','r')
    population = population_file.readlines()
    population_file.close()
    average_change(population)
    biggest_inc = greatest_inc(population)
    smallest_inc(biggest_inc,population)

def average_change(population):
    total = 0
    for value in population:
        value = int(value)
        total += value
    average = total / len(population)
    print('The average annual change in population during 1950-1990 is:',format(average,',.0f'),'people')

def greatest_inc(population):
    biggest_inc = 0
    prev_value = population[0]
    prev_value = int(prev_value)
    for value in population:
        value = int(value)
        difference = value - prev_value
        if difference > biggest_inc:
            biggest_inc = difference
        prev_value = value
    print('The year with the greatest increase in population during 1950-1990 is:',format(biggest_inc,',.0f'),'people')
    return biggest_inc

def smallest_inc(biggest_inc,population):
    small_inc = biggest_inc
    prev_value = population[0]
    prev_value = int(prev_value)
    for value in population:
        value = int(value)
        difference = value - prev_value
        print(difference)
        if difference < small_inc:
            small_inc = difference
        prev_value = value
    print('The year with the smallest increase in population during 1950-1990 is:',format(small_inc,',.0f'),'people')

main()