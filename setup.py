#!/usr/bin/env python3
"""
Setup script for GitHub Organization Statistics Tool
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
        return f.read()

# Read requirements from requirements.txt
def read_requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='github-org-stats',
    version='1.0.0',
    author='Open Source Contributors',
    author_email='contributors@github-org-stats.org',
    description='A comprehensive tool for analyzing GitHub organization statistics',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/zoharbabin/github-org-stats',
    project_urls={
        'Bug Reports': 'https://github.com/zoharbabin/github-org-stats/issues',
        'Source': 'https://github.com/zoharbabin/github-org-stats',
        'Documentation': 'https://github.com/zoharbabin/github-org-stats/blob/main/docs/USAGE.md',
    },
    py_modules=['github_org_stats'],
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.10.0',
            'black>=21.0.0',
            'flake8>=3.8.0',
            'mypy>=0.800',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    keywords='github organization statistics analysis repositories contributors',
    entry_points={
        'console_scripts': [
            'github-org-stats=github_org_stats:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['README.md', 'LICENSE', 'requirements.txt'],
    },
    zip_safe=False,
)