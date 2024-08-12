from abc import ABC, abstractmethod
import os
from src.file_handler import FileHandler
from fastapi import UploadFile
import aiofiles

class LocalFileHandler(FileHandler):
    """
    A concrete implementation of the FileHandler abstract base class for handling file operations locally.

    This class provides methods to save uploaded files to a local directory and to clean up (delete) files 
    from the local filesystem.

    Methods:
        save_file(file: UploadFile, destination: str): Asynchronously saves the uploaded file to the specified destination.
        clean_up_file(file_path: str): Deletes the specified file from the local filesystem if it exists.
    """

    async def save_file(self, file: UploadFile, destination: str):
        """
        Save an uploaded file to the specified destination asynchronously.

        This method uses aiofiles to write the contents of the uploaded file to the specified destination
        on the local filesystem. This allows the operation to be non-blocking, making it suitable for 
        use in an asynchronous web framework like FastAPI.

        Args:
            file (UploadFile): The uploaded file object.
            destination (str): The file path where the uploaded file should be saved.

        Returns:
            None
        """
        async with aiofiles.open(destination, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)

    def clean_up_file(self, file_path: str):
        """
        Delete a file from the local filesystem.

        This method checks if the specified file exists and deletes it. It is useful for cleaning up temporary
        files after they have been processed.

        Args:
            file_path (str): The file path of the file to be deleted.

        Returns:
            None
        """
        if os.path.exists(file_path):
            os.remove(file_path)
