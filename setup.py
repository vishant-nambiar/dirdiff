from distutils.core import setup
setup(
  name = 'dirdiff',        
  packages = ['dirdiff'],   
  version = '0.9',     
  license='gpl-3.0',        
  description = 'A utility to diff and patch entire directories, similiar to the GNU diff and patch for files.',  
  author = 'Vishant Nambiar',                  
  author_email = 'vishantnambiar@gmail.com',     
  url = 'https://github.com/vishant-nambiar/dirdiff',  
  download_url = 'https://github.com/vishant-nambiar/dirdiff/archive/refs/tags/0.9.tar.gz',   
  keywords = ['diff', 'patch', 'directories', 'folders', 'bash'],   
  install_requires=[            
          'subprocess',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: gpl-3.0',  
    'Programming Language :: Python :: 3',     
  ],
)