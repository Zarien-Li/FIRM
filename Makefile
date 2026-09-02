.PHONY: install verify validate onboarding-test project-generator-test project-prompt-test check demo

install:
	bash install.sh

verify:
	bash scripts/verify-install.sh

validate:
	python3 scripts/validate_skills.py

onboarding-test:
	bash scripts/test-onboarding.sh

project-generator-test:
	node scripts/test_project_generator.mjs

project-prompt-test:
	node scripts/tests/test_project_generation_prompt.mjs

check:
	bash scripts/release-check.sh

demo:
	bash demo/demo.sh
