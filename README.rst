=========
POLYGONAL
=========


-------------
What is this?
-------------

Polygonal is a proof-of-concept python implementation of a ports&adapters 
architecture.

It is inteded to present the possibilites of testing and architecturing of
fairly complex systems, while keeping their structure homogenic.


-------------------------
What are the limitations?
-------------------------

Currently the framework is built to support synchronous Python code.
This will be extended with suport fo asynchronicity and eventually will
support multiple languages and lead to a microservices based topography.


--------------------
How do I contribute?
--------------------

Please fork and 'pull request' any suggested changes. Only fully tested
code will be considered. The code must also comply with standards for language
used. In case of Python - pep8 and pyling (according to the rc files found
in the root of the repository)


--------------
Why do I care?
--------------

You will learn how to work with a ports&adapters paradigm (aka Hexagonal
architecture). You will learn how to test things in a world where mocks
replace any external dependencies in a clean way (no messing arround with
monkey-patching - dependency injection all the way).

-----------------------
How do I run the tests?
-----------------------
```
pip install -r requirements.txt
nosetests
```

----------------------
What is the structure?
----------------------

`polygonal` holds the library itself
`transport` holds a small web project intended to drive the development of
the library
