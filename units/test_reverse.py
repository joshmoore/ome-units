import pytest
from conversions import Conversions


def list_converted_units():
    """List all conversion keys as (category, from_unit) tuples"""
    keys = []
    categories = Conversions.keys()
    for category in categories:
        conversion_dict = Conversions[category]
        for to_unit in conversion_dict.keys():
            keys.append((category, to_unit))
    return keys


def list_conversions():
    """List all conversions as (category, from_unit, to_unit) tuples"""
    keys = []
    for category, to_unit in list_converted_units():
        for from_unit in Conversions[category][to_unit].keys():
            keys.append((category, to_unit, from_unit))
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


converted_units = list_converted_units()
converted_units_ids = ["-".join(x) for x in converted_units]
conversions = list_conversions()
conversion_ids = ["-".join(x) for x in conversions]


class TestReverse(object):

    @pytest.mark.parametrize('key', converted_units, ids=converted_units_ids)
    def test_self_transform(self, key):
        category, to_unit = key
        assert Conversions[category][to_unit][to_unit] == ()

    @pytest.mark.parametrize('key', conversions, ids=conversion_ids)
    def test_reverse_transform(self, key):
        category, from_unit, to_unit = key
        assert from_unit in Conversions[category][to_unit]

        forward_transform = Conversions[category][from_unit][to_unit]
        reverse_transform = Conversions[category][to_unit][from_unit]

        assert reverse_transform == get_reverse_transform(forward_transform)
