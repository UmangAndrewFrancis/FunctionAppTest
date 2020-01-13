FUNCTION_NAME=$(notdir $(shell pwd))
BUILD_FOLDER=$(shell pwd)/target
LIBRARY_FOLDER=$(shell pwd)/libraries

clean:
	rm -rf "$(BUILD_FOLDER)"
build: 
	printf 'Building $(FUNCTION_NAME)\n'
	python3 -m pip install -r requirements.txt -t ./
	mkdir -p "$(BUILD_FOLDER)"
	zip -r "$(BUILD_FOLDER)/$(FUNCTION_NAME).zip" ./ -x@zipignore.lst -q