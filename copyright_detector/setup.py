import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    name="copyright_detector",
    version="0.1",
    description="exercise",
    long_description=readme(),
    url='#',
    author='...',
    author_email='sm.marouzi@gmailmail.com',
    packages=['copyright_detector'],
    install_requires=[
          "nltk",
          "scikit-learn",
          "numpy",
          ],
    include_package_data=True,
    zip_safe=False
    )
