# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- pyGenericPath setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
#sys.path.insert(0, os.path.abspath('../Semaphore'))
#sys.path.insert(0, os.path.abspath('_extensions'))
#sys.path.insert(0, os.path.abspath('_themes/sphinx_rtd_theme'))


# -- Project information -----------------------------------------------------

project = 'Semaphore Microservice'
copyright = '2019-2020, Patrick Lehmann'
author = 'Patrick Lehmann'

# The full version, including alpha/beta/rc tags
release = 'v0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
# Sphinx theme
	"sphinx_rtd_theme",
# Standard Sphinx extensions
	"sphinx.ext.autodoc",
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.inheritance_diagram',
	'sphinx.ext.todo',
	'sphinx.ext.graphviz',
	'sphinx.ext.mathjax',
	'sphinx.ext.ifconfig',
	'sphinx.ext.viewcode',
# SphinxContrib extensions

# Other extensions
#	'DocumentMember',
# local extensions (patched)

# local extensions
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"_build",
	"Thumbs.db",
	".DS_Store"
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
intersphinx_mapping = {
	'python':          ('https://docs.python.org/3', None),
	#	'pyFlags':          ('http://pyFlags.readthedocs.io/en/latest', None),
	'pyExceptions':    ('http://pyExceptions.readthedocs.io/en/latest', None),
	'pyAttributes':    ('http://pyAttributes.readthedocs.io/en/latest', None),
	'pyGenericPath':   ('http://pyGenericPath.readthedocs.io/en/latest', None),
	'pyHTTPInterface': ('http://pyHTTPInterface.readthedocs.io/en/latest', None),
	'pyHTTPReqRouter': ('http://pyHTTPRequestRouter.readthedocs.io/en/latest', None),
	'pyHTTPServer':    ('http://pyHTTPServer.readthedocs.io/en/latest', None),
	'SphinxEx':        ('http://SphinxExtensions.readthedocs.io/en/latest', None),
}


# ==============================================================================
# Sphinx.Ext.AutoDoc
# ==============================================================================
# see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autodoc_member_order = "bysource"       # alphabetical, groupwise, bysource


# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	'issue': ('https://github.com/Paebbels/Semaphore-Microservice/issues/%s', 'issue #'),
	'pull':  ('https://github.com/Paebbels/Semaphore-Microservice/pull/%s', 'pull request #'),
	'src':   ('https://github.com/Paebbels/Semaphore-Microservice/blob/master/Semaphore/%s?ts=2', None),
#	'test':  ('https://github.com/Paebbels/Semaphore-Microservice/blob/master/test/%s?ts=2', None)
}


# ==============================================================================
# Sphinx.Ext.Graphviz
# ==============================================================================
graphviz_output_format = "svg"
