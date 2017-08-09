
# non file targets
.PHONY: test clean

# Remove
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf .coverage

# Targets for Coruscate testing
test:
	nosetests -v -w tests/
