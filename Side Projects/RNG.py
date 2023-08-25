import random

def generate_unique_random_numbers(start_range, end_range, count):
    all_numbers = list(range(start_range, end_range + 1))
    random.shuffle(all_numbers)
    return all_numbers[:count]

if __name__ == "__main__":
    start_range = 0   # Change this to the starting value of your desired range
    end_range = 9    # Change this to the ending value of your desired range
    count = 6         # Change this to the number of random numbers you want to generate
    num_sets = 1     # Change this to the number of sets you want to generate

    for set_num in range(1, num_sets + 1):
        random_numbers = generate_unique_random_numbers(start_range, end_range, count)
        random_number_1_to_10 = random.randint(1, 10)

        print(f"Set {set_num} - Random numbers:", random_numbers)
        print(f"Set {set_num} - Random number from 1 to 10:", random_number_1_to_10)
        print()
