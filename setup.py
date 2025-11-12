setup(
    name='nlltk',                      # ← new package name
    version='1.0.2',
    description='NLLTK: Natural Learning Lab Toolkit - All LP-1 ML Experiments + PDFs',
    author='Shubham Bhorkade',
    packages=find_packages(),
    include_package_data=True,
    package_data={'nlltk': ['data/*.pdf']},
    install_requires=['pandas','numpy','scikit-learn','matplotlib','scipy','mlxtend']
)
