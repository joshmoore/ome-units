import pytest
from conversions import Conversions


def find_all_conversions():
    """List all conversion keys as (category, from_unit, to_unit) tuples"""
    keys = []
    categories = Conversions.keys()
    for category in categories:
        conversion_dict = Conversions[category]
        for to_unit in conversion_dict.keys():
            for from_unit in conversion_dict[to_unit].keys():
                keys.append((category, from_unit, to_unit))
    return keys


def get_reverse_transform(transform):
    """Compute reverse transform"""

    # Handle self-transforms
    if not transform:
        return ()

    # Temporararily handle undefined transforms
    if not transform[0]:
        return (None, )

    return (
        (-transform[0][0], transform[0][1]),
        (transform[1][0], -transform[1][1]))


conversion_keys = find_all_conversions()
conversion_ids = ["-".join(x) for x in conversion_keys]


class TestReverse(object):

    @pytest.mark.parametrize('key', conversion_keys, ids=conversion_ids)
    def test_reverse_transform(self, key):
        category, from_unit, to_unit = key
        assert from_unit in Conversions[category][to_unit]

        forward_transform = Conversions[category][from_unit][to_unit]
        reverse_transform = Conversions[category][to_unit][from_unit]

        assert reverse_transform == get_reverse_transform(forward_transform)
