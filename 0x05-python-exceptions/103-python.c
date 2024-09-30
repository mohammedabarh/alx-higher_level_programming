#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
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
    Py_ssize_t size, i;
    char *str;

    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    
    str = PyBytes_AsString(p);
    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str ? str : "None");

    // Print first 10 bytes
    size = (size > 10) ? 10 : size;
    printf("  first %zd bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx%s", (unsigned char)str[i], (i < size - 1) ? " " : "\n");
    }
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to the PyObject
 */
void print_python_float(PyObject *p)
{
    char *str;
    double f;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    
    f = PyFloat_AsDouble(p);
    str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str);
    PyMem_Free(str);  // Free memory allocated by PyOS_double_to_string
}

/**
 * print_python_list - Print information about a Python list object
 * @p: Pointer to the PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
    
    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type_name);
        if (strcmp(type_name, "bytes") == 0)
            print_python_bytes(item);
        else if (strcmp(type_name, "float") == 0)
            print_python_float(item);
    }
}
