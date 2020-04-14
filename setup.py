from distutils.core import setup

setup(
  name = 'trtl',         
  packages = ['trtl'],
  version = '0.1',      
  license='MIT',        
  description = 'The Python RPC Wrapper for TurtleCoind and WalletAPI.',   
  author = 'Sayan Bhattacharyya',                
  author_email = 'sohamb03@outlook.com',    
  url = 'https://github.com/sohamb03/trtl-py', 
  download_url = 'https://github.com/sohamb03/trtl-py/archive/v_01.tar.gz',    
  keywords = ['turtlecoin', 'turtlecoind', 'wallet-api', 'py-wrapper'],   
  python_requires=">=3.6",
  install_requires=[           
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  project_urls={
        'Documentation': 'https://trtl-py.sohamb03.me',
  },
)
