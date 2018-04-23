PY=python

testProgram:
	$(PY) main.py

testImage:
	$(PY) -c "import test.imageTest"
