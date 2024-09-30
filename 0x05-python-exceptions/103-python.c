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
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to PyObject p.
 */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    // Get size and string representation
    size_t size = PyBytes_Size(p);
    const char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zu\n", size);
    printf("  trying string: %.*s\n", (int)size, str);
    
    // Print up to 10 bytes
    size = (size > 10) ? 10 : size;
    printf("  first %zu bytes: ", size);
    for (size_t i = 0; i < size; i++) {
        printf("%02hhx", (unsigned char)str[i]);
        if (i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: Pointer to PyObject p.
 */
void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);  // Get the double value
    printf("[.] float object info\n");
    printf("  value: %.6f\n", value);  // Print the float value
}

/**
 * print_python_list - Print information about a Python list object.
 * @p: Pointer to PyObject p.
 */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[*] Python list info\n");
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GET_ITEM(p, i);  // Get item safely
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type_name);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        }
    }
}
