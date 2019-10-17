import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import logging
import pprint
log = logging.getLogger(__name__)




class BrokenafterPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.IValidators)


    def _modify_package_schema(self, schema):
        schema.update({
            '__after' : [toolkit.get_validator('study_validator')],})
        return schema

    def create_package_schema(self):
        schema = super(BrokenafterPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
        

    def update_package_schema(self):
        schema = super(BrokenafterPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
       
    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def get_validators(self):
        return {'study_validator' : study_validator }

def study_validator(key, flattened_data, error, context):
    from pprint import pformat
    log.debug("study_validator got: "+ pformat(key) + " " + pformat(flattened_data))

