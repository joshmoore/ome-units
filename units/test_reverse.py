from conversions import Conversions


def find_all_conversions():
    keys = []
    categories = Conversions.keys()
    for category in categories:
        conversion_dict = Conversions[category]
        for to_unit in conversion_dict.keys():
            for from_unit in conversion_dict[to_unit].keys():
                keys.append((category, from_unit, to_unit))
    return keys

for key in find_all_conversions():
    category, from_unit, to_unit = key
    assert from_unit in Conversions[category][to_unit]
