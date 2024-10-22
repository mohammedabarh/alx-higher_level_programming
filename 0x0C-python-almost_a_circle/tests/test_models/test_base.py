#!/usr/bin/python3
'''Module containing unit tests for the Base class.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Unit tests for the Base class functionality.'''

    def setUp(self):
        '''Prepare the test environment before each test.'''
        Base._Base__nb_objects = 0  # Reset number of objects before tests
        pass

    def tearDown(self):
        '''Clean up after each test method.'''
        pass

    def test_A_nb_objects_private(self):
        '''Check if nb_objects is a private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Verify that nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Test instantiation of the Base class.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")  # Check class type
        self.assertEqual(b.__dict__, {"id": 1})  # Ensure id is set correctly
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Test the constructor's signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()  # Missing self argument
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Test constructor signature with incorrect number of arguments.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)  # Too many arguments
        msg = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Check that ids are assigned consecutively.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)  # Ensure b2's id follows b1's

    def test_F_id_synced(self):
        '''Test synchronization between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)  # Check id sync

    def test_F_id_synced_more(self):
        '''Test synchronization with multiple instances.'''
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)  # Final check of id sync

    def test_G_custom_id_int(self):
        '''Test assignment of a custom integer id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)  # Check if id is correctly assigned

    def test_G_custom_id_str(self):
        '''Test assignment of a custom string id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)  # Ensure string id is assigned correctly

    def test_G_id_keyword(self):
        '''Test assignment of id via keyword argument.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)  # Verify id assignment

    # ----------------- Tests for #15 ------------------------
    def test_H_to_json_string(self):
        '''Test the to_json_string() method.'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()  # Missing required argument
        s = "to_json_string() missing 1 required positional argument: 'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")  # Check for None input
        self.assertEqual(Base.to_json_string([]), "[]")  # Check for empty list
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244, 'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))  # Compare lengths

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))  # Compare lengths

        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d), '[{"foobarrooo": 989898}]')  # Check JSON output

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d), '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244, 'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))  # Compare lengths

        d = [{}]
        self.assertEqual(Base.to_json_string(d), '[{}]')  # Check single empty dictionary

        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')  # Check two empty dictionaries

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary]).replace("'", '"')  # Format for comparison
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(), r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary).replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary]).replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(), r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary).replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    # ----------------- Tests for #17 ------------------------
    def test_H_test_from_json_string(self):
        '''Test the from_json_string() method.'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()  # Missing required argument
        s = "from_json_string() missing 1 required positional argument: 'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])  # Check for None input
        self.assertEqual(Base.from_json_string(""), [])  # Check for empty string

        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244, 'height': 34340}]
        self.assertEqual(Base.from_json_string(s), d)  # Compare parsed output

        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)  # Check empty dictionaries
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)  # Check single empty dictionary

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        s = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)  # Check complex objects

        d = [{"foobarrooo": 989898}]
        s = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(s), d)  # Check single object

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)  # Check single object

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244, 'height': 34340}]
        s = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        self.assertEqual(Base.from_json_string(s), d)  # Check single object

        list_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)  # Compare input/output lists

        # ----------------- Tests for #16 ------------------------
    def test_I_save_to_file(self):
        '''Test the save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])  # Save rectangles to file

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)  # Check file length

        Rectangle.save_to_file(None)  # Save None
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")  # Check for empty array

        try:
            os.remove("Rectangle.json")  # Clean up
        except:
            pass
        Rectangle.save_to_file([])  # Save empty list
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")  # Check for empty array

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])  # Save single rectangle
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)  # Check file length

        Square.save_to_file(None)  # Save None for squares
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")  # Check for empty array

        try:
            os.remove("Square.json")  # Clean up
        except:
            pass
        Square.save_to_file([])  # Save empty list of squares
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")  # Check for empty array

        r2 = Square(1)
        Square.save_to_file([r2])  # Save single square
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)  # Check file length

        # ----------------- Tests for #18 ------------------------
    def test_J_create(self):
        '''Test the create() method.'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()  # Get dictionary representation
        r2 = Rectangle.create(**r1_dictionary)  # Create new rectangle from dictionary
        self.assertEqual(str(r1), str(r2))  # Compare string representations
        self.assertFalse(r1 is r2)  # Ensure different instances
        self.assertFalse(r1 == r2)  # Ensure not equal

        # ----------------- Tests for #19 ------------------------
    def test_K_load_from_file(self):
        '''Test the load_from_file() method.'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)  # Save rectangles
        list_out = Rectangle.load_from_file()  # Load rectangles
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))  # Different instances
        self.assertEqual(str(list_in[0]), str(list_out[0]))  # Compare string representations
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))  # Different instances
        self.assertEqual(str(list_in[1]), str(list_out[1]))  # Compare string representations

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)  # Save squares
        list_out = Square.load_from_file()  # Load squares
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))  # Different instances
        self.assertEqual(str(list_in[0]), str(list_out[0]))  # Compare string representations
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))  # Different instances
        self.assertEqual(str(list_in[1]), str(list_out[1]))  # Compare string representations

if __name__ == "__main__":
    unittest.main()  # Run all tests
