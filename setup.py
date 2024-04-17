from setuptools import setup, find_packages

setup(
    name="probatus",
    version="0.1.0",
    description="CLI Python API Testing Tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/probatus",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.24,<3",
        "PyYAML>=5.3,<6",
        "colorama>=0.4.4,<0.5",
        "argparse>=1.4.0,<2"
    ],
    entry_points={
        "console_scripts": [
            "probatus=probatus.__main__:main",
        ],
    },
    python_requires='>=3.8',
)