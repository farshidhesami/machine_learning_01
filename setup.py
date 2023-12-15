import setuptools

# Read the README file for the package's long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Read the list of required packages from requirements.txt
with open('requirements.txt') as f:
    required_packages = [line for line in f.read().splitlines() if not line.startswith('-e')]

__version__ = "0.0.0"  

REPO_NAME = "machine_learning_01"
AUTHOR_USER_NAME = "farshidhesami"
SRC_REPO = "MachineLearning_2023"
AUTHOR_EMAIL = "farshidhesami@gmail.com"

# Define package metadata and configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small Python package for machine learning projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    keywords="machine-learning ml data-science",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires='>=3.6',
    install_requires=required_packages,
)

