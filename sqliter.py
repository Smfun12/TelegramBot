import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status=True):
        """Получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_name):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_name` = ?', (user_name,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_name, status=True):
        """Добавляем нового подписчика"""
        if user_name is not None:
            with self.connection:
                return self.cursor.execute("INSERT INTO `subscriptions` (`user_name`, `status`) VALUES(?,?)",
                                           (user_name, status))
        else:
            print("User name is null")

    def update_subscription(self, user_name, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_name` = ?",
                                       (status, user_name))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
