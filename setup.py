from setuptools import setup

packages = [
    "numpy",
    "scipy",
    "matplotlib",
    "scikit-learn",
    "tensorflow",
    "cvxpy",
    "torch",
    "geopandas",
    "pymanopt",
    "pandas",
    "mosek",
    "stpy",
    "pytorch-minimize",
]
#
setup(
    name="sensepy",
    version="0.0.2",
    description="Point process sensing library",
    url="",
    author="Mojmir Mutny",
    author_email="mojmir.mutny@inf.ethz.ch",
    license="MIT licence",
    packages=["sensepy"],
    zip_safe=False,
    install_requires=packages,
)
