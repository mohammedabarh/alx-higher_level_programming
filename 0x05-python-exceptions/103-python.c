#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <floatobject.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            print_python_float(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    char *string = ((PyBytesObject *)p)->ob_sval;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx", string[i]);
        if (i < 9 && i < size - 1) printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    double value = ((PyFloatObject *)p)->ob_fval;

    printf("[.] float object info\n");
    printf("  value: %.*g\n", 17, value);
}
