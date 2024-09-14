# Function to calculate the number of ancestors in a given generation
def calculate_ancestors(generation):
    if generation == 0:
        return 1  # The initial male honeybee
    elif generation == 1:
        return 1  # The mother of the initial male honeybee
    else:
        # Using the Fibonacci sequence to calculate ancestors
        a, b = 1, 1
        for _ in range(2, generation + 1):
            a, b = b, a + b
        return b


# Main program
def main():
    #repeat until a valid (interger only) response is given
    while True:
        try:
            # Taking user input for the number of previous generations
            generations = int(input("Enter the number of previous generations: "))
            if generations < 0:
                print("Please enter a non-negative integer.")
                return

            # Calculating and displaying the number of ancestors
            ancestors = calculate_ancestors(generations)
            print(f"The number of ancestors in generation {generations} is: {ancestors}")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        else:
            break

# Running the main program
if __name__ == "__main__":
    main()
