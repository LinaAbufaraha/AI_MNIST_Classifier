#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Lina Abufarha
# DATE CREATED: 3/13/2025                                 
# REVISED DATE: 3/13/2025 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    # Creates list of files in directory
    filename_list = listdir(image_dir)

    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for filename in filename_list:

      # Skips hidden files starting with .
      # isn't an pet image file
      if filename[0] != ".":  
            # Sets pet_image variable to filename 
            pet_image = filename.lower()

            # Splits lower case string by _ to break into words 
            word_list_pet_image = pet_image.split("_")

            # Create pet_name starting as empty string
            pet_name = ""

            # Loops to check if word in pet name is only alphabetic characters
            # and appends word to pet_name separated by trailing space 
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "

            # Strip off starting/trailing whitespace characters 
            pet_name = pet_name.strip()

            # Adds filename and pet_name to results_dic
            if filename not in results_dic:
                results_dic[filename] = [pet_name]
            else:
                print(f"** Warning: Duplicate file detected: {filename}")         


    return results_dic
