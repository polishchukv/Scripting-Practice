import pkg_resources

installed_packages = {pkg.key for pkg in pkg_resources.working_set}

if 'openai' in installed_packages:
    print("The 'openai' package is installed!")
else:
    print("The 'openai' package is NOT installed.")
