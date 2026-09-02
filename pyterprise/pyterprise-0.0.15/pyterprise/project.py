from ._api_response_object import object_helper
from .workspace import Workspace

class Project(object):
    def __init__(self, project, organization_name, api_handler):
        self._api_handler = api_handler
        self.id = project.id
        self.organization_name = organization_name

        attributes = project.attributes
        self.name = attributes.name
        self.description = attributes.description
        self.created_at = attributes.created_at
        
        # Relationships (ej: lista de workspaces vinculados a este proyecto)
        self.relationships = project.relationships

        self.links = project.links

    def __str__(self):
        return str(self.__dict__)


    def list_ws(self):
        """
        Returns all workspaces that belong to this project
        by filtering the organization's workspaces.
        """
        workspaces = []
        params = {"page[size]": 100, "page[number]": 1}
        while True:
            response = self._api_handler.call(
                uri=f'organizations/{self.organization_name}/workspaces',
                params=params
            )
            if not response.data:
                break
            for ws in response.data:
                ws_obj = object_helper(ws)
                rel = getattr(ws_obj.relationships, "project", None)
                if rel and rel.data and rel.data.id == self.id:
                    workspaces.append(
                        Workspace(
                            workspace=ws_obj,
                            organization_name=self.organization_name,
                            api_handler=self._api_handler
                        )
                    )
            params["page[number]"] += 1
        return workspaces


    @classmethod
    def get_pr(cls, project_id, organization_name, api_handler):
        """
        Devuelve el objeto Project correspondiente a project_id
        recorriendo todos los proyectos disponibles.
        """
        try:
            # Llamada a la API que devuelve todos los proyectos
            response = api_handler.call("/projects")
            for p in response.data:
                if str(p.id) == str(project_id):  # comparo strings para estar seguro
                    return cls(p, organization_name, api_handler)
            # Si no encuentra ninguno
            return None
        except Exception as e:
            print(f"Error al recuperar proyecto {project_id}: {e}")
            return None
