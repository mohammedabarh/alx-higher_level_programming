#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - print python things
 * @obj: pointer to PyObject
 */
void print_python_bytes(PyObject *obj)
{
    size_t byte_count, index;
    char *byte_string;

    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");
    if (PyBytes_Check(obj) == 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    byte_string = ((PyBytesObject *)(obj))->ob_sval;
    byte_count = PyBytes_Size(obj);
    printf("  size: %ld\n  trying string: %s\n", byte_count, byte_string);
    byte_count >= 10 ? byte_count = 10 : byte_count++;
    printf("  first %ld bytes: ", byte_count);
    for (index = 0; index < byte_count - 1; index++)
        printf("%02hhx ", byte_string[index]);
    printf("%02hhx\n", byte_string[index]);
}

/**
 * print_python_float - print python things
 * @obj: pointer to PyObject
 */
void print_python_float(PyObject *obj)
{
    char *float_string;
    double float_value;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");
    if (PyFloat_Check(obj) == 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    float_value = ((PyFloatObject *)(obj))->ob_fval;
    float_string = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", float_string);
}

/**
 * print_python_list - print python things
 * @obj: pointer to PyObject
 */
void print_python_list(PyObject *obj)
{
    size_t allocated_size, list_size, index;
    const char *type_name;
    PyListObject *list_obj;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");
    if (PyList_Check(obj) == 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
    list_obj = (PyListObject *)obj;
    list_size = PyList_GET_SIZE(obj);
    allocated_size = list_obj->allocated;
    printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", list_size, allocated_size);
    for (index = 0; index < list_size; index++)
    {
        type_name = (list_obj->ob_item[index])->ob_type->tp_name;
        printf("Element %li: %s\n", index, type_name);
        !strcmp(type_name, "bytes") ? print_python_bytes(list_obj->ob_item[index]) : (void)type_name;
        !strcmp(type_name, "float") ? print_python_float(list_obj->ob_item[index]) : (void)type_name;
    }
}
