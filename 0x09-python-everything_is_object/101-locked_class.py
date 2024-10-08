#!/usr/bin/python3
# Import the LockedClass from the specified module
LockedClass = __import__('101-locked_class').LockedClass

# Create an instance of LockedClass
instance = LockedClass()
# Set the first_name attribute
instance.first_name = "John"

# Attempt to set a last_name attribute, which should raise an exception
try:
    instance.last_name = "Snow"
except Exception as error:
    print("[{}] {}".format(error.__class__.__name__, error))
