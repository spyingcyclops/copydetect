Copydetect
##########

Contents

.. toctree::
   :maxdepth: 2

   self
   cmdline
   api

Overview
========
Copydetect is a command line tool that detects code duplication and generates an HTML report of similarities between files. The report highlights similar code slices, with a similarity score for each pair of files. Copydetect is highly configurable, allowing you to set thresholds for similarity detection, exclude boilerplate code, and filter by file extension.

Copydetect was designed to help identify potential cases of plagiarism. It can also be used to identify refactoring opportunities in a codebase or documentation set. 


Approach
========
Copydetect is based on the approach proposed in `Winnowing: Local Algorithms for Document Fingerprinting <http://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf>`_ and used for the popular `MOSS <https://theory.stanford.edu/~aiken/moss/>`_ platform. Copydetect takes a list of directories containing code as input, and generates an HTML report displaying copied slices as output. The implementation takes advantage of fast numpy functions for efficient generation of results. Code tokenization is handled by `Pygments <https://pygments.org>`_, so all 500+ languages that pygments can detect and tokenize are in turn supported by Copydetect.



Installation
============
Python version 3.7 or greater is required.

To install copydetect, run

``pip install copydetect``

To use copydetect, run the ``copydetect`` command. (On Windows, run ``copydetect.exe``. If your scripts folder is not in your PATH, you can also run copydetect with ``py.exe -m copydetect``).

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
