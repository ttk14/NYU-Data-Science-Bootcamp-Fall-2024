# Question 1
def count_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    
    return vowel_count


# Question 2
def print_animals_in_allcaps():
    animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

    for animal in animals:
        print(animal.upper())


# Question 3
def print_number_with_parity():
    for number in range(1, 21):
        if number % 2 == 0:
            print(f"{number}, even")
        else:
            print(f"{number}, odd")
            

# Question 4
def sum_of_integers():
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
       
        return (a + b)
    
    except ValueError:
        print("Error! Please enter valid integers.")
        return None

# sum = sum_of_integers()
# if sum is not None:
#     print("The sum is:", sum)