from setuptools import setup


setup(
    name="igi_lab3_Oleg",
    version="1.0",
    description="library for python serialization",
    url="https://github.com/OlegErshov/IGI/tree/Lab3/Lab3",
    author="Ershov Oleg",
    author_email="olezhka1629@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["Serializer/Json_Serialization", "Serializer/Base",
              "Serializer/Xml_Serialization", "Serializer"],
    include_package_data=True
)