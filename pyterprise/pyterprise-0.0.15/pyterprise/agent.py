from ._api_response_object import object_helper

class Agent(object):

    def __init__(self, agent, api_handler):
        self._api_handler = api_handler
        self.id = agent.id
        attr = agent.attributes
        self.name = attr.name
        self.status = attr.status


    def __str__(self):
        return str(self.__dict__)

    def show(self):
            """Reloads and returns the Agent object from the API"""
            response = self._api_handler.call(uri=f"agents/{self.id}")
            return Agent(agent=object_helper(response.data), api_handler=self._api_handler)

    def delete(self):
        """Deletes the agent"""
        return self._api_handler.call(method="delete", uri=f"agents/{self.id}")
