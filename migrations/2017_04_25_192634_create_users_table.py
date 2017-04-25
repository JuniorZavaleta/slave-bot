from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name', 50)
            table.string('username', 50)
            table.big_integer('telegram_chat_id')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
