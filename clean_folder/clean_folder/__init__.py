from setuptools import setup, find_namespace_packages

setup(
    name='useful',
    version='1',
    description='Very useful code',
    url='http://github.com/dummy_user/useful',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
<<<<<<< HEAD
)
=======
)
>>>>>>> cedbeb6bad83c1864ab4bd51b35fccfefa79baf1
