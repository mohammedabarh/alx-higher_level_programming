#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Outputs details about a Python bytes object
 * @p: Pointer to the PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t length, index;
    const char *byte_str;

    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    byte_str = PyBytes_AsString(p);
    length = PyBytes_Size(p);
    printf("  size: %zd\n  trying string: %s\n", length, byte_str);

    length = (length > 10) ? 10 : length + 1; // Adjust for printing
    printf("  first %zd bytes: ", length);
    for (index = 0; index < length - 1; index++)
        printf("%02hhx ", (unsigned char)byte_str[index]);
    printf("%02hhx\n", (unsigned char)byte_str[index]);
}

/**
 * print_python_float - Outputs details about a Python float object
 * @p: Pointer to the PyObject
 */
void print_python_float(PyObject *p)
{
    char *float_str;
    double value;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    float_str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", float_str);
    PyMem_Free(float_str); // Free the allocated string
}

/**
 * print_python_list - Outputs details about a Python list object
 * @p: Pointer to the PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t list_size, i;
    PyListObject *list_obj;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list_obj = (PyListObject *)p;
    list_size = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", list_size, list_obj->allocated);

    for (i = 0; i < list_size; i++)
    {
        PyObject *item = list_obj->ob_item[i];
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type_name);
        if (strcmp(type_name, "bytes") == 0)
            print_python_bytes(item);
        else if (strcmp(type_name, "float") == 0)
            print_python_float(item);
    }
}
