#return the number of ancesteros in the genration given
def count_ancestors(generations):
    #if 1 or 0 return 1
    if generations <= 1:
        return 1
    #other generation value calculate by adding the generaton before its ancestor count and addisng it to the ancestor count befor ethat, (fibonachi sequence) until you get to the generation entered ancestor#
    else:
        return count_ancestors(generations - 1) + count_ancestors(generations - 2)

#print bees distance according to which level/generation it is in and its parent as long as the level/layer is less than the genrations entered
def print_family_tree(generations):
    def print_tree(level, max_level, gender):
        if level > max_level:
            return
        indent = "    " * level
        if gender == "Male":
            print(f"{indent}Male (Gen {level})")
            if level < max_level:
                print_tree(level + 1, max_level, "Female")
        else:
            print(f"{indent}Female (Gen {level})")
            if level < max_level:
                print_tree(level + 1, max_level, "Male")
                print_tree(level + 1, max_level, "Female")
    
    print_tree(0, generations, "Male")


# Main program
def main():
    #repeatedly request for an input until a response conataining only positve integers is recieved
    while True:
        try:
            # Taking user input for the number of previous generations
            # Input: Number of generations
            generations = int(input("Enter the number of previous generations: "))
            if generations <0:
                raise ValueError
        except ValueError:
            print('invalid response')
        else:
            break
    # Calculating and displaying the number of ancestors
    # Output the number of ancestors in the specified generation
    ancestors = count_ancestors(generations)
    print(f"The number of ancestors in generation {generations} is: {ancestors}")
    print("Family tree:")
    print_family_tree(generations)

# Running the main program
if __name__ == "__main__":
    main()
