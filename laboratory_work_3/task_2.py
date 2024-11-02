# TODO Напишите функцию find_common_participants

def find_common_participants (str1, str2, str3 = ","):
        first_group = set(str1.split(str3))
        second_group = str2.split(str3)
        set_result = first_group.intersection(second_group)
        common_participants = []
        for i in set_result:
            common_participants.append(i)
        common_participants.sort()
        return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print (find_common_participants (participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
