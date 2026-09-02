import time
from datetime import date
from .exceptions import APIException
from ._api_response_object import object_helper, collections
from .run import Run
from .variableset import VariableSet
from .workspace import Workspace

class Varset(object):
    """ Varset class instanlated with api response attributes for varsets. """
    def __init__(self, varset, organization_name, api_handler):
        self._api_handler      = api_handler
        self.id                = varset.id
        self.organization_name = organization_name
        self.relationships     = varset.relationships
        #self.organization_name = relationships.id
        self.attributes        = varset.attributes
        self.name              = varset.attributes.name


    def __str__(self):
        return str(self.__dict__)

    # IMPLEMENT HERE THE CODE TO SHOW THE VARIABLES OF THE VARIABLE SET.
    # Create a class for handling variables with an update and delete method included instead of using varset class
    def list_set_variables(self):
        """ Returns list of variable objects for workspace for modification. """
        variables = []
        params = {"page[size]": 100, "page[number]": 1}
        while True:
            response = self._api_handler.call(uri=f'varsets/{self.id}/relationships/vars', params=params).data
            if not response:
                break
            for variableset in response:
                variables.append(
                    VariableSet(object_helper(variableset), self._api_handler))
            params["page[number]"] += 1
        return variables


    def remove_variable_from_set(self, variable_set_id):
        """ delete variable from variable set. """
        return self._api_handler.call(uri=f'varsets/{self.id}/relationships/vars/{variable_set_id}', method='delete')
        ## Debug
        # print ('variable_set_id: ', variable_set_id)
        # return True


    def add_variable_to_set(self, variable_to_move, value_to_move):
        today = date.today()
        today_str = today.strftime("%Y/%m/%d")
        """ add variable to variable set. """
        payload = {
            "data": {
                "type": "vars",
                "attributes": {
                    "key": variable_to_move,
                    "value": value_to_move,
                    "description": "Adding by python script " + today_str,
                    "category": "terraform",
                    "hcl": False,
                    "sensitive": False
                },
                "relationships": {
                    "vars": {
                        "data": {
                            "id": self.id,
                            "type": "vars"
                        }
                    }
                }
            }
        }
        return self._api_handler.call(uri=f'varsets/{self.id}/relationships/vars', method='post', json=payload)
        ## Debug
        # print ('variable_to_move: ', variable_to_move)
        # print ('value_to_move: ', value_to_move)
        # return True


    def add_variable_to_set_ext(self, variable_to_move, value_to_move, the_desc, the_category, the_hcl, the_sensitive):
        today = date.today()
        today_str = today.strftime("%Y/%m/%d")
        """ add variable to variable set. """
        payload = {
            "data": {
                "type": "vars",
                "attributes": {
                    "key": variable_to_move,
                    "value": value_to_move,
                    "description": the_desc,
                    "category": the_category,
                    "hcl": the_hcl,
                    "sensitive": the_sensitive
                },
                "relationships": {
                    "vars": {
                        "data": {
                            "id": self.id,
                            "type": "vars"
                        }
                    }
                }
            }
        }
        return self._api_handler.call(uri=f'varsets/{self.id}/relationships/vars', method='post', json=payload)


    def list_ws(self):
        """
        Devuelve la lista de IDs de workspaces asociados a este varset.
        La información ya viene en 'relationships.workspaces' del JSON del varset.
        """
        try:
            # data puede ser una lista de dicts o de objetos, según object_helper
            ws_data_list = self.relationships.workspaces.data
            workspaces_ids = []

            for ws in ws_data_list:
                # si es dict
                if isinstance(ws, dict):
                    workspaces_ids.append(ws["id"])
                # si es objeto
                elif hasattr(ws, "id"):
                    workspaces_ids.append(ws.id)

            return workspaces_ids

        except AttributeError:
            # si relationships o workspaces no existen
            return []


    def list_pr(self):
        """
        Devuelve la lista de IDs de projects asociados a este varset.
        La información ya viene en 'relationships.workspaces' del JSON del varset.
        """
        try:
            # data puede ser una lista de dicts o de objetos, según object_helper
            pr_data_list = self.relationships.projects.data
            projects_ids = []

            for pr in pr_data_list:
                # si es dict
                if isinstance(pr, dict):
                    projects_ids.append(pr["id"])
                # si es objeto
                elif hasattr(pr, "id"):
                    projects_ids.append(pr.id)

            return projects_ids

        except AttributeError:
            # si relationships o workspaces no existen
            return []
