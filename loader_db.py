import config

from scripts.database.sqlite import GroupsDB, ParameterDB

groups_db = GroupsDB(config.PATH_FILE_DB + 'group_db.db')
parameter_bool_db = ParameterDB(config.PATH_FILE_DB + 'group_db.db', '`storage_bool_parm`')
parameter_str_db = ParameterDB(config.PATH_FILE_DB + 'group_db.db', '`storage_str_parm`')

