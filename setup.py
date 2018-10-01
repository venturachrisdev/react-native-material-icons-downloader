import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="react_native_material_icons",
    version="0.0.1",
    author="Christopher Ventura",
    author_email="venturachrisdev@gmail.com",
    description="Download icons from https://material.io in React Native icons format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/venturachrisdev/react-native-material-icons-downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)