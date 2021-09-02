from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'dirdiff',        
  packages = ['dirdiff'],   
  version = '1.0',     
  license='gpl-3.0',        
  description = 'A utility to diff and patch entire directories, similiar to the GNU diff and patch for files.',
  long_description=long_description,
  long_description_content_type="text/markdown", 
  author = 'Vishant Nambiar',                  
  author_email = 'vishantnambiar@gmail.com',     
  url = 'https://github.com/vishant-nambiar/dirdiff',  
  download_url = 'https://github.com/vishant-nambiar/dirdiff/archive/refs/tags/1.0.tar.gz',   
  keywords = ['diff', 'patch', 'directories', 'folders', 'bash'],   
  install_requires=[            
          'subprocess',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
    'Programming Language :: Python :: 3',     
  ],
)