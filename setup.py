from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open('README.md') as README_file:
    description = README_file.read()

setup(
    name='CraftiGames.py',
    version='2.1.1',
    author='sti1ltyping',
    author_email='sti1ltyping.chillax@gmail.com',
    url='https://github.com/sti1ltyping/CraftiGames.py',
    packages=find_packages(),
    license='MIT',
    description='A Python based API wrapper for CraftiGames community',
    long_description=description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)