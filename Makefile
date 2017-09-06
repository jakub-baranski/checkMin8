default: install

virtualenv_v := '${shell pip show virtualenv}'
current_dir := $(shell pwd)

install:
	make test
	virtualenv venv -p python3
	${shell . venv/bin/activate}
	venv/bin/pip install -r requirements.txt

test:
	$(if $(findstring virtualenv,$(virtualenv_v)),\
		$(info OK),\
		$(error   Looks like virtualenv is missing))

