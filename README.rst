PyQt5 + Autobahn/Twisted Votes Demo
===================================

PyQt5 + Autobahn/Twisted version of the Crossbar Votes demo_ using Python 2.

Download with::

   $ git clone git@github.com:estan/votes.git

Install with::

   $ virtualenv2 --system-site-packages ~/demo_env
   $ source ~/demo_env/bin/activate
   $ cd votes
   $ pip install -e .

Run against the Crossbar demo router with::

   $ votes-qt --url wss://demo.crossbar.io/ws

Screenshot
----------

.. image:: https://raw.githubusercontent.com/estan/votes/master/screenshot.png
    :alt: Screenshot of the demo client
    :align: center

.. _demo: https://demo.crossbar.io/votes/index.html
