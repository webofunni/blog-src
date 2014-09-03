#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Unni'
SITENAME = u'Mutexes Blog'
SITETITLE = u'Notes of a sys admin'
SITEURL = ''

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'naiq'

MENUITEMS = (('feed', '/blog/feeds/all.atom.xml'),
             ('code', '/blog/pages/code.html'),
             ('about', '/blog/pages/about-me.html'),)


DEBUG = True

MD_EXTENSIONS = ['codehilite(css_class=codehilite)','extra']

STATIC_PATHS = ['talks']

PAGE_EXCLUDES = ['talks']
ARTICLE_EXCLUDES = ['pages', 'talks']
            
