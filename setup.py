from setuptools import setup

setup(
    name='discogs-import',
    version='0.1',
    description='A fork of discogs import/export scripts',
    author='*',
    author_email='*',
    url='http://github.com/bmcfee/discogs-import',
    download_url='http://github.com/bmcfee/discogs-import/releases',
    long_description="""\
    A fork of discogs import/export scripts
    """,
    scripts=['parse_discogs.py'],
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Multimedia :: Text Processing :: Markup",
    ],
    keywords='web template',
    license='GPL',
    install_requires=[
        'json',
    ],
    extras_require = {
        'ujson': 'ujson',
        'couchdb': 'couchdb',
        'mongodb': 'pymongo',
        'postgres': 'psycopg2'
    }
)
