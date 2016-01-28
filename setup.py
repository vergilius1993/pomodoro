try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Command Line Pomodoro',
    'author': 'vergilius',
    'url': 'github.com/vergilius1993/pomodoro',
    'download': 'git clone https://github.com/vergilius1993/pomodoro.git',
    'author_email': 'lucius0720@hotmail.com',
    'version': '0.1',
    'install_request': ['nose'],
    'packages': ['NAME'],
    'script': [],
    'name': 'Pomodoro'
}
setup(**config)
