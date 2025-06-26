from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cnnClassifier",
    version="0.0.1",
    author="Harshad Humane",
    author_email="harshadhumane.scoe.mech@gmail.com",
    description="CNN-based deep learning project for kidney disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshadhumane18/Kidney-Disease-Classification-Deep-Learning-Project",
    project_urls={
        "Bug Tracker": "https://github.com/harshadhumane18/Kidney-Disease-Classification-Deep-Learning-Project/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
)
