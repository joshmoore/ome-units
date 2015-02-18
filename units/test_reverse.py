import pytest
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

conversion_keys = find_all_conversions()


class TestReverse(object):

    @pytest.mark.parametrize('key', conversion_keys)
    def test_reverse_transform_exists(self, key):
        category, from_unit, to_unit = key
        assert from_unit in Conversions[category][to_unit]
