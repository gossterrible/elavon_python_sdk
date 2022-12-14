# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class QuizQuestionChoice(object):

    """Implementation of the 'QuizQuestionChoice' model.

    TODO: type model description here.

    Attributes:
        answer_number (int): Question answer number
        answer_text (string): Answer text

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "answer_number": 'answerNumber',
        "answer_text": 'answerText'
    }

    _optionals = [
        'answer_number',
        'answer_text',
    ]

    def __init__(self,
                 answer_number=APIHelper.SKIP,
                 answer_text=APIHelper.SKIP):
        """Constructor for the QuizQuestionChoice class"""

        # Initialize members of the class
        if answer_number is not APIHelper.SKIP:
            self.answer_number = answer_number 
        if answer_text is not APIHelper.SKIP:
            self.answer_text = answer_text 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        answer_number = dictionary.get("answerNumber") if dictionary.get("answerNumber") else APIHelper.SKIP
        answer_text = dictionary.get("answerText") if dictionary.get("answerText") else APIHelper.SKIP
        # Return an object of this model
        return cls(answer_number,
                   answer_text)
