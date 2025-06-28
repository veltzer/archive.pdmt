""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
requires = config_requires + build_requires
