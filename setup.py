import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spiref",
    version="1.0.4",
    author="Kenneth Verstraete",
    author_email="verstraetekenneth@gmail.com",
    description="This package contains the reference value calculator for spirometry.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kennethv93/spiref",
    packages=setuptools.find_packages(),
    package_data={'spiref': ['GLI-2012.xlsx']},
    install_requires=['openpyxl', 'numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)