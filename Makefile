test-upload:
	python setup.py sdist upload -r pypitest

upload:
	python setup.py sdist upload -r pypi
