import sqlite3


class GroupsDB:
    __table = '`groups`'

    def __init__(self, path_database):
        """Підключаємося до БД и зберігаємо курсор з'єднання"""
        self.connection = sqlite3.connect(path_database)
        self.cursor = self.connection.cursor()

    def group_exists(self, group_id):
        """
        Чи група присутня
        """
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {self.__table} WHERE `id` = ?', (group_id,)).fetchall()
        return bool(len(result))

    def add_group(self, group_id: int, tag: str = None, name: str = None):
        """Добавляем групу"""
        with self.connection:
            self.cursor.execute(f"INSERT INTO {self.__table} (`id`, `tag`,`name`) VALUES(?,?,?)",
                                (group_id, tag, name))

    def group_exists_and_add(self, group_id: int, tag: str = '', name: str = ''):
        with self.connection:
            if not self.group_exists(group_id):
                self.add_group(group_id, tag, name)
            return self.group_exists(group_id)

    def group_exists_and_update_or_add(self, group_id: int, tag: str = '', name: str = ''):
        with self.connection:
            if not self.group_exists(group_id):
                return self.add_group(group_id, tag, name)
            self.update_groups(group_id, tag, name)

    def get_all_id_groups(self, column_find: str):
        """Получаем id всех активных подписчиков бота"""
        with self.connection:
            result = self.cursor.execute(f"SELECT {column_find} FROM {self.__table}").fetchall()
            return (column[0] for column in result)

    def update_groups(self, group_id: int, tag: str = None, name: str = None):
        """Оновимо"""
        with self.connection:
            self.cursor.execute(f"UPDATE {self.__table} SET `tag` = ? WHERE `id` = ? ",
                                (tag, group_id))

            self.cursor.execute(f"UPDATE {self.__table} SET `name` = ? WHERE `id` = ? ",
                                (name, group_id))

    def remove_group(self, id_group: int):
        """Видалимо групу з БД"""
        with self.connection:
            self.cursor.execute(f"DELETE FROM {self.__table} WHERE `id` = ?", (id_group,))

    def group_exists_and_remove(self, group_id: int):
        with self.connection:
            if self.group_exists(group_id):
                self.remove_group(group_id)

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()


class ParameterDB:

    def __init__(self, path_database, table):
        """Підключаємося до БД и зберігаємо курсор з'єднання"""
        self.connection = sqlite3.connect(path_database)
        self.cursor = self.connection.cursor()
        self.__table = table

    def exists(self, name: str):
        """
        Чи присутній параметр
        """
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {self.__table} WHERE `name` = ?', (name,)).fetchall()
        return bool(len(result))

    def add(self, name: str, status: bool = False):
        """Добавляем"""
        with self.connection:
            self.cursor.execute(f"INSERT INTO {self.__table} (`name`, `status`) VALUES(?,?)",
                                (name, status))

    def update(self, name: str, status: [bool, str]):
        """Оновимо"""
        with self.connection:
            self.cursor.execute(f"UPDATE {self.__table} SET `status` = ? WHERE `name` = ? ",
                                (status, name))

    def get_name(self, name: str):
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM {self.__table} WHERE `name` = ?', (name,)).fetchone()
        return result[1]

    def exists_and_update_or_add(self, name: str, status: bool = False):
        with self.connection:
            if not self.exists(name=name):
                return self.add(name=name, status=status)
            self.update(name=name, status=status)
