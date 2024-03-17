ROOT := $(shell pwd)
BUILD_DIR := build
BUILD_PATH := $(ROOT)/$(BUILD_DIR)
OUTPUT_DIR := outputs
OUTPUT_PATH := $(ROOT)/$(OUTPUT_DIR)

IPE_DIR := $(ROOT)/pictures/ipe
IPE_XML := $(wildcard $(IPE_DIR)/*.ipe) 
IPE_PDF := $(IPE_XML:.ipe=.pdf)

PYCHARTS_DIR := $(ROOT)/plots
PYCHARTS := $(wildcard $(PYCHARTS_DIR)/*.py)  
PYCHARTS_PGF := $(PYCHARTS:.py=.pgf)

all: $(OUTPUT_PATH)/paper.pdf

$(OUTPUT_PATH)/paper.pdf: $(BUILD_PATH)/paper.pdf  
	cp $^ $@;

open: $(OUTPUT_PATH)/paper.pdf
	xdg-open $^

$(BUILD_PATH)/paper.pdf: $(wildcard *.tex) $(wildcard tables/*.tex) $(IPE_PDF) $(PYCHARTS_PGF)
	@if [ ! -d $(BUILD_PATH) ]; then \
		mkdir $(BUILD_PATH); \
		fi && pdflatex -shell-escape -output-directory=$(BUILD_DIR) paper.tex \
		&& pdflatex -shell-escape -output-directory=$(BUILD_DIR) paper.tex

$(IPE_DIR)/%.pdf: $(IPE_DIR)/%.ipe 
	@echo $< " ----> " $@ 
	ipetoipe -pdf $< $@

$(PYCHARTS_DIR)/%.pgf: $(PYCHARTS_DIR)/%.py
	@echo $< "---->" $@
	@python $< $@

init:
	@git remote add overleaf https://git@git.overleaf.com/65db8af8509fe8bd93a1f768
	@git remote -v
	@git config --local credential.helper store
	@echo "overleaf password: olp_8D71PQGNvoUsTajPsmjAGnpuW3qVH22whFHq"
	@git fetch overleaf

overleaf_pull:
	git pull overleaf master 

overleaf_push:
	git push overleaf master 

clean:
	rm -rf $(BUILD_DIR)
	rm -rf $(IPE_DIR)/*.pdf
	rm -rf $(PYCHARTS_DIR)/*.pgf

