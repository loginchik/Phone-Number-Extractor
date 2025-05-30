from setuptools import setup, find_packages


setup(
    name='phone-number-extractor',
    version='1.0.0',
    author='Anna Loginova',
    packages=find_packages(exclude=['tests', '__pycache__']),
    license='MIT',
    description='A Python library for extracting and formatting phone numbers',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/loginchik/Phone-Number-Extractor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_required='>=3.11'
)
