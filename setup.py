import setuptools

with open('./README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('./requirements.txt') as requirements_file:
    requirements = [line.strip() for line in requirements_file.readlines()]

setuptools.setup(
    name='cl-testlog',
    version='0.0.1',
    author='The Project Contributors',
    description='CompatibL Platform Integration for Test Log',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url='https://github.com/compatibl/cl-testlog',
    project_urls={
        'Source Code': 'https://github.com/compatibl/cl-testlog',
    },
    packages=setuptools.find_namespace_packages(where='.', include=['cl.testlog*'], exclude=['tests', 'tests.*']),
    package_dir={'': '.'},
    classifiers=[
        # Alpha - will attempt to avoid breaking changes but they remain possible
        'Development Status :: 3 - Alpha',

        # Audience and topic
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',

        # License
        "License :: OSI Approved :: Apache Software License",

        # Runs on Python 3.9 and later releases
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

        # Operating system
        'Operating System :: OS Independent',
    ],
)
