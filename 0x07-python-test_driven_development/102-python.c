#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_string - Displays information about Python string objects.
 * @p: Pointer to the PyObject structure.
 */
void print_python_string(PyObject *p)
{
    wprintf(L"[.] String object information\n");
    
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        wprintf(L"  [ERROR] Invalid String Object\n");
        return;
    }
    
    if (PyUnicode_IS_COMPACT_ASCII(p))
        wprintf(L"  type: compact ASCII\n");
    else
        wprintf(L"  type: compact Unicode\n");
    
    wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(p));
    wprintf(L"  value: %ls\n", PyUnicode_AS_UNICODE(p));
}
