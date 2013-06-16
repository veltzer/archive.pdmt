.PHONY: all
all:
	$(info tell me something more specific)

.PHONY: clean
clean:
	rm -rf `find . -name "*.pyc"` `find . -name "*.o"` `find . -name "*.exe"`
	rm -rf build dist deb_dist

.PHONY: clean_full
clean_full:
	git clean -xdf

.PHONY: sdist
sdist:
	./setup.py sdist

.PHONY: build
build:
	./setup.py build

.PHONY: deb
deb:
	git-buildpackage

.PHONY: install-deb
install-deb:
	sudo dpkg --install deb_dist/python-pdmt_1-1_all.deb

.PHONY: listfiles
listfiles:
	dpkg --listfiles python-pdmt
.PHONY: purge
purge:
	sudo dpkg --purge python-pdmt
