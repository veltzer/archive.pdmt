include /usr/share/templar/Makefile

ALL:=$(TEMPLAR_ALL)
ALL_DEP:=$(TEMPLAR_ALL_DEP)

#############
# Variables #
#############
# do you want to show the commands executed ?
# Since we are using ?= for assignment it means that you can just
# set this from the command line and avoid changing the makefile...
DO_MKDBG?=0

#########
# Logic #
#########
# silent stuff
ifeq ($(DO_MKDBG),1)
Q:=
# we are not silent in this branch
else # DO_MKDBG
Q:=@
#.SILENT:
endif # DO_MKDBG

#########
# Rules #
#########
.DEFAULT_GOAL=all
.PHONY: all
all: $(ALL)

# source stuff

.PHONY: source-build
source-build:
	$(info doing $@)
	$(Q)setup.py build

.PHONY: source-install
source-install:
	$(info doing $@)
	$(Q)setup.py install

.PHONY: source-sdist
source-sdist:
	$(info doing $@)
	$(Q)setup.py sdist

# clean

.PHONY: clean_manual
clean_manual:
	$(info doing $@)
	$(Q)rm -rf `find . -name "*.pyc"` `find . -name "*.o"` `find . -name "*.elf"`
	$(Q)rm -rf build dist deb_dist

.PHONY: clean
clean:
	$(info doing $@)
	$(Q)git clean -xdf

# creating a debian package

.PHONY: deb2
deb2:
	$(error dont use this)
	rm -f ../pdmt-* ../pdmt_*
	git clean -xdf
	python setup.py sdist --dist-dir=../ --prune
#	python setup.py sdist --dist-dir=../
	dpkg-buildpackage -i -I -rfakeroot

.PHONY: deb
deb:
	rm -f ../pdmt-* ../pdmt_*
	git clean -xdf
	git-buildpackage --git-ignore-new
	mv ../pdmt_* ~/packages/

.PHONY: install-deb
install-deb:
	sudo dpkg --install deb_dist/pdmt_1-1_all.deb

.PHONY: listfiles
listfiles:
	dpkg --listfiles pdmt
.PHONY: purge
purge:
	sudo dpkg --purge pdmt
.PHONY: results
results:
	dpkg --contents ~/packages/pdmt_$(VER)_all.deb
	dpkg --info ~/packages/pdmt_$(VER)_all.deb

.PHONY: check_main
check_main:
	@-git grep __main -- "*.py"
.PHONY: check_semicol
check_semicol:
	@-git grep ";$$" -- "*.py"

.PHONY: check_all
check_all: check_main check_semicol
