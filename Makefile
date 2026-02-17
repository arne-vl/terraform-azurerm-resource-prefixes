default:
	python codegen.py
	terraform fmt -recursive
