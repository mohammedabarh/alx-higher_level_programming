#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to the PyObject
 */
void print_python_bytes(PyObject *p)
{
    size_t byte_count; /* Variable to hold the size of the bytes object */
    size_t index; /* Loop index */
    char *byte_string; /* Pointer to the bytes string */

    setbuf(stdout, NULL); /* Ensure unbuffered output */
    printf("[.] bytes object info\n");

    if (PyBytes_Check(p) == 0) /* Check if p is a valid bytes object */
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    byte_string = ((PyBytesObject *)(p))->ob_sval; /* Get the string value of bytes */
    byte_count = PyBytes_Size(p); /* Get the size of the bytes object */
    printf("  size: %ld\n  trying string: %s\n", byte_count, byte_string);

    byte_count = (byte_count >= 10) ? 10 : byte_count + 1; /* Limit the number of bytes to print */
    printf("  first %ld bytes: ", byte_count);

    for (index = 0; index < byte_count - 1; index++) /* Print each byte in hexadecimal format */
    {
        printf("%02hhx ", byte_string[index]);
    }
    printf("%02hhx\n", byte_string[index]); /* Print the last byte */
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to the PyObject
 */
void print_python_float(PyObject *p)
{
    char *float_string; /* Pointer to the float string representation */
    double float_value; /* Variable to hold the float value */

    setbuf(stdout, NULL); /* Ensure unbuffered output */
    printf("[.] float object info\n");

    if (PyFloat_Check(p) == 0) /* Check if p is a valid float object */
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    float_value = ((PyFloatObject *)(p))->ob_fval; /* Retrieve float value */
    float_string = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL); /* Convert float to string */
    printf("  value: %s\n", float_string); /* Print the float value */
}

/**
 * print_python_list - Print information about a Python list object
 * @p: Pointer to the PyObject
 */
void print_python_list(PyObject *p)
{
    size_t allocated_size; /* Variable to hold the allocated size of the list */
    size_t list_size; /* Variable to hold the size of the list */
    size_t index; /* Loop index */
    const char *type_name; /* Pointer to the type name of each element */
    PyListObject *list_obj; /* Pointer to the list object */

    setbuf(stdout, NULL); /* Ensure unbuffered output */
    printf("[*] Python list info\n");

    if (PyList_Check(p) == 0) /* Check if p is a valid list object */
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list_obj = (PyListObject *)p; /* Cast p to a PyListObject */
    list_size = PyList_GET_SIZE(p); /* Get the size of the list */
    allocated_size = list_obj->allocated; /* Get the allocated size of the list */
    printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", list_size, allocated_size);

    for (index = 0; index < list_size; index++) /* Iterate through each element in the list */
    {
        type_name = (list_obj->ob_item[index])->ob_type->tp_name; /* Get the type name of the element */
        printf("Element %li: %s\n", index, type_name); /* Print the index and type name */

        if (!strcmp(type_name, "bytes")) /* If the element is bytes, print its details */
        {
            print_python_bytes(list_obj->ob_item[index]);
        }
        else if (!strcmp(type_name, "float")) /* If the element is float, print its details */
        {
            print_python_float(list_obj->ob_item[index]);
        }
    }
}
