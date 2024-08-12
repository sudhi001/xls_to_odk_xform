from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
import os
from fastapi.templating import Jinja2Templates
from src.impl.file.local_file_handler import LocalFileHandler
from src.impl.xls.pyform_xls_converter import PyxformXLSConverter
from src.impl.xls.xform_service import XFormConversionService

# Initialize the FastAPI application
app = FastAPI()

# Dependency Injection: Initialize the file handler, converter, and conversion service
file_handler = LocalFileHandler()
converter = PyxformXLSConverter()
conversion_service = XFormConversionService(file_handler, converter)

@app.post("/xls/to/xform")
async def xls_to_xform_xml(file: UploadFile = File(...)):
    """
    Convert an uploaded XLS file to an XForm XML format.

    This endpoint allows users to upload an XLS file, which is then processed and converted
    to the XForm XML format using the XFormConversionService. The converted XML file is 
    returned as a downloadable response.

    Args:
        file (UploadFile): The XLS file uploaded by the user.

    Returns:
        FileResponse: The converted XForm XML file as a downloadable response.
    """
    # Handle the upload and conversion process, returning the file path of the converted file
    file_path = await conversion_service.handle_upload_and_conversion(file)
    return FileResponse(file_path, filename=os.path.basename(file_path))

# Initialize the Jinja2 template engine with the specified directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serve the root HTML page.

    This endpoint renders and returns the main HTML page of the application. The page is 
    rendered using the Jinja2 template engine and can be customized to display dynamic content.

    Args:
        request (Request): The HTTP request object.

    Returns:
        HTMLResponse: The rendered HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})
