from setuptools import (
    find_packages,
    setup,
)

setup(
    name="weechat-relay-parser",
    version="0.0.1.dev1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'bitstring',
    ],
    author="Yuval Langer",
    author_email="yuval.langer@gmail.com",
    description="WeeChat Relay Protocol parser",
    license="AGPL3+",
    keywords="irc weechat relay protocol parser",
    url="https://gitgud.io/yuvallanger/weechat-relay-parser/",
)
