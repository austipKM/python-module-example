"""This file defines a template factory that returns a desired template


    functions:
        template_factory: Returns template specified by argument template_type

    classes:
        TemplateType: This is an enum that defines valid arguments for template_factory
"""

from .template1 import Template1
from .template2 import Template2
from .base_template import BaseTemplate
from enum import Enum


class TemplateType(Enum):
    TEMPLATE_1 = 'template1'
    TEMPLATE_2 = 'template2'


def template_factory(template_type: TemplateType) -> BaseTemplate:
    """Returns an instance of the specified template_type

    Args:
        template_type (TemplateType): string that represents the template type

    Raises:
        ValueError: Invalid template type was passed

    Returns:
        _type_: ModuleType, which represents a module/python script
    """

    if template_type == TemplateType.TEMPLATE_1.value:
        return Template1()
    elif template_type == TemplateType.TEMPLATE_2.value:
        return Template2()
    else:
        raise ValueError(
            f'Unknown template type. Valid template types are: {", ".join([t.value for t in TemplateType])}')
