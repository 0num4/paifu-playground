USE_POETRY ?= yes

# USE_POETRY の値によって実行コマンドを変更
ifeq ($(USE_POETRY),yes)
	RUN_PREFIX := poetry run
else
	RUN_PREFIX :=
endif

# コマンド定義
ISORT_CMD := $(RUN_PREFIX) isort --skip .venv --skip cdk.out --skip cdk
RUFF_CMD := $(RUN_PREFIX) ruff check .
FLAKE8_CMD := $(RUN_PREFIX) flake8 --max-line-length=300
MYPY_CMD := $(RUN_PREFIX) mypy --explicit-package-bases
PYRIGHT_CMD := $(RUN_PREFIX) pyright
PYTEST_CMD := $(RUN_PREFIX) pytest --ignore cdk

.PHONY: isort-check isort lint lint-flake8 lint-mypy lint-pyright

deploy:
	cd cdk && cdk deploy --require-approval never --profile ankokuyakusyo

pr:
	gh pr create --base deploy --head main --title "Release Note: $$(date '+%Y/%m/%d')" --body ""

isort-check:
	$(ISORT_CMD) --check-only .

isort:
	$(ISORT_CMD) .

test:
	$(PYTEST_CMD)

lint:
	$(RUFF_CMD) .

lint-flake8:
	$(FLAKE8_CMD) ./lambda
	$(FLAKE8_CMD) ./search_keijiban
	$(FLAKE8_CMD) ./estimate_dynamo_db_key_size.py

lint-mypy:
	$(MYPY_CMD) ./search_keijiban
	$(MYPY_CMD) ./estimate_dynamo_db_key_size.py
	$(MYPY_CMD) ./lambda

lint-pyright:
	$(PYRIGHT_CMD) ./search_keijiban
	$(PYRIGHT_CMD) ./estimate_dynamo_db_key_size.py
	$(PYRIGHT_CMD) ./lambda

# lambda-sample-lambda:
# 	aws lambda invoke --function-name sample-lambda --profile ankokuyakusyo --log-type Tail --payload '{"sutatus":"a"}' --cli-binary-format raw-in-base64-out /dev/stdout

# lambda-save-executable:
# 	aws lambda invoke --function-name save-executable --profile ankokuyakusyo --log-type Tail --payload '{}' /dev/stdout

# lambda-cost-notificator:
# 	aws lambda invoke --function-name cost-notificator --profile ankokuyakusyo --log-type Tail --payload '{}' /dev/stdout

# lambda-cost-notificator-pythonfunction:
# 	aws lambda invoke --function-name cost-notificator-pythonfunction --profile ankokuyakusyo --log-type Tail --payload '{}' /dev/stdout