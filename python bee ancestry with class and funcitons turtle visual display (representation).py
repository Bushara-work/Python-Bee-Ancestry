#note child in this case meas the dots/bees that re tin the level/layer below itself, whereever child is denoted it is that dot/bee's parent(s)

#import necessary modules
from turtle import Screen, Turtle

#could be used for changing the rounding and such of the results of the maths operations used
#import math

#Create the Dot class with the 
class Dot:
    # use a method to initialise x,y positon atributes along side ites gender children and level
    def __init__(self, x, y, gender, level):
        self.x = x
        self.y = y
        self.gender = gender
        self.level = level
        self.children = []

    #Use a function method to draw the dot int the correct space, move the drawing pen up (aka dont draw) move it to the position that the dot is attributed then draw the dot color it according to the gender
    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        color = "blue" if self.gender == "Male" else "red"
        t.dot(10, color)

    #connect the dots with whatever children it has 
    def connect_to_children(self, t):
        for child in self.children:
            t.penup()
            t.goto(self.x, self.y)
            t.pendown()
            t.goto(child.x, child.y)
            child.draw(t)
            child.connect_to_children(t)

#return the number of ancesters 0 for 0 gen 1 for 1 gen and otherwise calculate via adding the ancestors that are in the gen before andbefore that then combining them
def count_ancestors(generations):
    if generations <= 1:
        return 1
    else:
        return count_ancestors(generations - 1) + count_ancestors(generations - 2)

#calculate the amount of ancestors by repeating 
def calculate_ancestors(generations):
    ancestors = []
    for gen in range(generations + 1):
        ancestors.append(count_ancestors(gen))
    return ancestors


def print_generations(t, generations):
    #calculate the ancestors in the e
    ancestors = calculate_ancestors(generations)

    #centred x and y vlues -- defult
    y = 207
    x = -20

    #move the generations and ancestor information to the left if the generations is 6 or below (since the graph is small and the text can fit to the side and remain on screen)
    if generations < 7:
        x = -260

    #If the generations are 7 or higher then use the defult x and yvalues the generations and ancestor count (since the space between the middle dots is large enough)
    
    #for every level/ generation print the generation and the corresponding amount of ancestors that re in the generation print each line below the one befroe wit some distance
    for level in range(generations + 1):
        num_ancestors = ancestors[level]
        t.penup()
        t.goto(x, y-10)
        t.write(f"{num_ancestors} ancestors:    Gen {level}", align="center", font=("Arial", 12, "normal"))
        y -= 40

def create_fibonacci_tree(level, max_level, gender, x, y, spacing):
    if level > max_level:
        return None
    
    dot = Dot(x, y, gender, level)
    
    #if the layer/level is not the final one add the children dots (bees parent(s)) 
    if level < max_level:
        if gender == "Male":
            child = create_fibonacci_tree(level + 1, max_level, "Female", x, y - 40, spacing / 2)
            if child:
                dot.children.append(child)
        else:
            child1 = create_fibonacci_tree(level + 1, max_level, "Male", x - spacing, y - 40, spacing / 2)
            child2 = create_fibonacci_tree(level + 1, max_level, "Female", x + spacing, y - 40, spacing / 2)
            if child1:
                dot.children.append(child1)
            if child2:
                dot.children.append(child2)
    
    return dot

def main():
    #create the screen window and set its sizse
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.screensize(2000, 2000)  # Set the virtual canvas size
    screen.title("Fibonacci Tree") #title the window
    
    #initialise another window with the title input that requests the generation
    #terminates if a non number entity is entered
    generations = int(screen.textinput("Input", "Enter the number of generations: "))
    
    t = Turtle()
    t.hideturtle()
    t.speed(0)

    # Display the generations teh user entered and number of ancestors in that generation at the top of the window
    ancestors = calculate_ancestors(generations)
    t.penup()
    t.goto(0, 250)
    t.write(f"Generation: {generations}, Ancestors: {ancestors[-1]}", align="center", font=("Arial", 16, "bold"))
    
    #determine the intial spacing between dots by taking into consideraton the generations given (makes the distance between the earliest dots larger as generation # is increased) ---could be improved since the intital distance grows fairly quickly alongside the shortening of the distance with each subsequent generation
    #prevents the dots or connections from over lapping
    initial_spacing = 7 * (2 ** (generations - 1))
    root = create_fibonacci_tree(0, generations, "Male", 0, 200, initial_spacing)
    if root:
        root.draw(t)
        root.connect_to_children(t)
    
    print_generations(t, generations)

    # Add scrollbars
    canvas = screen.getcanvas()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    screen.mainloop()

#run the main loop
if __name__ == "__main__":
    main()
