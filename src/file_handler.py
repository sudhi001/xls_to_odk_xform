from fastapi import UploadFile
from abc import ABC, abstractmethod

class FileHandler(ABC):
    """
    An abstract base class that defines the interface for handling file operations.

    This class provides an interface for saving and cleaning up files, intended to be
    implemented by concrete subclasses. The methods are defined as asynchronous or
    synchronous as required by the use case.

    Methods:
        save_file(file: UploadFile, destination: str): Asynchronously saves an uploaded file to a specified destination.
        clean_up_file(file_path: str): Cleans up (deletes) a file from the filesystem.
    """

    @abstractmethod
    async def save_file(self, file: UploadFile, destination: str):
        """
        Save an uploaded file to the specified destination asynchronously.

        This method must be implemented by any subclass to define the logic for saving an
        uploaded file to the desired location.

        Args:
            file (UploadFile): The uploaded file object to be saved.
            destination (str): The file path where the uploaded file should be saved.

        Returns:
            None
        """
        pass
    
    @abstractmethod
    def clean_up_file(self, file_path: str):
        """
        Clean up (delete) a file from the filesystem.

        This method must be implemented by any subclass to define the logic for deleting
        a file from the filesystem.

        Args:
            file_path (str): The file path of the file to be deleted.

        Returns:
            None
        """
        pass
