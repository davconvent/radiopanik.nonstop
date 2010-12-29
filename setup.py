from setuptools import setup, find_packages
import os

name = 'radiopanik.nonstop'
version = '0.1'

entry_points = """
[console_scripts]
    nonstop = %(name)s.console.command:run
    test = %(name)s.console.my_test:run
    dbtest = %(name)s.database.basic:run
[global_nonstop_command]
    help = radiopanik.nonstop.console.help:NonStopHelpCommand
    fetch = radiopanik.nonstop.console.fetch:FetchCommand
    add = radiopanik.nonstop.console.add:AddCommand
    dbtest = radiopanik.nonstop.database.sh:NonStopDatabaseCommand          
    web = radiopanik.nonstop.web.generator:WebPagesCommand
    db = radiopanik.nonstop.metadata.basicdb:BasicDBCommand
[radiopanik.config]
    etc = %(name)s:etc
    web_cfg = %(name)s:web_cfg
    web_www = %(name)s:web_www
"""


setup(name=name,
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['radiopanik'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout',
          'PasteScript',
          'sqlalchemy',
          'zope.pagetemplate',
          'mutagen',
          # -*- Extra requirements: -*-
      ],
      entry_points=entry_points % dict(name=name),
      )
