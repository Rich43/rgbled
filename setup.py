from setuptools import setup

setup(name='rgbled',
    version='1.0',
    description='rgbled',
    author='Rich Ward',
    author_email='rward@python.net',
    url='https://www.rgbled.com/',
    packages=['rgbled'],
    install_requires=['PyQT5', 'pyqt5-tools', 'pyserial']
)
