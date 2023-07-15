farm_file = open('farm.txt')
sheep = farm_file.readline()
pig = farm_file.readline()
duck = farm_file.readline()

print(f'Общее количество ног всех животных: {int(sheep) * 4 + int(pig) * 4 + int(duck) * 2}')

farm_file.close()