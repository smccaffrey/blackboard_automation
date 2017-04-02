from setuptools import setup, find_packages

version = '0.1.0'

setup(name="PIRT ASU",
      version=version,
      author="Sam McCaffrey",
      author_email="samccaff@asu.edu",
      license="Apache-2.0",
      scripts=['scripts/bulk_upload'],
      install_requires=['selenium',
                        'getpass',
                        'xlrd',
                        ],
      zip_safe=True,
)
