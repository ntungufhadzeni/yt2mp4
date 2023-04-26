from setuptools import setup

setup(
    name='yt2mp4',
    version='0.0.1',
    install_requires=["pytube==12.1.2"],
    packages=['yt2mp4'],
    entry_points={
        'console_scripts': [
            'yt2mp4 = yt2mp4.main:main',
        ]
    }
    
)