# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="Lagrange Interpolation", 
 version="1.0", 
 description="This program find a polynomial through a quantity n of points given by the user. Then the program shows a graphic with the polynomial as function.", 
 author="@brus2099", 
 author_email="brunocruzgranados@outlook.com", 
 url="https://github.com/brus2099/NumericMethods/tree/master/3ra_serie", 
 license="tipo de licencia", 
 scripts=["Lagrange.py, 
 console=["Lagrange.py, 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)