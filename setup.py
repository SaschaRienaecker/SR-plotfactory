from setuptools import setup, find_packages

setup(
    name='plotfactory',
    version='1.0.0',
    author='SR',
    author_email='your.email@example.com',
    description='',
    packages=find_packages(),  # Automatically discover and include all packages
    include_package_data=True,
    package_data={
        '': ['*.mplstyle'],
        # or specify the specific package where the mplstyle files are located
        # 'your_package_name': ['*.mplstyle']
    },
    install_requires=[
        # List the dependencies your package needs
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        # 'Development Status :: 3 - Alpha',
        # 'Intended Audience :: Developers',
        # 'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3.8',
        # Add other classifiers as needed
    ],
    entry_points={
        'console_scripts': [
            # Define any command-line scripts your package provides
        ],
    },
)
