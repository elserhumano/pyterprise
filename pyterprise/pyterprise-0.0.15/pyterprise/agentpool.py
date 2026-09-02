from ._api_response_object import object_helper
from .agent import Agent

# agentpool.py
from ._api_response_object import object_helper
from .agent import Agent

class AgentPool(object):
    """Represents a Terraform Agent Pool"""

    def __init__(self, pool, api_handler):
        self._api_handler = api_handler
        self.id = pool.id
        attrs = pool.attributes
        self.name = attrs.name
        self.organization_scoped = attrs.organization_scoped

    def __str__(self):
        return str(self.__dict__)

    def list_agents(self):
        """Returns a list of Agent objects in this pool"""
        agents_list = []
        params = {"page[size]": 100, "page[number]": 1}

        while True:
            response = self._api_handler.call(
                uri=f"agent-pools/{self.id}/agents",
                params=params
            )
            if not response.data:
                break
            for agent_data in response.data:
                agents_list.append(
                    Agent(agent=object_helper(agent_data), api_handler=self._api_handler)
                )
            params["page[number]"] += 1
        return agents_list

    def show(self):
        """Reloads and returns the AgentPool object from the API"""
        response = self._api_handler.call(uri=f"agent-pools/{self.id}")
        return AgentPool(pool=object_helper(response.data), api_handler=self._api_handler)
