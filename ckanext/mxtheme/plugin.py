import datetime
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def format_display_date(time_stamp, format_date="%Y/%m/%d"):
    date_object = datetime.datetime.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime(format_date)


class MxthemePlugin(plugins.SingletonPlugin):
    # IConfigurer
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'mxtheme')

    def get_helpers(self):
        return {'format_display_date': format_display_date}