#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Abdallah Deeb <abdallah@deeb.me>"
import os
from setuptools import setup, find_packages
import os, sys, glob, fnmatch
NAME = "Django-TimelineJS"
GITHUB_URL = "https://github.com/abdallah/%s" % (NAME)
DESCRIPTION = "Pluggable app for Django to edit and display TimelineJS timelines"
VERSION = '0.2'

def opj(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)

def find_data_files(srcdir, *wildcards, **kw):
    # get a list of all files under the srcdir matching wildcards,
    # returned in a format to be used for install_data
    def walk_helper(arg, dirname, files):
        if '.svn' in dirname:
            return
        names = []
        lst, wildcards = arg
        for wc in wildcards:
            wc_name = opj(dirname, wc)
            for f in files:
                filename = opj(dirname, f)

                if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                    names.append(filename)
        if names:
            lst.append( (dirname, names ) )

    file_list = []
    recursive = kw.get('recursive', True)
    if recursive:
        os.path.walk(srcdir, walk_helper, (file_list, wildcards))
    else:
        walk_helper((file_list, wildcards),
                    srcdir,
                    [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
    return file_list
files = find_data_files('timelinejs/', '*.*')
print 'files', files

setup(name=NAME,
    version=VERSION,
    download_url="%s/zipball/master" % GITHUB_URL,
    description=DESCRIPTION,
    packages = find_packages(),
    data_files = files,
    author='Abdallah Deeb',
    author_email='abdallah@deeb.me',
    url=GITHUB_URL,
    long_description=open('README.txt', 'r').read(),
    license='MPL2.0',
    #packages=[
    #    'timelinejs',
    #],
    
    #package_data={
    #    'timelinejs': [
    #        'templates/*',
    #        'static/*',
    #        'static/css/*',
    #        'static/css/themes/*',
    #        'static/css/themes/font/*',
    #        'static/admin/*',
    #        'static/admin/css/*',
    #        'static/admin/js/*',
    #        'static/js/*',
    #        'static/js/locale/*',
    #        'templatetags/*'
    #    ]
    #},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
