.PHONY: install verify onboarding-test demo

install:
	bash install.sh

verify:
	bash scripts/verify-install.sh

onboarding-test:
	bash scripts/test-onboarding.sh

demo:
	bash demo/demo.sh
