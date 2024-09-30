#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[.] Python list info\n");
        printf("[ERROR] Invalid List Object\n");
        return;
    }
    
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[.] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type_name);
        
        // Print sub-info if the item is a bytes object
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
        // Print sub-info if the item is a float object
        else if (PyFloat_Check(item)) {
            print_python_float(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }
    
    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    
    const char *bytes_str = PyBytes_AsString(p);
    printf("  trying string: %.*s\n", (int)size < 10 ? (int)size : 10, bytes_str);
    printf("  first %d bytes: ", size < 10 ? (int)size : 10);
    
    for (int i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x", (unsigned char)bytes_str[i]);
        if (i < (size < 10 ? size : 10) - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("[ERROR] Invalid Float Object\n");
        return;
    }
    
    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %.6f\n", value);
}
