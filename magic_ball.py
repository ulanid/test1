import random

# Базовий список відповідей чарівної кулі
magic_ball_answers = [
    "Yes.",
    "No.",
    "Ask again later.",
    "Cannot predict now.",
    "Most likely.",
]

# Функція для імітації чарівної кулі передбачення
def charivna_kulka(question):
    if not question or not isinstance(question, str):
        raise ValueError("Invalid input: Please provide a non-empty string question.")
    answer = random.choice(magic_ball_answers)
    return answer

# Функція для створення чарівної кулі з додатковими відповідями та скоригованими ймовірностями
def set_up_magic_ball(additional_answers=[], probabilities={}):
    global magic_ball_answers
    
    # Обчислення загальної ймовірності
    total_probability = sum(probabilities.values())
    
    # Нормалізація ймовірностей, якщо вони в сумі не дорівнюють 1
    if total_probability != 1:
        for answer in probabilities:
            probabilities[answer] /= total_probability
    
    # Додавання додаткових відповідей до базового списку
    magic_ball_answers.extend(additional_answers)
    
    # Налаштування ймовірності наявних або доданих відповідей
    for answer, probability in probabilities.items():
        if answer in magic_ball_answers and 0 <= probability <= 1:
            index = magic_ball_answers.index(answer)
            magic_ball_answers.pop(index)
            magic_ball_answers.insert(index, answer)
            for _ in range(int(probability * 100) - 1):
                magic_ball_answers.insert(index, answer)

# Перевірка програми
if __name__ == "__main__":
    # Введення питання чарівній кулі
    question = input("Ask the magic ball a question: ")
    answer = charivna_kulka(question)
    print("Magic Ball says:", answer)
    
