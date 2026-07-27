.PHONY: install verify demo

install:
	bash install.sh

verify:
	bash scripts/verify-install.sh

demo:
	bash demo/demo.sh
