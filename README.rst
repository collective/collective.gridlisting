.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.gridlisting/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.gridlisting/actions/workflows/plone-package.yml


======================
collective.gridlisting
======================

Adds a Behavior to manipulate various listing appearance settings
using Bootstrap 5 (column layout) and patternslib (masonry).

This behavior is automatically enabled for "Folder" and "Collection" when you install it.


Features
--------

- Adds new view template "Grid listing" for "Folder" and "Collection"
- You get a new "Grid listing" tab when editing a Folder or a Collection where
  you can set various options for the listing template.


Translations
------------

This product has been translated into

- English
- German


Installation
------------

Install collective.gridlisting by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.gridlisting


and then running ``bin/buildout``



Contribute
----------

- Issue Tracker: https://github.com/collective/collective.gridlisting/issues
- Source Code: https://github.com/collective/collective.gridlisting
- Documentation: https://github.com/collective/collective.gridlisting/docs



License
-------

The project is licensed under the GPLv2.
