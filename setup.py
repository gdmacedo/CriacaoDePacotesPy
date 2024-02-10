from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-test",
    version="0.0.1",
    author="Glener Diniz Macedo",
    author_email="gdmacedo@hotmail.com",
    description="Trial version - Image processing. This project belongs to Glener Diniz Macedo, Full Stack developer, production engineer and data science specialist. This package is a demo for upload simulation on the Test Pypi website, and is from the Bootcamp full stack Python developer class. E-mail: gdmacedo@hotmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdmacedo/DscmplcndCrçãoPctsPrcssmntImgnsPythonPrre",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)