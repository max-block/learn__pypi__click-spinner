from setuptools import find_packages, setup

setup(
    name="learn",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click==7.1.2", "click-spinner==0.1.10"],
    entry_points={"console_scripts": ["app = main:cli"]},
)
