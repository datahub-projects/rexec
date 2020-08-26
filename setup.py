from setuptools import setup, find_packages
from rexec.version import version

setup(
    name="rexec",
    version=version,
    packages=find_packages(),
    python_requires='>=3',
    scripts=['bin/rexec', 'bin/rexec_auth'],
    package_data={
        "rexec_auth": ["Dockerfile"]
    },
    install_requires=[
        "blessings == 1.7",
        "apache-libcloud == 3.1.0",
	"cryptography==3.0"
    ],
    include_package_data=True
)
