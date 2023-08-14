from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [

]

test_requirements = [

]

setup(
    name='hellosound',
    version='0.1a',
    description='Test a sound in pulseaudio',
    long_description=readme,
    author='Luis Louro',
    author_email='lapisdecor@gmail.com',
    url='https://github.com/lapisdecor/hellosound',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    include_package_data=True,
    licence='GNU GPL v3',
    zip_safe=False,
    keywords='hellosound',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    scripts=['bin/hello']
)
