from setuptools import setup, find_packages

setup(
    name="app",
    version="0.0.0",
    description="TODO",
    author="Xinyuan Yao",
    author_email="yao.ntno@google.com",
    license="TODO",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "cytoolz",
        "matplotlib",
        "torch",
        "kaggle",
        "tqdm",
        "scikit-image",
        "torchvision",
        "albumentations",
        "typing_extensions",
        "object_detection @ git+https://github.com/h4nyu/object-detection",
    ],
    extras_require={"dev": ["mypy", "pytest", "black",]},
    entry_points={"console_scripts": ["app=app.cmd:main"],},
)
