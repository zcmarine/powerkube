from setuptools import setup

INSTALL_REQUIRES = [
    'kubernetes-py',
    'powerline-status',
    ]

# Heavily inspired by the powerline-kubernetes library written by Vincent De Smet
# (vincent.drl@gmail.com) and located at https://github.com/so0k/powerline-kubernetes
setup(
    name='powerkube',
    version='0.1.0',
    description='A powerline segment to show kubernetes context items, with toggling and alert color functionality',
    author='Zach Marine',
    author_email='zcmarine@gmail.com',
    url='https://github.com/zcmarine/powerkube',
    download_url='https://github.com/zcmarine/powerkube/tarball/0.1',
    package=['powerkube'],
    install_requires=INSTALL_REQUIRES,
    license='Copyright',
    keywords='powerline kubernetes k8s context segment',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Terminals'
    ]
)
