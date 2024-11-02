# TODO  Напишите функцию count_letters

def count_letters (text):
    lower_text = text.lower()
    dict_count = {}
    for i in lower_text:
        if i.isalpha():
            if i in dict_count:
                dict_count[i] += 1
            else:
                dict_count[i] = 1
    return dict_count


# TODO Напишите функцию calculate_frequency

def calculate_frequency (dict_):
    dict_frequency = {}
    sum_letters = sum(dict_.values())
    for item_, value_ in dict_.items():
        dict_frequency[item_] = value_/sum_letters
    return dict_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dict_count_ = count_letters(main_str)
dict_frequency_ = calculate_frequency(dict_count_)

for item, value in dict_frequency_.items():
    print(f"{item}: {value:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
