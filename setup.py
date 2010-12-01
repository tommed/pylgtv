from distutils.core import setup

setup(name='pylgtv',
        version='1.0',
        description='Python tool for controlling LG TVs and other domestic devices',
        author='Thomas Medhurst',
        author_email='tom@tommed.co.uk',
        url='http://www.tommed.co.uk'
        packages=[
                'pylgtv',
                'pylgtv.televisions',
                'pylgtv.televisions.lg',
                'pylgtv.test',
                'pylgtv.test.tools',
                ],
        )
