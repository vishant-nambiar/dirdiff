from distutils.core import setup
setup(
  name = 'dirdiff',         # How you named your package folder (MyLib)
  packages = ['dirdiff'],   # Chose the same as "name"
  version = '0.9',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A utility to diff and patch entire directories, similiar to the GNU diff and patch for files.',   # Give a short description about your library
  author = 'Vishant Nambiar',                   # Type in your name
  author_email = 'vishantnambiar@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vishant-nambiar/dirdiff',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['diff', 'patch', 'directories', 'folders', 'bash'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'subprocess',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)