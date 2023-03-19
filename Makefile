run:
	python -m project.src.main

run_test: 
	python -m unittest discover -s tests -t project

run_test_m: 
	python -m unittest discover -s tests.test_main.TestMain -t project
