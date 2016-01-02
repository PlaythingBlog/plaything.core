==============================================================================
PlayThing
==============================================================================

.. image:: https://github.com/PlaythingBlog/branding/blob/master/playthinglogo.png?raw=true

PlayThing is a microblogging platform.

At the moment, Plaything is being developed as a standalone product, not really an add-on. It can do bad things to existing sites. In short don't install this on a production site if you care about the data.

Install on Heroku
------------------

Click the Heroku button below to try out Plaything. Be up and running in 5 minutes.
We recommend that you set the ``App Name`` and the ``SITE_NAME`` to same thing.
NOT FOR PRODUCTION, JUST FOR TESTING.

..  image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy?template=https://github.com/PlaythingBlog/plaything.core


Install on Cloud9
---------------------

One way to get started on development is to use the Plaything Cloud9 installer.

Step 1 - checkout to c9
`````````````````````````
Go to http://c9.io and create a new workspace cloning from ``https://github.com/PlaythingBlog/plaything.core.git``

.. image:: https://github.com/PlaythingBlog/plaything.core/blob/master/docs/images/creating-a-plaything-dev-box.png?raw=true

Step 2 - run the installer
`````````````````````````````
::

    sh c9install.sh

This will install dependencies and setup a PlayThing site.

Step 3 - launch the site
````````````````````````````
::

   bin/instance fg

You can view the running site by going to "Preview" > "Preview Running Application"

Views
---------
You can visit [yourplaythingsite]/posts to view all your posts
or view posts by year or month e.g.
[yourplaythingsite]/posts/2015 or [yourplaythingsite]/posts/2015/12


Features
---------
Discussion System
``````````````````
Builtin discussion system which includes basic captcha support to prevent spam.

Tag support
``````````````
Tag your posts and view them organized by tag.

Collections and folders for the meticulous
````````````````````````````````````````````
A ``collection`` is a special way of automatically organizing posts based on 
date, type, creator or whatever. You can even treat each collection as 
if it were a separate microblog. For the more discriminating you may prefer 
"physically" grouping your posts into their own locations.

Multiuser
````````````
Out of the box PlayThing allows multiple blog users

Different types of posts
``````````````````````````
A blog post can be any of the following types:
Photos, News Items, Links, Files or Events.

Embed Videos
`````````````
Embed videos or other media

Easily create your own post type
```````````````````````````````````
Some times the existing post types just don't cut it.
You may need a "customer testimonial" or "case study", just create your own
custom post type add you'll have it for your PlayThing site.

But wait there's more... We have Pages
````````````````````````````````````````
Add a page and make it your home page, so PlayThing can be your website

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
