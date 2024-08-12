from abc import ABC, abstractmethod

class XLSConverter(ABC):
    """
    An abstract base class that defines the interface for converting XLS files to XForm XML format.

    This class provides an interface for converting an XLS file to an XForm XML file. Subclasses 
    that inherit from this class must implement the `convert_to_xform` method, which handles 
    the conversion process.

    Methods:
        convert_to_xform(file_location: str) -> str: Converts an XLS file at the given location to an XForm XML file.
    """

    @abstractmethod
    def convert_to_xform(self, file_location: str) -> str:
        """
        Convert an XLS file to an XForm XML file.

        This method must be implemented by any subclass to define the logic for converting
        an XLS file to XForm XML format. The method should return the file path of the
        converted XML file.

        Args:
            file_location (str): The file path of the XLS file to be converted.

        Returns:
            str: The file path of the converted XForm XML file.
        """
        pass
