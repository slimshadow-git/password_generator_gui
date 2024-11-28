from setuptools import setup, find_packages

setup(
    name="password_generator_gui",  # Name of the package
    version="0.1",  # Version number
    description="A simple password generator GUI using Tkinter",
    long_description=open('README.md').read(),  # Description from README
    long_description_content_type="text/markdown",
    author="slimshadow",  # Your name or organization
    author_email="slimshadow-code@gmail.com",  # Your email
    url="https://github.com/slimshadow-git/password_generator_gui",  # Link to the project repo
    packages=find_packages(where='src'),  # Find all the Python packages inside the 'src' folder
    package_dir={"": "src"},  # Tells setuptools where the packages are located
    install_requires=[  # List of required dependencies
        "tkinter",  # Add other dependencies like 'pytest', 'requests', etc. if needed
    ],
    classifiers=[  # These help categorize your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
