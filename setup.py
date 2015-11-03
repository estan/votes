from setuptools import setup, find_packages

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass={'build_ui': build_ui}
except ImportError:
    cmdclass={}

setup(
    name='votes',
    version='0.1',
    description='PyQt5 + Autobahn/Twisted version of Votes Crossbar demo',
    url='http://github.com/estan/votes',
    author='Elvis Stansvik',
    license='License :: OSI Approved :: MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    install_requires=[
        'autobahn',
        'twisted',
        'pyOpenSSL',
        'service_identity',
        'qt5reactor',
    ],
    entry_points={
        'gui_scripts': [
            'votes-qt=votes.frontend:main'
        ],
    },
    cmdclass=cmdclass
)
