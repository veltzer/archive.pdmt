.PHONY: all
all:
	$(info tell me something more specific)

.PHONY: clean
clean:
	rm -rf `find . -name "*.pyc"` `find . -name "*.o"` `find . -name "*.exe"`
