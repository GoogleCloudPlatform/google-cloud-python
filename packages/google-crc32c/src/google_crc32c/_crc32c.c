#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <crc32c/crc32c.h>

/* The minimum buffer size in bytes (1MB) required to justify the overhead of releasing the GIL. */
static const Py_ssize_t gil_threshold = 1024 * 1024;


static PyObject *
_crc32c_extend(PyObject *self, PyObject *args)
{
    unsigned long crc_input;
    uint32_t crc;
    PyThreadState *save = NULL;
    Py_buffer buffer;

    if (!PyArg_ParseTuple(args, "ky*", &crc_input, &buffer))
        return NULL;

    if (buffer.len >= gil_threshold) {
        save = PyEval_SaveThread();
    }

    crc = crc32c_extend((uint32_t)crc_input, (const uint8_t*)buffer.buf, buffer.len);

    if (save) {
        PyEval_RestoreThread(save);
    }

    PyBuffer_Release(&buffer);

    return PyLong_FromUnsignedLong(crc);
}


static PyObject *
_crc32c_value(PyObject *self, PyObject *args)
{
    uint32_t crc;
    Py_buffer buffer;
    PyThreadState *save = NULL;

    if (!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;

    if (buffer.len >= gil_threshold) {
        save = PyEval_SaveThread();
    }

    crc = crc32c_value((const uint8_t*)buffer.buf, buffer.len);

    if (save) {
        PyEval_RestoreThread(save);
    }

    PyBuffer_Release(&buffer);

    return PyLong_FromUnsignedLong(crc);
}


static PyMethodDef Crc32cMethods[] = {
    {"extend",  _crc32c_extend, METH_VARARGS,
     "Return an updated CRC32C checksum."},
    {"value",  _crc32c_value, METH_VARARGS,
     "Return an initial CRC32C checksum."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

#if PY_VERSION_HEX >= 0x030f0000
PyABIInfo_VAR(abi_info);
static PySlot Crc32cSlots[] = {
    PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
    PySlot_STATIC_DATA(Py_mod_name, "_crc32c"),
    PySlot_STATIC_DATA(Py_mod_methods, Crc32cMethods),
    PySlot_SIZE(Py_mod_state_size, 0),
    PySlot_UINT64(Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED),
    PySlot_UINT64(Py_mod_gil, Py_MOD_GIL_NOT_USED),
    PySlot_END
};

PyMODEXPORT_FUNC
PyModExport__crc32c()
{
    return Crc32cSlots;
}

PyMODINIT_FUNC
PyInit__crc32c(void)
{
    /* workaround for setuptools on Python 3.15+ */
    /* https://github.com/pypa/distutils/issues/387 */
    return NULL;
}

#else

static PyModuleDef_Slot Crc32cSlots[] = {
#ifdef Py_mod_multiple_interpreters
    {Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED},
#endif
#ifdef Py_mod_gil
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
#endif
    {0, NULL}
};

static struct PyModuleDef crc32cmodule = {
    PyModuleDef_HEAD_INIT, /* m_base */
    "_crc32c",             /* m_name: name of module */
    NULL,                  /* m_doc: module documentation, may be NULL */
    0,                     /* m_size: size of per-interpreter state of the module */
    Crc32cMethods,         /* m_methods */
    Crc32cSlots,           /* m_slots */
    NULL,                  /* m_traverse */
    NULL,                  /* m_clear */
    NULL,                  /* m_free */
};

PyMODINIT_FUNC
PyInit__crc32c(void)
{
    return PyModuleDef_Init(&crc32cmodule);
}
#endif
