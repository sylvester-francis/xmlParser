class IncreasePriceException(Exception):
    """Exception raised for errors during the increase price process."""
    pass

class CategoryNotFoundException(Exception):
    """Exception raised when the specified category is not found."""
    pass
class EmptyCategoryNameException(Exception):
    """Exception raised when the new category name is an empty string."""
    pass
class InvalidRatingException(Exception):
    """Exception raised when an invalid rating is provided."""
    pass
class ReportGenerationException(Exception):
    """Exception raised for errors during report generation."""
    pass
