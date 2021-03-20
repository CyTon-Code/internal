# internal modules (questions)

Here you can see the internal modules in development mode.

![questions.png](logo_internal.png)

# Как правило ожидать от функций этих библиотек можно только:
- return None - как правило почти аналогичен False - значит что задание выполнилось.
- return True - задание не выполнилось.
- return False - задание выполнилось, НО...
- raise Exception - означает, что не было сделано какое-то важное
действие (не закрылся файл, не сохранился в файл, не смог удалить файл
и т.д.)

Каждая библиотека имеет в наличии свои подводные камни, не смотря на
свой простой код (именно поэтому к каждой библиотеке будет прилагаться
документация - лучше иметь почти везде плохую документацию, чем
никакой).
