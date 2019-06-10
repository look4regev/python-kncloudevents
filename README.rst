=============
kncloudevents
=============


.. image:: https://img.shields.io/pypi/v/kncloudevents.svg
        :target: https://pypi.python.org/pypi/kncloudevents

.. image:: https://img.shields.io/travis/elegantmonkeys/python-kncloudevents.svg
        :target: https://travis-ci.org/elegantmonkeys/python-kncloudevents

.. image:: https://readthedocs.org/projects/kncloudevents/badge/?version=latest
        :target: https://kncloudevents.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



kncloudevents is a HTTP server for listening to Knative Eventing messages


* Documentation: https://kncloudevents.readthedocs.io.
* Source code: https://github.com/elegantmonkeys/python-kncloudevents
* Bug reports: https://github.com/elegantmonkeys/python-kncloudevents/issues


Description
-----------

A lightweight package for doing the heavy lifting of setting up a `cloudevents <https://cloudevents.io/>`_ server for you!
Just provide your function and it will be called on every new event with the event data.


Notes
-----

* Uses the `official cloudevents sdk for Python <https://github.com/cloudevents/sdk-python>`_ for parsing the incoming data
* Inspired by the `Knative Golang project <https://github.com/knative/eventing-contrib/tree/master/pkg/kncloudevents>`_


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
