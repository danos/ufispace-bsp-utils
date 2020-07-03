clean:
	rm -rf ../../output/tmp/python_tmp/

install:
	mkdir -p ../../output/tmp/python_tmp/
	find . -name "__pycache__" -type d -exec rm -r "{}" \;
	cp -r python/* ../../output/tmp/python_tmp/
	install python/platform_utility.py ../../output/usr/sbin/

.PHONY: clean
