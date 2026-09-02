class Resource:
    def __init__(self, id, type_, name, address=None, provider=None, module=None, provider_type=None):
        self.id = id
        self.type = type_
        self.name = name
        self.address = address
        self.provider = provider
        self.module = module
        self.provider_type = provider_type

    def __repr__(self):
        return f"<id={id} resource_type={self.type} name={self.name} address={self.address} provider={self.provider} module={self.module} provider_type={self.provider_type}>"
