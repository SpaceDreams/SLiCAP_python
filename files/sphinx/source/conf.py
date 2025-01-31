# -*- coding: utf-8 -*-
import time
import sphinx_rtd_theme
from projectinfo import project, copyright, author, version, release

# -- Sphinx extensions --------------------------------------------------------
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.excel',
    'sphinxcontrib.excel_table',
    'sphinxcontrib.inkscapeconverter',
]

# -- Sphinx settings ----------------------------------------------------------
source_suffix    = '.rst'
master_doc       = 'index'
language         = None
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']
templates_path   = ['_templates']
pygments_style   = None
numfig           = True

# -- HTML settings ------------------------------------------------------------
def setup(app):
    app.add_stylesheet('custom.css')
html_theme         = 'sphinx_rtd_theme'
html_logo          = '_static/html_logo.png'
html_static_path   = ['_static']
htmlhelp_basename  = project
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- LaTeX settings -----------------------------------------------------------
latex_toplevel_sectioning = 'chapter'
latex_elements = {
    'papersize': 'A4paper',
    'pointsize': '12pt',
    'preamble': r'''
     \usepackage{float}
     \usepackage{svg}
    ''',
    'figure_align': 'htb',
}
