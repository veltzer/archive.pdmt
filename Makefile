.PHONY: all
all:
	$(info tell me something more specific)

.PHONY: clean
clean:
	rm -rf `find . -name "*.pyc"` `find . -name "*.o"` `find . -name "*.exe"`
	rm -rf build dist deb_dist

.PHONY: sdist
sdist:
	./setup.py sdist

.PHONY: build
build:
	./setup.py build

.PHONY: full
full:
	./setup.py sdist
	py2dsc dist/pdmt-1.tar.gz
	cd deb_dist/pdmt-1; debuild

.PHONY: install-deb
install-deb:
	sudo dpkg --install deb_dist/python-pdmt_1-1_all.deb
