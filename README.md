
# Table of Contents

1.  [Installing from pypi](#org968aafe)
2.  [Installing from git](#org30a6023)
3.  [Execute test](#org1d2e448)
4.  [Making and uploading a pypi package](#orgdd75ed0)

Learning about Scraping with python by David Arroyo Menéndez

You can check external documentation in

-   <https://requests.readthedocs.io/en/latest/>
-   <https://mechanicalsoup.readthedocs.io/en/stable/>
-   <https://newspaper.readthedocs.io/en/latest/>


<a id="org968aafe"></a>

# Installing from pypi

First, to create a python virtual environment

    $ mkdir ~/venv-damescraping
    $ python3.14 -m venv ~/venv-damescraping
    $ cd venv-damescraping
    $ source bin/activate

Second, to download the python package

    $ python3.14 -m pip install damescraping

Last, to go the directory and to check files and directories

    $ cd lib/python3.14/site-packages/damescraping
    $ ls


<a id="org30a6023"></a>

# Installing from git

    $ git clone https://github.com/davidam/damescraping
    $ pip3 install markdown mechanicalsoup newspaper3k lxml requests
    $ cd damescraping


<a id="org1d2e448"></a>

# Execute test

    $ cd damescraping
    $ ./runtest.sh


<a id="orgdd75ed0"></a>

# Making and uploading a pypi package

To install create tar.gz in dist directory:

    $ cd damescraping
    $ python3 -m build
    $ twine upload dist/damescraping-0.1.tar.gz

