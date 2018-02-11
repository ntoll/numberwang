Numberwang.py
=============

A utility to recreate the classic gameshow, Numberwang!

What's Numberwang..? See `this YouTube video from the first episode <https://www.youtube.com/watch?v=ZH-cXBhkl-E>`_.

Installation
------------

To install simply type::

    $ pip install numberwang

Usage
-----

Simply pass a sentence to the ``numberwang`` command. The sentence must contain
a number::

    $ numberwang The square root of -1
    That's Numberwang!

If you don't a response, it's because the sentence isn't Numberwang. In that
case, please try again.

Development
-----------

The source code is hosted in GitHub. Please feel free to fork the repository.
Assuming you have Git installed you can download the code from the canonical
repository with the following command::

    $ git clone https://github.com/ntoll/numberwang.git

Ensure you have the correct dependencies for development installed by creating
a virtualenv and running::

    $ pip install -r requirements.txt

There is a Makefile that helps with most of the common workflows associated
with development. Typing ``make`` on its own will list the options.

