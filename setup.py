from setuptools import setup

setup(name='ytdowndp',
      version='0.0.2',
      description='MP3 downloader wrapper made with pytube',
      url='https://github.com/danielpanaite/ytdown',
      author='danielpanaite',
      author_email='dani.panaite@gmail.com',
      license='GPL-3.0',
      packages=['ytdowndp'],
      install_requires=[
          'pytube',
      ],
      zip_safe=False)