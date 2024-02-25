ROOT := $(shell pwd)
BUILD_DIR := build
BUILD_PATH := $(ROOT)/$(BUILD_DIR)
OUTPUT_DIR := outputs
OUTPUT_PATH := $(ROOT)/$(OUTPUT_DIR)

all: $(OUTPUT_PATH)/paper.pdf

open: $(OUTPUT_PATH)/paper.pdf
	xdg-open $^

$(OUTPUT_PATH)/%.pdf: $(BUILD_PATH)/%.pdf 
	mv $^ $@;

$(BUILD_PATH)/%.pdf: %.tex
	@cd thesis; \
		if [ ! -d $(BUILD_PATH) ]; then \
		mkdir $(BUILD_PATH); \
		fi && pdflatex -shell-escape -output-directory=$(BUILD_DIR) $< \
		&& pdflatex -shell-escape -output-directory=$(BUILD_DIR) $<

overleaf_pull:
	git pull overleaf master 

overleaf_push:
	git push overleaf master 

clean:
	rm -rf $(BUILD_DIR)
