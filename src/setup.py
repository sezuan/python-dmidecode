from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib

libdir = get_python_lib(1)

setup(
  name = "python-dmidecode",
  version = "3.10.6",
  license='GPL-2',
  description = "Python extension module for dmidecode",
  author = "Nima Talebi & David Sommerseth",
  author_email = "nima@it.net.au, davids@redhat.com",
  url = "http://projects.autonomy.net.au/python-dmidecode/",
  data_files = [ ('share/python-dmidecode', ['src/pymap.xml']) ],
  ext_modules = [
    Extension(
      "dmidecodemod",
      sources      = [
        "src/dmidecodemodule.c",
        "src/util.c",
        "src/dmioem.c",
        "src/dmidecode.c",
        "src/dmixml.c",
        "src/dmierror.c",
        "src/xmlpythonizer.c"
      ],
      include_dirs = [ "/usr/include/libxml2" ],
      library_dirs = [ libdir ],
      libraries    = [ "xml2", "xml2mod" ]
    )
  ],
  py_modules = [ "dmidecode" ]
)
