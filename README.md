# Chance decorator

Декоратор with_chance, который либо вернет результат функции с заданной вероятностью, либо вернет значение по умолчанию.
В случае отсутствия значения по умолчанию, должно быть вызвано исключение.
В случае если в декоратор передана не функция, должно быть вызвано исключение.

```
@with_chance(50, "Default Value")
def some_fn(*args, **kwargs):
    pass
```

### Run tests
```
python decorators.py
```
