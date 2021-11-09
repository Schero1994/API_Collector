from abc import ABC, abstractmethod

class Base(ABC):
    """
    Abstract Class for the different APIs with all necessary methods
    """

    @abstractmethod
    def call_api(url):
        """
        Requesting the API Endpoint
        """
        pass

    @abstractmethod
    def _authentication(self):
        """
        Authentication for the API Access
        """
        pass

    @abstractmethod
    def _check_authentication(self):
        """
        Check if the authentication is succesful
        """
        pass

    @abstractmethod
    def _check_limit(self):
        """
        Overviews the rate limit and waits if needed
        """
        pass
    
    @abstractmethod
    def _pagination(self):
        """
        Handles pagination from API Endpoints who distribute their data across multiple pages
        """
        pass
