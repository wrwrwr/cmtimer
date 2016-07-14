=======
cmtimer
=======

Measures the execution time of a block of code. Uses perf_counter_ for the
measurement. Behaves like a float (seconds) when printed or used within an
arithmetic context.

.. _perf_counter: https://docs.python.org/3/library/time.html#time.perf_counter

Example
=======

.. code:: python

    from cmtimer import Timer

    with Timer() as time:
        # Three hours too soon or a minute too late?

    print(f"Time taken: {time:.2f} s")

Installation
============

.. code:: bash

    pip3 install cmtimer
