# user.py

from ._api_response_object import object_helper

class User:
    """
    Representa un usuario dentro de una organización en Terraform Enterprise.
    """

    def __init__(self, user_data, api_handler):
        """
        Inicializa el objeto User con los datos de la API.
        
        :param user_data: objeto retornado por object_helper(response.data)
        :param api_handler: instancia de api_handler de la organización
        """
        self._api_handler = api_handler
        self.id = user_data.id
        self.attributes = user_data.attributes


    def __str__(self):
        email = self.attributes.email
        status = self.attributes.status
        return f"User(id={self.id}, email={email}, status={status})"


    def __repr__(self):
        return self.__str__()


    def update(self, **kwargs):
        """
        Actualiza los atributos del usuario.
        """
        payload = {"data": {"id": self.id, "type": "users", "attributes": kwargs}}
        response = self._api_handler.call(f"users/{self.id}", method="patch", json=payload)
        self.attributes.update(object_helper(response.data).attributes)
        return self

    def delete(self):
        """
        Elimina este usuario de la organización.
        """
        return self._api_handler.call(f"users/{self.id}", method="delete")
