ENV := PYTHONWARNINGS="ignore:Unverified HTTPS request"
ifndef VIRTUAL_ENV
PREFIX = . .venv/bin/activate ;
VENVREQ = .venv
endif

export ROBOT_LOG_PATH ?= test_results
export ROBOT_REPORT_NAME ?= AT&T Solution Smoke Test



.PHONY: test
test: $(VENVREQ) requirements
	rm -rf $(ROBOT_LOG_PATH)
	mkdir -p $(ROBOT_LOG_PATH)
	$(PREFIX) $(ENV) PYTHONPATH=`pwd` robot -d $(ROBOT_LOG_PATH) --loglevel DEBUG --name "$(ROBOT_REPORT_NAME)" --argumentfile argfile.txt

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
	echo "--extra-index-url https://artifactory.adtran.com/artifactory/api/pypi/pypi/simple" >> requirements.lock
	. .venv/bin/activate && pip freeze >> requirements.lock
	rm -rf .venv

.PHONY: requirements
requirements: $(VENVREQ) requirements.lock
	$(PREFIX) pip install -r requirements.lock

.PHONY: clean
clean:
	rm -rf .venv
	rm -rf $(ROBOT_LOG_PATH)
	find . -name '*.pyc' -delete
