import inspect
import functools
import random
import unittest


def with_chance(probability, default_value):
    """
    Function decorator.
    Returns the result of the function with a specified probability, or returns the default value.
    :param probability:
    :param default_value:
    """
    assert isinstance(probability, int), 'chance_value must be integer.'
    assert 1 <= probability <= 99, 'chance_value must be from 1 to 99.'

    is_function_chances = [True] * probability + [False] * (100 - probability)

    def with_chance_decorator(func):
        assert inspect.isfunction(func), 'Decorator with_chance for functions only.'

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) if random.choice(is_function_chances) else default_value

        return wrapper

    return with_chance_decorator


class TestChanceDecorator(unittest.TestCase):
    """
    Tests for with_chance decorator.
    """

    def test_probability_max_value(self):
        with self.assertRaises(AssertionError):
            @with_chance(100, "Default Value")
            def some_fn():
                pass

            some_fn()

    def test_probability_min_value(self):
        with self.assertRaises(AssertionError):
            @with_chance(0, "Default Value")
            def some_fn():
                pass

            some_fn()

    def test_probability_type_value(self):
        with self.assertRaises(AssertionError):
            @with_chance(50.2, "Default Value")
            def some_fn():
                pass

            some_fn()

    def test_decorate_class(self):
        with self.assertRaises(AssertionError):
            @with_chance(50, "Default Value")
            class SomeClass:
                pass

    def test_call_decorated_function(self):
        default_value = "default value"

        @with_chance(50, default_value)
        def sqr(x):
            return x * x

        value_for_test = 3
        result = sqr(value_for_test)
        self.assertTrue((result == value_for_test ** 2) or result == default_value)


if __name__ == "__main__":
    unittest.main()
