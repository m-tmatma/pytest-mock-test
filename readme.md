# test for pytest-mock

This repository is for testing [pytest-mock](https://github.com/pytest-dev/pytest-mock)


## On Ubuntu

### how to prepare (事前準備)

Run this command to run on python3 and install `pytest` and `pytest-mock`.
(python3 上で実行するために以下のコマンドで `pytest` および `pytest-mock` をインストールする。)

```
sudo apt install -y python3-pytest python3-pytest-mock
```

### How to run (実行方法)

The point to run on ubuntu is use `pytest-3` on ubuntu.(Ubuntu 上で実行する場合のポイントは `pytest-3` を使うこと。)

#### run all tests in the current directory. (カレントディレクトリにあるすべてのテストを実行)

```
pytest-3 -vv .
```

#### run all tests in the specified test script. (指定したスクリプトのすべてのテストを実行)

```
pytest-3 -vv ./test_builtin_mock.py
```
