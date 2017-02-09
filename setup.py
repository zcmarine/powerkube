from setuptools import setup

INSTALL_REQUIRES = [
    'kubernetes-py>=1.4.7.7',
    'powerline-status>=2.5.2',
    ]

setup(
    name='powerkube',  # Heavily inspired by the powerline-kubernetes library
    version='1.0.0',
    description='A powerline segment to show kubernetes context items, with toggling and alert color functionality',
    author='Zach Marine',  # powerline-kubernetes was written by Vincent De Smet
    author_email='zcmarine@gmail.com',  # vincent.drl@gmail.com
    url='https://github.com/zcmarine/powerkube',  # https://github.com/so0k/powerline-kubernetes
    package=['powerkube'],
    install_requires=INSTALL_REQUIRES,
    license='Copyright',
    keywords='powerline kubernetes context segment',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Apache License 2.0',
        'Topic :: Terminals'
    ]
)
