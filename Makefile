default:
	@echo "Nothing to do by default. Please read the manual."

# -- Python Virtual Env machinery --------------------
virtualenv.installed: _venv/bin/activate

_venv/bin/activate: requirements.txt
	test -d _venv || virtualenv _venv
	_venv/bin/pip install -Ur requirements.txt
	touch _venv/bin/activate

virtualenv:
	@if test "$(VIRTUAL_ENV)" = "" ; then \
		echo "**** Please first start your virtualenv : source _venv/bin/activate ****"; \
		exit 1; \
	fi

# -- Install section --------------------

install: install.pkg install.python

install.pkg:
	sudo apt-get update
	sudo apt-get install ipython python-pip

install.python: virtualenv.installed

# -- Update section --------------------

update: virtualenv update.git

update.git:
	git pull
