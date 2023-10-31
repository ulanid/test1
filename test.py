import pytest
from magic_ball import charivna_kulka, set_up_magic_ball, magic_ball_answers

# Функція повертає одне з очікуваних значень
def test_charivna_kulka_returns_valid_answer():
    answer = charivna_kulka("Will it rain tomorrow?")
    assert answer in magic_ball_answers

# Функція повертає значення типу str
def test_charivna_kulka_returns_str():
    answer = charivna_kulka("Is it going to be a sunny day?")
    assert isinstance(answer, str)

# Відповідь функції на порожнє поле або цифри
def test_charivna_kulka_handles_empty_or_non_string_input():
    with pytest.raises(ValueError):
        charivna_kulka("")
    with pytest.raises(ValueError):
        charivna_kulka(123)

# Введення додаткових відповідей, перевірка чи з'являються щойно додані відповіді у виведенні
def test_set_up_magic_ball_adds_additional_answers():
    additional_answers = ["Absolutely!", "I doubt it."]
    probabilities = {"Yes, definitely.": 0.5, "No, not at all.": 0.5}
    set_up_magic_ball(additional_answers, probabilities)
    assert all(answer in magic_ball_answers for answer in additional_answers)

# Правильність налаштувань ймовірності відповідей
def test_set_up_magic_ball_adjusts_probabilities():
    additional_answers = ["Absolutely!", "I doubt it."]
    probabilities = {"Yes, definitely.": 0.5, "No, not at all.": 0.5}
    set_up_magic_ball(additional_answers, probabilities)
    count_yes = probabilities.get("Yes, definitely.", 0)
    count_no = probabilities.get("No, not at all.", 0)
    total_answers = len(magic_ball_answers)
    assert pytest.approx(count_yes, 0.01) == 0.5
    assert pytest.approx(count_no, 0.01) == 0.5

