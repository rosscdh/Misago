from typing import List

from jinja2 import ChoiceLoader, Environment, PackageLoader, select_autoescape

from ..conf import settings
from ..hooks import jinja2_extensions, jinja2_filters
from ..plugins import plugins


def get_template_loaders() -> List[PackageLoader]:
    template_loaders = [PackageLoader("misago.template", "templates")]
    for plugin in plugins.get_plugins_with_directory("templates"):
        template_loaders.append(PackageLoader(plugin.module_name, "templates"))
    return list(reversed(template_loaders))


def get_jinja2_environment() -> Environment:
    env = Environment(
        auto_reload=settings.debug,
        autoescape=select_autoescape(["html", "svg", "xml"]),
        enable_async=True,
        loader=ChoiceLoader(get_template_loaders()),
    )

    env.filters.update(jinja2_filters)
    for extension in jinja2_extensions:
        env.add_extension(extension)

    return env


env = get_jinja2_environment()