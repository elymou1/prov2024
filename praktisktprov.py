# Author: Elyas Mounir
# Date: 2024-09-25

def main():
    input_values = input("skriv siffra eller siffror: ")
    if not input_values.strip():
        return
    numbers = [int(num) for num in input_values.split()]
    for num in numbers:
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        print()

if __name__ == "__main__":
    main()