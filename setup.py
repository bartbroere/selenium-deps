from setuptools import setup

with open('README.md', 'r') as readme:
    readme = "".join(readme.readlines())

with open('requirements.in', 'r') as requirements:
    dependencies = [dependency.split('#')[0].replace('\n', '').replace(' ', '')
                    for dependency in requirements.readlines() if
                    dependency[0] != '#']

setup(
    name='selenium_deps',
    version='2019.3.30',
    url='https://github.com/bartbroere/selenium-deps/',
    author='Bart Broere',
    author_email='mail@bartbroere.eu',
    license='MIT License',
    description="Download all dependencies for a working Selenium-browser",
    keywords='firefox selenium geckodriver',
    long_description=readme,
    py_modules=['seleniumdeps'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': ['seleniumdeps=seleniumdeps:main'],
    },
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    )
)
