from setuptools import setup, find_packages

setup(
    version='0.0.1',
    author='Gui Martins',
    name='fancydocket',
    website='https://fancywhale.ca',
    email='gmartins@fancywhale.ca',
    description='Fancy writing for your next docket',
    packages=find_packages(),
    install_requires=[
        'click',
        'iterfzf'
    ],
    entry_points="""
    [console_scripts]
    fancydocket=fancydocket:fancydocket
    """
)