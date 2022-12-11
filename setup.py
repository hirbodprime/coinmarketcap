import setuptools


with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bing-background',
    version='0.0.1',
    author='hirbod aflaki',
    author_email='hirbodprime@gmail.com',
    description='downloads coinmarketcap data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hirbodprime/coinmarketcap.git',
    # project_urls = {
        # "Bug Tracker": "https://git.pe42.ir/hirbod/bing-background-python/issues"
    # },
    keywords=['python', 'coin','coinmarketcap' 'beautifulsoup','requests','data','coin data'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license='MIT',
    packages=['coinmarketcap'],
    install_requires=['beautifulsoup4' , 'requests' , 'colorama'],
)