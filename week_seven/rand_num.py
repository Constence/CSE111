import random

def main():
    numbers = [16.2, 75.1, 52.3]
    word = []

    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(word, 1)
    print(word)

    append_random_words(word, 2)
    print(word)


def append_random_numbers(numbers, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        random_number_round = round(random_number, 1)
        numbers.append(random_number_round)

def append_random_words(words_list, quantity=1): 
    words= ['bob', 'cat', 'dog']
    for _ in range(quantity):
        random_word= random.choice(words)
        words_list.append(random_word)
    
main()