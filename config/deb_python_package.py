# deb section
deb_package = True
deb_section = "python"
deb_priority = "optional"
deb_architecture = "all"
deb_pkgname = "pdmt"
# to which series to publish the package?
deb_series = [
    "artful",
    "zesty",
    "xenial",
    "trusty",
]
deb_depends = "${misc:Depends}, ${python3:Depends}, python3-mako"
deb_builddepends = "python3, python3-setuptools, debhelper, dh-python"
deb_standards_version = "3.9.8"
deb_x_python_version = ">= 3.4"
deb_x_python3_version = ">= 3.4"
deb_urgency = "low"
entry_points = {
    "console_scripts": [
    ],
}
