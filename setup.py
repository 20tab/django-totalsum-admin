from setuptools import setup, find_packages
import totalsum

setup(name='twentytab-totalsum-admin',
      version=totalsum.__version__,
      description='A django app that initializes admin changelist view with last row in results as sum of some numerical fields or properties',
      author='20tab S.r.l.',
      author_email='info@20tab.com',
      url='https://github.com/20tab/twentytab-totalsum-admin',
      license='MIT License',
      install_requires=[
          'Django >=1.6',
      ],
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
      }
)
