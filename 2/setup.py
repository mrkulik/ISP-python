from setuptools import setup

scripts_list = ['lab2/xrange.py', 'lab2/my_json.py', 'lab2/vector.py',
                'lab2/sequence.py', 'lab2/cached.py', 'lab2/logger.py',
                'lab2/sequence.py', 'lab2/multidimensional_dict.py', 'lab2/singleton.py',
                'lab2/model_creator.py', 'lab2/attribute_writer.py']

setup(name='lab2',
      version='1.0',
      description='Run start.py',
      author='Kulik Gleb',
      author_email='mr.kulik23@gmail.com',
      packages=['lab2'],
      scripts=scripts_list
     )
