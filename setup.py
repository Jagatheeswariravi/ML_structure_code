from setuptools import find_packages,setup
from typing import List

hypen = "-e ."

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path,"r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)

    return requirements

    

setup(

    name = "ML_structure_code",
    author="Jagatheeswari Ravi",
    author_email="jagavirat1010@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)