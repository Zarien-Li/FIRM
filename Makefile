.PHONY: install verify validate onboarding-test check demo

install:
	bash install.sh

verify:
	bash scripts/verify-install.sh

validate:
	python3 scripts/validate_skills.py

onboarding-test:
	bash scripts/test-onboarding.sh

check:
	bash scripts/release-check.sh

demo:
	bash demo/demo.sh
