# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Пользовательская документация ПК "СтройКонтроль"'
copyright = '2022, ООО "Мобильные решения для строительства"'
author = 'ООО "Мобильные решения для строительства"'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.youtube', 
    'sphinx_comments',
    'sphinxcontrib.images',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'
locale_dirs = ['./locale']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_copy_source = False

html_logo = '_static/logo.png'

html_favicon = '_static/favicon.ico'

html_theme_options = {
    "icon_links": [
        {
            "name": "AppStore",
            "url": "https://apps.apple.com/ru/app/стройконтроль/id867522092",
            "icon": "fab fa-app-store"
        },
         
       {
            "name": "PlayMarket",
            "url": "https://play.google.com/store/apps/details?id=com.planstery.review&hl=ru",
            "icon": "fab fa-google-play"
        },
        
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/mrs_software/",
            "icon": "fab fa-instagram",
        },

        {
            "name": "VK",
            "url": "https://vk.com/m_r_s",
            "icon": "fab fa-vk",
        }
    ],

     "search_bar_text": "Поиск по документации...",

}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
 ('index', 'yourdoc.tex', u'DocName', u'YourName', 'manual'),
]