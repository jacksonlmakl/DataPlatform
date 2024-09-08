from setuptools import setup, find_packages

setup(
    name='DataPlatform',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python client to interact with the DataPlatform API.',
    url='https://github.com/yourusername/yourrepo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
