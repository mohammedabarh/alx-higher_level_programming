#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>

/**
 * print_python_string - Prints Python strings
 * @p: PyObject string object
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    wchar_t *value;
    const char *type;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsWideCharString(p, &length);

    if (PyUnicode_IS_COMPACT_ASCII(p))
        type = "compact ascii";
    else
        type = "compact unicode object";

    printf("  type: %s\n", type);
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", value);

    PyMem_Free(value);
}
