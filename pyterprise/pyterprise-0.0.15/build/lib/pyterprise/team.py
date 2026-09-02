# team.py
from ._api_response_object import object_helper

class Team(object):
    """ Team class instantiated with API response attributes for teams. """

    def __init__(self, team, organization_name, api_handler):
        """
        `team` debe ser el resultado de object_helper(item) donde `item` es
        cada entrada del array `data` de la API (que tiene `id`, `type`, `attributes`).
        OJO: el `id` está a nivel superior, no en attributes.
        """
        self._api_handler = api_handler
        self.organization_name = organization_name

        # Guardamos el id ANTES de entrar a attributes
        self.id = getattr(team, "id", None)

        # Luego nos movemos a attributes para el resto
        attrs = getattr(team, "attributes", team)

        # Campos comunes del recurso "teams"
        self.name = getattr(attrs, "name", None)
        self.visibility = getattr(attrs, "visibility", None)  # "secret" | "organization"
        self.users_count = getattr(attrs, "users_count", getattr(attrs, "users-count", None))
        self.sso_team_id = getattr(attrs, "sso_team_id", getattr(attrs, "sso-team-id", None))
        self.permissions = getattr(attrs, "permissions", None)
        self.organization_access = getattr(attrs, "organization_access", getattr(attrs, "organization-access", None))
        self.allow_member_token_management = getattr(
            attrs, "allow_member_token_management", getattr(attrs, "allow-member-token-management", None)
        )

    def __str__(self):
        return f"Team(name={self.name}, id={self.id}, visibility={self.visibility})"

    def to_dict(self):
        return {
            "id": self.id,
            "organization": self.organization_name,
            "name": self.name,
            "visibility": self.visibility,
            "users_count": self.users_count,
            "sso_team_id": self.sso_team_id,
            "permissions": self.permissions,
            "organization_access": self.organization_access,
            "allow_member_token_management": self.allow_member_token_management,
        }

    # ------------------------
    # Operaciones
    # ------------------------

    def refresh(self, include_users=False):
        """Refresca los atributos desde la API. Use `include_users=True` para incluir usuarios."""
        if not self.id:
            raise ValueError("Team sin id: no se puede refrescar.")
        params = {}
        if include_users:
            params["include"] = "users"
        resp = self._api_handler.call(uri=f"teams/{self.id}", params=params)
        t = object_helper(resp.data)

        # Reasignar atributos como en __init__
        self.id = getattr(t, "id", self.id)
        attrs = getattr(t, "attributes", t)
        self.name = getattr(attrs, "name", self.name)
        self.visibility = getattr(attrs, "visibility", self.visibility)
        self.users_count = getattr(attrs, "users_count", getattr(attrs, "users-count", self.users_count))
        self.sso_team_id = getattr(attrs, "sso_team_id", getattr(attrs, "sso-team-id", self.sso_team_id))
        self.permissions = getattr(attrs, "permissions", self.permissions)
        self.organization_access = getattr(attrs, "organization_access", getattr(attrs, "organization-access", self.organization_access))
        self.allow_member_token_management = getattr(
            attrs, "allow_member_token_management",
            getattr(attrs, "allow-member-token-management", self.allow_member_token_management)
        )
        # Si pediste include users, podés leer `resp.included` si tu api_handler lo expone
        return self

    def update(self, new_name=None, new_visibility=None, organization_access=None,
               allow_member_token_management=None, sso_team_id=None):
        """PATCH /teams/:team_id — actualiza atributos del team."""
        if not self.id:
            raise ValueError("Team sin id: no se puede actualizar.")

        attrs = {}
        if new_name is not None:
            attrs["name"] = new_name
        if new_visibility is not None:
            attrs["visibility"] = new_visibility  # "secret" | "organization"
        if organization_access is not None:
            # dict con claves de org-access (manage-workspaces, read-workspaces, etc.)
            attrs["organization-access"] = organization_access
        if allow_member_token_management is not None:
            attrs["allow-member-token-management"] = bool(allow_member_token_management)
        if sso_team_id is not None:
            attrs["sso-team-id"] = sso_team_id

        payload = {"data": {"type": "teams", "id": self.id, "attributes": attrs}}
        resp = self._api_handler.call(uri=f"teams/{self.id}", method="patch", json=payload).data
        # Actualizamos estado local con lo devuelto
        updated = object_helper(resp)
        self.id = getattr(updated, "id", self.id)
        a = getattr(updated, "attributes", updated)
        self.name = getattr(a, "name", self.name)
        self.visibility = getattr(a, "visibility", self.visibility)
        self.organization_access = getattr(a, "organization_access", getattr(a, "organization-access", self.organization_access))
        self.allow_member_token_management = getattr(
            a, "allow_member_token_management", getattr(a, "allow-member-token-management", self.allow_member_token_management)
        )
        self.sso_team_id = getattr(a, "sso_team_id", getattr(a, "sso-team-id", self.sso_team_id))
        self.users_count = getattr(a, "users_count", getattr(a, "users-count", self.users_count))
        self.permissions = getattr(a, "permissions", self.permissions)
        return self

    # ------------------------
    # Miembros del team
    # ------------------------

    def add_user_ids(self, user_ids):
        """
        Agrega uno o varios usuarios por `user_id`.
        POST /teams/:team_id/relationships/users
        """
        if isinstance(user_ids, str):
            user_ids = [user_ids]
        payload = {"data": [{"type": "users", "id": uid} for uid in user_ids]}
        return self._api_handler.call(
            uri=f"teams/{self.id}/relationships/users", method="post", json=payload
        ).data

    def add_org_membership_ids(self, membership_ids):
        """
        Agrega usuarios por `organization_membership_id`.
        POST /teams/:team_id/relationships/organization-memberships
        """
        if isinstance(membership_ids, str):
            membership_ids = [membership_ids]
        payload = {"data": [{"type": "organization-memberships", "id": mid} for mid in membership_ids]}
        return self._api_handler.call(
            uri=f"teams/{self.id}/relationships/organization-memberships", method="post", json=payload
        ).data

    def remove_user_ids(self, user_ids):
        """DELETE /teams/:team_id/relationships/users"""
        if isinstance(user_ids, str):
            user_ids = [user_ids]
        payload = {"data": [{"type": "users", "id": uid} for uid in user_ids]}
        return self._api_handler.call(
            uri=f"teams/{self.id}/relationships/users", method="delete", json=payload
        )

    def remove_org_membership_ids(self, membership_ids):
        """DELETE /teams/:team_id/relationships/organization-memberships"""
        if isinstance(membership_ids, str):
            membership_ids = [membership_ids]
        payload = {"data": [{"type": "organization-memberships", "id": mid} for mid in membership_ids]}
        return self._api_handler.call(
            uri=f"teams/{self.id}/relationships/organization-memberships", method="delete", json=payload
        )

    def list_user_ids(self):
        """
        Devuelve solo IDs de users (identificadores).
        GET /teams/:team_id/relationships/users
        """
        members = []
        params = {"page[size]": 100, "page[number]": 1}
        while True:
            resp = self._api_handler.call(uri=f"teams/{self.id}/relationships/users", params=params)
            if not resp.data:
                break
            for u in resp.data:
                # u es un resource identifier { "type": "users", "id": "..." }
                ou = object_helper(u)
                members.append(getattr(ou, "id", None))
            params["page[number]"] += 1
        return members

    def list_users(self):
        """
        Devuelve objetos de usuario completos usando include=users.
        GET /teams/:team_id?include=users
        """
        resp = self._api_handler.call(uri=f"teams/{self.id}", params={"include": "users"})
        users = []
        # api_handler típico expone `included` con los recursos incluidos
        included = getattr(resp, "included", []) or []
        for inc in included:
            inc = object_helper(inc)
            if getattr(inc, "type", None) == "users" or getattr(inc, "type", None) == "user":
                users.append(inc)  # queda como object_helper para consistencia con tu lib
        return users
