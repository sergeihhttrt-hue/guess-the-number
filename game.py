import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его за 10 попыток!")
    
    secret_number = random.randint(1, 100)
    attempts = 10
    
    while attempts > 0:
        print(f"\nУ вас осталось {attempts} попыток.")
        
        try:
            guess = int(input("Введите ваше предположение (1-100): "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue
            
        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100!")
            continue
            
        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number}!")
            return
            
        if guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
            
        attempts -= 1
    
    print(f"\nК сожалению, вы не угадали. Загаданное число было {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
