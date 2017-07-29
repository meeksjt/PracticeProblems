ENV := PYTHONWARNINGS="ignore:Unverified HTTPS request"
ifndef VIRTUAL_ENV
PREFIX = . .venv/bin/activate ;
VENVREQ = .venv
endif


.PHONY: test
test: $(VENVREQ) requirements
	$(PREFIX) $(ENV) PYTHONPATH=`pwd` python src/hangman.py 'words.txt'

.venv:
	virtualenv .venv
	$(PREFIX) pip install --upgrade pip

.PHONY: freeze
freeze:
	rm -rf .venv
	virtualenv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	echo "# WARNING: This file is auto-generated." > requirements.lock
	echo "# Edit requirements.txt instead and run 'make freeze' to regenerate this file." >> requirements.lock
	. .venv/bin/activate && pip freeze >> requirements.lock
	rm -rf .venv

.PHONY: requirements
requirements: $(VENVREQ) requirements.lock
	$(PREFIX) pip install -r requirements.lock

.PHONY: clean
clean:
	rm -rf .venv
	find . -name '*.pyc' -delete
