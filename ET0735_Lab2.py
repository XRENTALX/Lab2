def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")


def get_user_input():
    num = input()
    num_split = num.split()
    num_list = num_split
    print(num_list)
    num_list = list(map(float, num_list))
    return num_list


def calc_average(num_list):
    num_average = sum(num_list)/len(num_list)
    print("Average number is:", num_average)


def find_min_max():
    print("find_min_max")


def sort_temperature():
    print(sort_temperature)


def calc_median_temperature():
    print("calc_median_temperature")


if __name__ == "__main__":
    main()



