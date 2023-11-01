with open('numbers.txt', 'w') as file:
    file.write("1 2 3\n")
    file.write("4 5 6\n")
    file.write("7 8 9\n")


def sum_of_numbers(filename):
    try:
        with open(filename, 'r') as file:
            total_sum = 0
            for line in file:
                numbers = line.split()
                for num in numbers:
                    total_sum += float(num)
            print(f"Sum of numbers: {total_sum}")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")


sum_of_numbers('numbers.txt')
