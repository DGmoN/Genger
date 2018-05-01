

default:
	python main.py
push:
	git add *
	git commit -m "${MSG}"
	git push
