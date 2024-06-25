class Friends:
    def __init__(self, connections):
        self.connections = [tuple(sorted(connection)) for connection in connections]
        self.all_names = set.union(*[set(connection) for connection in connections])

    def add(self, connection):
        connection = tuple(sorted(connection))
        if connection not in self.connections:
            self.connections.append(connection)
            self.all_names.update(connection)
            return True
        return False

    def remove(self, connection):
        connection = tuple(sorted(connection))
        if connection in self.connections:
            self.connections.remove(connection)
            self.all_names -= set(connection)
            return True
        return False

    def get_names(self):
        return self.all_names

    def connected(self, name):
        connected_names = set()
        for connection in self.connections:
            if name in connection:
                connected_names.update(set(connection) - {name})
        return connected_names


# Создаем обьект класса Friends c некоторыми связями
f = Friends([{"a", "b"}, {"b", "c"}, {"c", "a"}])


# Вывод имен, указанных в соединениях
print(f.get_names())

# Добавить новое соединение
f.add({"a", "d"})
print(f.get_names())

# Удалить соединение
f.remove({"c", "a"})
print(f.get_names())

# Проверить, кто связан с "a"
print(f.connected("a"))

# Проверить, кто связан с "d"
print(f.connected("d"))

# Попробовать добавить соединение, которое уже существует
print(f.add({"a", "b"}))

# Попробовать удалить несуществующее соединение
print(f.remove({"e", "f"}))
