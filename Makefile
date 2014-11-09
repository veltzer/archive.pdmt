include /usr/share/templar/Makefile

ALL:=$(TEMPLAR_ALL)
ALL_DEP:=$(TEMPLAR_ALL_DEP)

#############
# Variables #
#############
# do you want to show the commands executed ?
DO_MKDBG:=0

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
	$(info doing [$@])

# source stuff

.PHONY: source-build
source-build:
	$(info doing [$@])
	$(Q)setup.py build

.PHONY: source-install
source-install:
	$(info doing [$@])
	$(Q)setup.py install

.PHONY: source-sdist
source-sdist:
	$(info doing [$@])
	$(Q)setup.py sdist

# clean

.PHONY: clean_manual
clean_manual:
	$(info doing [$@])
	$(Q)rm -rf `find . -name "*.pyc"` `find . -name "*.o"` `find . -name "*.elf"`
	$(Q)rm -rf build dist deb_dist

.PHONY: clean
clean:
	$(info doing [$@])
	$(Q)git clean -xdf > /dev/null

# checking

.PHONY: check_main
check_main:
	$(info doing [$@])
	$(Q)-git grep __main -- "*.py"
.PHONY: check_semicol
check_semicol:
	$(info doing [$@])
	$(Q)-git grep ";$$" -- "*.py"

.PHONY: check_all
check_all: check_main check_semicol
	$(info doing [$@])

# deb building

# where to build source packages?
PKG_TIGHT:=$(tdefs.deb_pkgname)_$(tdefs.git_lasttag)
PKG_BASE:=$(PKG_TIGHT)_all
PKG:=$(PKG_BASE).deb
PKG_FULL:=$(tdefs.deb_repo)/$(PKG)
PKG_CHANGES:=$(PKG_TIGHT)_source.changes
PKG_LOCAL:=$(tdefs.deb_build_all)/$(PKG)

.PHONY: deb-debug
deb-debug:
	$(info doing [$@])
	$(info PKG_TIGHT is $(PKG_TIGHT))
	$(info PKG_BASE is $(PKG_BASE))
	$(info PKG is $(PKG))
	$(info PKG_FULL is $(PKG_FULL))
	$(info PKG_CHANGES is $(PKG_CHANGES))
	$(info PKG_LOCAL is $(PKG_LOCAL))

# we must do hard clean in the next target because debuild will take everything,
# including results of building of other stuff, into the source package
.PHONY: deb-build-gbp
deb-build-gbp:
	$(info doing [$@])
	$(Q)-rm -f ../$(tdefs.deb_pkgname)_*
	$(Q)git clean -xdf > /dev/null;make templar;rm .tdefs.config
	$(Q)-mkdir $(tdefs.deb_build_gbp)
	$(Q)git-buildpackage > /tmp/git-buildpackage.log
	$(Q)mv ../$(tdefs.deb_pkgname)_* $(tdefs.deb_build_gbp)
	$(Q)chmod 444 $(tdefs.deb_build_gbp)/$(tdefs.deb_pkgname)_*

# we must do hard clean in the next target because debuild will take everything,
# including results of building of other stuff, into the source package
.PHONY: deb-build-debuild-all
deb-build-debuild-all:
	$(info doing [$@])
	$(Q)-rm -f ../$(tdefs.deb_pkgname)_*
	$(Q)git clean -xdf > /dev/null;make templar;rm .tdefs.config
	$(Q)-mkdir $(tdefs.deb_build_all)
	$(Q)debuild > /tmp/debuild.log
	$(Q)mv ../$(tdefs.deb_pkgname)_* $(tdefs.deb_build_all)
	$(Q)chmod 444 $(tdefs.deb_build_all)/$(tdefs.deb_pkgname)_*

# we must do hard clean in the next target because debuild will take everything,
# including results of building of other stuff, into the source package
.PHONY: deb-build-debuild-source
deb-build-debuild-source:
	$(info doing [$@])
	$(Q)-rm -f ../$(tdefs.deb_pkgname)_*
	$(Q)git clean -xdf > /dev/null;make templar;rm .tdefs.config
	$(Q)-mkdir $(tdefs.deb_build_source)
	$(Q)debuild -S > /tmp/debuild_s.log
	$(Q)mv ../$(tdefs.deb_pkgname)_* $(tdefs.deb_build_source)
	$(Q)chmod 444 $(tdefs.deb_build_source)/$(tdefs.deb_pkgname)_*

.PHONY: deb-install
deb-install: deb-build-debuild-all
	$(info doing [$@])
	$(Q)sudo dpkg --install $(PKG_LOCAL)

.PHONY: deb-local-contents
deb-local-contents:
	$(info doing [$@])
	$(Q)dpkg --contents $(PKG_LOCAL)

.PHONY: deb-local-info
deb-local-info:
	$(info doing [$@])
	$(Q)dpkg --info $(PKG_LOCAL)

.PHONY: deb-local-all
deb-local-all: deb-local-contents deb-local-info

# move the package to somewhere

.PHONY: deb-dput
deb-dput: deb-build-debuild-source
	$(info doing [$@])
	$(Q)dput $(tdefs.launchpad_ppa) $(tdefs.deb_build_source)/$(PKG_CHANGES)

.PHONY: deb-archive
deb-archive: deb-build-debuild-all
	$(info doing [$@])
	$(Q)-rm -f $(tdefs.deb_repo)/$(tdefs.deb_pkgname)_*
	$(Q)cp $(tdefs.deb_build_all)/$(tdefs.deb_pkgname)_* $(tdefs.deb_repo)

.PHONY: deb-archive-contents
deb-archive-contents:
	$(info doing [$@])
	$(Q)dpkg --contents $(PKG_FULL)

.PHONY: deb-archive-info
deb-archive-info:
	$(info doing [$@])
	$(Q)dpkg --info $(PKG_FULL)

.PHONY: deb-archive-all
deb-archive-all: deb-archive-contents deb-archive-info

.PHONY: deb-installed-listfiles
deb-installed-listfiles:
	$(info doing [$@])
	$(Q)dpkg --listfiles $(tdefs.deb_pkgname)

.PHONY: deb-installed-status
deb-installed-status:
	$(info doing [$@])
	$(Q)dpkg --status $(tdefs.deb_pkgname)

.PHONY: deb-installed-purge
deb-installed-purge:
	$(info doing [$@])
	$(Q)sudo dpkg --purge $(tdefs.deb_pkgname)
