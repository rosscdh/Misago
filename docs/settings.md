Settings reference
==================

In Misago there are two types of settings: static settings that are initialized on Misago startup and don't change afterwards, and dynamic settings that are stored in database and can be changed from admin control panel.


Static settings
---------------

Static settings values are accessible throught the attributes of `misago.conf.settings` object:

- `debug: bool` - Switch controlling if `debug` mode is enabled.
- `test: bool` - Switch specifying if application is running within test runner (pytest).
- `test_database_name: Optional[str]` - If specified, makes tests run against different database.
- `database_url: str` - Database connection URL as used by [`Databases` library](https://www.encode.io/databases/database_queries/).
- `cache_url: str` - Cache connection URL as used by [`async-caches` library](https://rafalp.github.io/async-caches/backends/).
- `static_root: str` - Absolute path to directory from which static files are served by the HTTP server.
- `media_root: str` - Absolute path to directory from which uploaded files are served by the HTTP server.
- `enabled_plugins: Optional[str]` - Absolute path to text file with a list of enabled plugins.


Dynamic settings
----------------

- `forum_name: str` - Forum name.