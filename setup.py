from setuptools import setup

setup(
        name="Runner",
        version="0.1",
        py_modules=["runner"],
        install_requires=[
            'Click',
        ],
        entry_points={
            "console_scripts": [
                "runner=runner:main",
                ]
            }
)
