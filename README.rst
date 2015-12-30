.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
PlayThing
==============================================================================
.. image:: https://github.com/PlaythingBlog/branding/blob/master/playthinglogo.png?raw=true

PlayThing is a microblogging platform.
We call our blogs "collections" and you can create multiple "collections" on a single
``PlayThing`` site.

Getting Started
-----------------
The fastest way to get started is to use the Plaything Cloud9 installer.

Step 1 - checkout to c9
`````````````````````````
Go to http://c9.io and create a new workspace cloning from ``https://github.com/PlaythingBlog/plaything.core.git``

.. image:: https://github.com/PlaythingBlog/plaything.core/blob/master/docs/images/creating-a-plaything-dev-box.png?raw=true

Step 2 - run the installer
`````````````````````````````
::
    sh c9install.sh

Step 3 - launch the site
````````````````````````````
::

   bin/instance fg

You can view the running site by going to "Preview" > "Preview Running Application"

Features
---------
Discussion System
``````````````````
Builtin discussion system which includes basic captcha support to prevent spam.

Multiple microblogs
````````````````````
PlayThing is a microblogging platform which allows you to run multiple microblogs
at a time. 
Each microblog is called a ``collection``.

Multiuser
````````````
Out of the box PlayThing allows multiple users

Different types of posts
``````````````````````````
A blog post can be any of the following types:
Images, News Items, Links, Files or Events.

Easily create your own post type
```````````````````````````````````
You can create your own custom content types and add them to your blog.

Super secure
`````````````
PlayThing is built on a NoSQL platform which makes it immune to all too common
SQL Injection Attacks.

Restful API 
````````````````
Your developer friends will be happy too because we provide a restful API out of the box.



Documentation
-------------
Full documentation for end users will be hosted at
http://plaything.readthedocs.org/ (really soon)



Installation
------------

Install plaything.core by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plaything.core


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/plaything.core/issues
- Source Code: https://github.com/collective/plaything.core
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
