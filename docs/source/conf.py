# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ProjectTwo'
copyright = '2025, Author'
author = 'Author'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# -- Bing Webmaster Tools Verification Meta Tag ------------------------------

def add_bing_meta(app, pagename, templatename, context, doctree):
    context['metatags'] = context.get('metatags', '') + \
        '<meta name="msvalidate.01" content="00150BC63D685D5320E81633846C5088" />\n'

def setup(app):
    app.add_config_value('meta_tags', '', 'html')
    app.connect('html-page-context', add_bing_meta)