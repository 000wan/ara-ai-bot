.PHONY: run test

run:
	python main.py $(filter-out $@,$(MAKECMDGOALS))

test:
	python test.py $(filter-out $@,$(MAKECMDGOALS))

%:
	@: