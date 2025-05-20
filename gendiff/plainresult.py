from structuregenerator import KEYS


def plain_formater(structure):
    lines = []
    all_keys = KEYS[1]

    for all_key in all_keys:

        for structure_key in structure:

            if all_key in structure[structure_key].keys():
                main_dictionary = structure[structure_key]

                if structure_key == 'unchanged' or structure_key == 'added':
                    key_dict = main_dictionary[all_key]
                    lines.append(f"Property {all_key} was added with value: {key_dict['value']}")

                elif structure_key == 'changed':
                    key_dict = main_dictionary[all_key]
                    print(f"Changed dict is {key_dict}")
                    old_value = key_dict['old']
                    new_value = key_dict['new']
                    print(key_dict)
                    lines.append(f"Property {all_key} was updated. "
                                  f"From {old_value['value']} to {new_value['value']}")

                elif structure_key == 'removed':
                    lines.append(f"Property {all_key} was removed")

                elif structure_key == 'nested':
                    lines.append(f"Property {all_key} was added with value: [complex value]")


    return lines

