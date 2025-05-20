from structuregenerator import KEYS


def flatten_gen(nested, isatom=lambda x: not isinstance(x, list)):
    for item in nested:
        if isatom(item):
            yield item
        else:
            yield from flatten_gen(item)


def return_string(dictionary, tab):
    if isinstance(dictionary['value'], dict):
        dictionary['value'] = '{'
    return f"{tab}{dictionary['mark']} {dictionary['key']}: {dictionary['value']}"


def stylish_formater(structure, level=1):
    #наша главная строка
    lines = []

    #формируем пробел
    tab = '..' * level

    #тайми вайми с кейс
    KEYS['check_counter'] += 1
    cycle_counter = KEYS['check_counter']
    all_keys = KEYS[cycle_counter]

    for all_key in all_keys:

        for structure_key in structure:

            if all_key in structure[structure_key].keys():
                #value по ключу
                main_dictionary = structure[structure_key]

                if structure_key == 'nested':
                    #value of all_key
                    child_value = main_dictionary[all_key]

                    if isinstance(child_value['value'], dict):
                        lines.append(stylish_formater(child_value['value'], level=level * 2))
                    lines.insert(-1, return_string(child_value, tab))


                elif structure_key == 'changed':
                    for key in main_dictionary[all_key]:
                        little_dict = main_dictionary[all_key]
                        lines.append(return_string(little_dict[key], tab))

                else:
                    lines.append(return_string(main_dictionary[all_key], tab))

    lines.append(f"{'..' * (level-2)}{'}'}")

    return list(flatten_gen(lines))


