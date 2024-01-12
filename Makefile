all: install run

install:
	brew install ollama

run:
	ollama run mistral

clean:
	brew uninstall ollama

new-model:
	ollama create new-model -f Modelfile

run-new-model:
	ollama run new-model
