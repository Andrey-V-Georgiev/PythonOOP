import unittest

from IntegerList import IntegerList


class ListTests(unittest.TestCase):

    """
    Operation `add`, should add an element and returns the list.
    If the element is not an integer, a ValueError is thrown
    """

    def test_integer_list_add_operation_add_element_correctly(self):
        self.integer_list = IntegerList()
        self.integer_list.add(3)
        self.assertEqual(self.integer_list.get_data()[0], 3)

    def test_integer_list_add_operation_add_element_at_the_end(self):
        self.integer_list = IntegerList(2, 4, 6)
        self.integer_list.add(8)
        last_element = self.integer_list.get_data()[len(self.integer_list) - 1]
        self.assertEqual(last_element, 8)

    def test_integer_list_operation_add_return_the_data(self):
        self.integer_list = IntegerList()
        self.assertEqual(self.integer_list.add(2), [2])

    def test_integer_list_add_operation_raise_value_error_if_add_string(self):
        self.integer_list = IntegerList()
        with self.assertRaises(ValueError):
            self.integer_list.add('a')

    """
    remove_index operation removes the element on that index and returns it.
    if the index is out of range, an IndexError is thrown
    """

    def test_integer_list_operation_remove_index_return_removed_value(self):
        self.integer_list = IntegerList(1, 2, 3, 4)
        self.assertEqual(self.integer_list.remove_index(1), 2)

    def test_integer_list_operation_remove_index_remove_element_correctly(self):
        self.integer_list = IntegerList(1, 2, 3, 4)
        length_before = len(self.integer_list.get_data())
        self.integer_list.remove_index(1)
        length_after = len(self.integer_list.get_data())
        self.assertEqual(length_before, length_after + 1)

    def test_integer_list_operation_list_remove_on_un_existing_index_raise_index_error(self):
        self.integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(3)

    """
    __init__ should only take integers, and store them
    """

    def test_integer_list_constructor_take_integers_only(self):
        self.integer_list = IntegerList(1, 'a', 3, 'b')
        self.assertEqual(len(self.integer_list.get_data()), 2)

    def test_integer_list_constructor_initialize_correct_with_no_params(self):
        self.integer_list = IntegerList()
        self.assertEqual(len(self.integer_list.get_data()), 0)

    """
    get should return the specific element
    if the index is out of range, an IndexError is thrown
    """

    def test_integer_list_operation_get_return_correct_result(self):
        self.integer_list = IntegerList(1, 2, 3, 4)
        self.assertEqual(self.integer_list.get(2), 3)

    def test_integer_list_operation_get_on_un_existing_index_raise_index_error(self):
        self.integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            self.integer_list.get(3)

    """
    insert
    if the index is out of range, IndexError is thrown
    if the element is not an integer, ValueError is thrown
    """

    def test_integer_list_operation_insert_on_proper_index(self):
        self.integer_list = IntegerList(1, 2, 3)
        old_first_value = self.integer_list.get_data()[0]
        self.integer_list.insert(0, 9)
        new_first_value = self.integer_list.get_data()[0]
        self.assertNotEqual(old_first_value, new_first_value)

    def test_integer_list_operation_insert_on_un_existing_index_raise_index_error(self):
        self.integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            self.integer_list.insert(10, 5)

    def test_integer_list_insert_operation_raise_value_error_if_insert_string(self):
        self.integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError):
            self.integer_list.insert(2, 'a')

    """
    get_biggest
    """

    def test_integer_list_operation_get_biggest_return_the_biggest_integer_in_the_list(self):
        self.integer_list = IntegerList(1, 2, 3)
        self.assertEqual(self.integer_list.get_biggest(), 3)

    """
    get_index
    """

    def test_integer_list_operation_get_index_return_the_index_of_element(self):
        self.integer_list = IntegerList(1, 2, 3)
        self.assertEqual(self.integer_list.get_index(3), 2)


if __name__ == '__main__':
    unittest.main()
