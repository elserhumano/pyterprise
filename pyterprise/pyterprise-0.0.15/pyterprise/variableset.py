class VariableSet(object):

    def __init__(self, variable, api_handler):
        self._api_handler = api_handler

        self.id          = variable.id
        attributes       = variable.attributes
        self.key         = attributes.key
        self.value       = attributes.value
        self.category    = attributes.category
        self.hcl         = attributes.hcl
        self.sensitive   = attributes.sensitive
        self.description = attributes.description

    def __str__(self):
        return str(self.__dict__)
