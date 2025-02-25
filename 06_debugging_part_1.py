from test_api.checks import run_test, skip_test, format_err_msg

"""
### get_first_item ###

get_first_item is a function that takes an list and returns the first element.

Unfortunately, it looks like the function is currently throwing a NameError.

Can you work out what needs to be changed to make the function pass all the
tests?
"""


def get_first_item(my_list):
    first_item = my_list[0]
    return firstitem


# Do not change tests!


@run_test
def get_first_item_should_return_first_number_item():
    result = get_first_item([1, 2, 3, 4])
    expected = 1
    assert result == expected, format_err_msg(expected, result)


@run_test
def get_first_item_should_return_first_string_item():
    result = get_first_item(["black", "khaki", "cyan"])
    expected = "black"
    assert result == expected, format_err_msg(expected, result)


"""
### split_string ###

split_string is a function that takes a string and returns a list containing
all of the individual characters as separate elements.

Unfortunately, it looks like the function is currently throwing a TypeError.

Can you work out what needs changing to make the function pass all the tests?
"""


def split_string():
    return list(str)


# Do not change tests!


@skip_test
def split_string_should_split_lowercase_string():
    result = split_string("string")
    expected = ["s", "t", "r", "i", "n", "g"]
    assert result == expected, format_err_msg(expected, result)


@skip_test
def split_string_should_split_titlecase_string():
    result = split_string("Northcoders")
    expected = ["N", "o", "r", "t", "h", "c", "o", "d", "e", "r", "s"]
    assert result == expected, format_err_msg(expected, result)


"""
add_bread is a function that takes a dictionary describing a `person`
and a string of their favourite bread, and returns that object with a
new property (`fave_bread`) set to a value of their favourite bread.

If no favourite bread is given then the default fave_bread is 'granary'.

Unfortunately, it looks like the function has a couple of issues with
the way it's written.

Can you work out what needs changing to make the function pass all the tests?
"""


def add_bread(person, loaf):
    person["loaf"] == loaf
    return


# Do not change tests!
@skip_test
def add_bread_should_add_favourite_bread_rye():
    result = add_bread({"name": "Joe"}, "rye")
    expected = {"name": "Joe", "fave_bread": "rye"}
    assert result == expected, format_err_msg(expected, result)


@skip_test
def add_bread_should_add_favourite_bread_granary():
    result = add_bread({"name": "Paul"}, "granary")
    expected = {"name": "Paul", "fave_bread": "granary"}
    assert result == expected, format_err_msg(expected, result)


@skip_test
def add_bread_should_add_default_favourite_bread_granary():
    result = add_bread({"name": "Poonam"})
    expected = {"name": "Poonam", "fave_bread": "granary"}
    assert result == expected, format_err_msg(expected, result)


if __name__ == "__main__":
    get_first_item_should_return_first_number_item()
    get_first_item_should_return_first_string_item()

    split_string_should_split_lowercase_string()
    split_string_should_split_titlecase_string()

    add_bread_should_add_favourite_bread_rye()
    add_bread_should_add_favourite_bread_granary()
    add_bread_should_add_default_favourite_bread_granary()
