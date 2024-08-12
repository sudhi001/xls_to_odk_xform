import os
import ntpath
import tempfile
import pyxform.xls2json as xls2json
import pyxform.builder as builder
from src.xls_converter import XLSConverter

class PyxformXLSConverter(XLSConverter):
    """
    A concrete implementation of the XLSConverter abstract base class for converting XLS forms to XForm XML format.

    This class uses the Pyxform library to parse an XLS file into a JSON structure and then converts it into an
    XForm XML file. The converted file is saved temporarily and the path to the XML file is returned.

    Methods:
        convert_to_xform(file_location: str) -> str: Converts an XLS file to XForm XML format and returns the file path.
    """

    def convert_to_xform(self, file_location: str) -> str:
        """
        Convert an XLS file to an XForm XML file.

        This method takes the file path of an XLS file, parses it into a JSON structure using the Pyxform library, 
        and then converts it into an XForm XML file. The resulting XML file is saved in a temporary directory and 
        the path to the XML file is returned.

        Args:
            file_location (str): The file path of the XLS file to be converted.

        Returns:
            str: The file path of the converted XForm XML file.
        """
        warnings = []
        
        # Parse the XLS file into a JSON survey structure
        json_survey = xls2json.parse_file_to_json(file_location, warnings=warnings)
        
        # Create a survey element from the JSON structure
        survey = builder.create_survey_element_from_dict(json_survey)
        
        # Create a temporary directory to save the XForm XML file
        temp_dir = tempfile.mkdtemp()
        
        # Extract the base name of the file without the extension
        file_name = ntpath.basename(file_location).split('.')[0]
        
        # Define the path where the XML file will be saved
        file_path = os.path.join(temp_dir, f"{file_name}.xml")
        
        # Print the survey as an XForm XML file and save it to the specified path
        survey.print_xform_to_file(file_path, warnings=warnings, pretty_print=True)
        
        return file_path
