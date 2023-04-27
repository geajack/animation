import setuptools

setuptools.setup(
    name="animation",
    version="1.0.0",
    author="j3m",
    packages=["animation"],
    entry_points={
        "console_scripts": ["animate=animation.cli:main"]
    },
    install_requires=["pygame", "opencv-python"]
)