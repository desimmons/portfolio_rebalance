.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/portfolio_rebalance.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/portfolio_rebalance
    .. image:: https://readthedocs.org/projects/portfolio_rebalance/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://portfolio_rebalance.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/portfolio_rebalance/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/portfolio_rebalance
    .. image:: https://img.shields.io/pypi/v/portfolio_rebalance.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/portfolio_rebalance/
    .. image:: https://img.shields.io/conda/vn/conda-forge/portfolio_rebalance.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/portfolio_rebalance
    .. image:: https://pepy.tech/badge/portfolio_rebalance/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/portfolio_rebalance
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/portfolio_rebalance

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

===================
portfolio_rebalance
===================


    Understand how to rebalance your UK Vanguard portfolio using switch procedures.


This file performs portfolio rebalancing calculations, presenting the results
confluent with Vanguard Switch procedures. It _does not_ interact directly with 
your Vanguard account. For example, if you hold
assets "A", "B", and "C" on Vanguard, each with total values in your
portfolio of 2000, 3000, and 4000, respectively. By running::

    rebalance A 2000 B 3000 C 4000

You will be presented with::

    {'A': 1.0, 'B': 0.0, 'C': -0.25},

indicating that you should sell 25% of "C", placing 100% of the sale
into "A" and 0% into "B".


Install and run
===============

1. Ensure you have `pip` installed
2. `pip install .`
3. Run the following::

        rebalance <Asset A> <Total value of asset A in your portfolio> ... <Asset Z> <Total value of asset Z in your portfolio>

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.1.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
