import os

from setuptools import setup


def find_stub_files():
    result = []
    for root, dirs, files in os.walk("sqlalchemy"):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(
    packages=["sqlalchemy"],
    package_data={"sqlalchemy": find_stub_files()},
)
