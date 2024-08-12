from fastapi import FastAPI, File, UploadFile, HTTPException
import os
from src.file_handler import FileHandler
from src.xls_converter import XLSConverter

class XFormConversionService:
    """
    A service class responsible for handling the upload and conversion of XLS files to XForm XML format.

    This class manages the file upload process, invokes the conversion from XLS to XForm XML format,
    and ensures cleanup of temporary files. It relies on injected dependencies for file handling
    and conversion functionality.

    Attributes:
        file_handler (FileHandler): An instance of a FileHandler for managing file operations.
        converter (XLSConverter): An instance of an XLSConverter for converting XLS files to XForm XML.
        upload_dir (str): The directory where uploaded files will be temporarily stored.

    Methods:
        ensure_upload_dir(): Ensures that the upload directory exists, creating it if necessary.
        handle_upload_and_conversion(file: UploadFile) -> str: Handles the file upload and conversion process.
    """

    def __init__(self, file_handler: FileHandler, converter: XLSConverter, upload_dir: str = "./uploads"):
        """
        Initialize the XFormConversionService with a file handler, converter, and optional upload directory.

        Args:
            file_handler (FileHandler): The file handler responsible for saving and cleaning up files.
            converter (XLSConverter): The converter responsible for converting XLS files to XForm XML format.
            upload_dir (str): The directory where uploaded files will be stored temporarily. Defaults to './uploads'.
        """
        self.file_handler = file_handler
        self.converter = converter
        self.upload_dir = upload_dir
        self.ensure_upload_dir()
    
    def ensure_upload_dir(self):
        """
        Ensure that the upload directory exists.

        This method checks if the specified upload directory exists, and if not, creates it.
        This is necessary to prevent errors when trying to save uploaded files.

        Returns:
            None
        """
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    async def handle_upload_and_conversion(self, file: UploadFile) -> str:
        """
        Handle the upload and conversion of an XLS file to XForm XML format.

        This method saves the uploaded file to a temporary location, converts it to XForm XML format,
        and then cleans up the temporary file. If the conversion fails, an HTTPException is raised.

        Args:
            file (UploadFile): The XLS file uploaded by the user.

        Returns:
            str: The file path of the converted XForm XML file.

        Raises:
            HTTPException: If the conversion process fails, a 500 status code HTTPException is raised.
        """
        file_location = os.path.join(self.upload_dir, file.filename)
        await self.file_handler.save_file(file, file_location)
        
        try:
            return self.converter.convert_to_xform(file_location)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to convert XLS to XForm: {str(e)}")
        finally:
            self.file_handler.clean_up_file(file_location)
