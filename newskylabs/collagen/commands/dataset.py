"""newskylabs/collagen/commands/dataset.py:

Generate a dataset conformimg to the given dataset specification.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2018 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2018/08/02"

import os, sys
from pathlib import Path
import numpy as np

from newskylabs.collagen.utils.yaml import load_yaml_file
from newskylabs.collagen.generators.digit_generator import DigitGenerator

## =========================================================
## class DatasetGenerator
## ---------------------------------------------------------

class DatasetGenerator:

    def __init__(self, file):
        self._file = file
        self._load_dataset_specification()

    def _load_dataset_specification(self):
        """
        Load the dataset specification file
        """

        # Load the data set specification
        spec = load_yaml_file(self._file)
        self._spec = spec

        # Get the debug flag
        key = 'debug'
        self._debug = ((key in spec) and spec[key] == True)

        # Get the directory from the dataset specification
        self._dataset_spec = spec['dataset']
        self._dataset = spec['dataset']['name']
        self._class_to_label = spec['dataset']['classes']
        self._subsets_spec = spec['subsets']

        # Calculate the inverse dictionary of self._class_to_label
        self._label_to_class = {}
        for class_, label in self._class_to_label.items():
            self._label_to_class[label] = class_

        # Get base dir
        base_dir = spec['dir']
        base_dir = Path(base_dir)
        base_dir = base_dir.expanduser() # Expand ~ if given
        self._base_dir = base_dir

        # Get scale
        key = 'scale'
        if key in spec:
            scale = spec[key]
        else:
            # default scale is 1
            scale = 1 
        self._scale = scale

        # Init the digit generator
        self._digit_gen = DigitGenerator()
    
        # Init the augmentation pipeline
        augmentation_pipeline_spec = self._load_augmentation_pipeline_specification()
        self._digit_gen.init_augmentation_pipeline(augmentation_pipeline_spec)


    def _load_augmentation_pipeline_specification(self):
        """
        Load the augmentation pipeline from the dataset specification
        and return it.
        """
        # TODO 
        # 
        # Define some subclass of dic which
        # - allowes to access the data with paths like "some.spec.path"
        # - allowes to check for features which have to be defined
        # - allowes to define default value
        # 
        # Using this:
        # - check for all necessary dataset features:
        # - define defaults for all features where this makes sense
        # 
        # See for example: $COLLAGEN/examples/datasets/half-and-quarter-notes000.yaml
        # 
        # dataset: 
        #   name: notes000
        #   classes:
        #     half: 1
        #     quarter: 2
        # 
        # subsets:
        #   train: 10
        #   valid:  4
        #   test:   4
        # 
        # dir: ~/.collagen/data/notes
        # 
        # augmentation-pipeline:
        # 
        #   - mirror:
        #       probability: 0.5
        #       direction: y
        # 
        #   - rotate:
        #       probability: 0.5
        #       angle: 90

        spec = self._spec
        
        # Ensure that augmentation pipeline is defined
        key = 'augmentation-pipeline'
        if not key in spec:
            msg = "\nWARNING No augmentation pipeline defined: {}!\n".format(spec)
            print("\n{}".format(msg), file=sys.stderr)

        # Get augmentation pipeline definition
        pipeline_spec = spec[key]

        # When no operation has been given use an empty list
        if pipeline_spec == None:
            pipeline_spec = []
    
        # Return it
        return pipeline_spec

    def _load_subset(self, subset):
        """
        Load the SUBSET of the actual dataset.
        """

        dataset = self._dataset
        self._digit_gen.load_dataset(dataset, subset=subset)

    def get_labels(self):
        """
        Get list of all defined labels.
        """
        return list(self._label_to_class.keys())

    def get_classes(self):
        """
        Get list of all defined classes.
        """
        return list(self._class_to_label.keys())

    def number_of_classes(self):
        """
        Get the number of classes.
        """
        return len(self.get_classes())

    def get_label(self, class_):
        """
        Get the numerical label for the given class.
        """
        return self._class_to_label[class_]

    def get_class(self, label):
        """
        Get the class name corresponding to the given label.
        """
        return self._label_to_class[label]

    def generate_image(self, img_path, class_):
        """
        Generate an image
        and save it under IMG_PATH.
        """

        label = self.get_label(class_)

        print("DEBUG generating image: {}  ({} : {})".format(img_path, label, class_))
        
        # Generate the image
        image = self._digit_gen.image(label, name=img_path)
   
        # And save it
        scale = self._scale
        if self._debug:
            # Show the image
            # when in debug mode
            image.save_and_show(scale=scale)
        else:
            image.save(scale=scale)

    def check_subset_numbers(self):
        """
        Ensure that the number of images per subset 
        is a multiple of the number of classes.
        """

        # Check number of images per subsets
        msg = ""
        number_of_classes = self.number_of_classes()
        for subset, number in self._subsets_spec.items():
            rest = number % number_of_classes
            if (rest != 0):
                msg += "ERROR {} (number of images for subset {}) "\
                       "is not a multiple of {} (number of classes)!\n".format(number, subset, number_of_classes)

        if msg != "":
            print("\n{}".format(msg), file=sys.stderr)
            sys.exit(-1)

    def generate_subset(self, subset, number):
        """
        Generate a subset of the dataset.
        """
        if subset[:4] == "test":
            self.generate_testset(subset, number)
        else:
            self.generate_named_subset(subset, number)

    def generate_named_subset(self, subset, number):
        """
        Generate a named subset of the dataset.
        """

        print("Generating '{}' set with {} images...".format(subset, number))

        # Load the subset of the dataset
        self._load_subset(subset)

        # Make the subset directory
        subset_directory = self._base_dir / subset
        subset_directory.mkdir(parents=True)

        images_per_class = number // self.number_of_classes()
        for class_ in self.get_classes():

            # Make the class directory
            class_directory = subset_directory / class_
            class_directory.mkdir(parents=True)

            for i in range(images_per_class):
                
                img_name = "{}.{}".format(class_, i)
                img_path = class_directory / img_name
                
                self.generate_image(img_path, class_)

    def generate_testset(self, subset, number):
        """
        Generate a testset.
        """
        
        print("Generating '{}' set with {} images...".format(subset, number))

        # Load the subset of the dataset
        self._load_subset(subset)

        # Make the subset directory
        subset_directory = self._base_dir / subset
        subset_directory.mkdir(parents=True)

        classes = self.get_classes()
        labels  = self.get_labels()

        # Generate random list of labels
        #
        # Example:
        #   labels = [3, 5], images_per_class = 3
        #   => ordered_labels:    [3, 3, 3, 5, 5, 5] 
        #   => randomized_labels: [5, 3, 5, 5, 3, 3]
        # 
        images_per_class = number // self.number_of_classes()
        ordered_labels = np.repeat(labels, images_per_class)
        randomized_labels = np.random.permutation(ordered_labels)

        # Save the randomized labels list
        # encoding the class corresponding to the test images
        randomized_labels_file = subset_directory / "labels.npy"
        np.save(randomized_labels_file, randomized_labels)

        # Generate test images
        for i in range(number):
                
            label = randomized_labels[i]
            class_ = self.get_class(label)
                
            img_name = "{}".format(i)
            img_path = subset_directory / img_name
                
            self.generate_image(img_path, class_)

    def load_testset_labels(self):
        """
        Load the testset labels and return them.
        """

        # Calculate the testset labels file
        subset = "test"
        subset_directory = self._base_dir / subset
        randomized_labels_file = subset_directory / "labels.npy"

        # Load the testset labels
        testset_labels = np.load(randomized_labels_file)

        return testset_labels

    def generate(self):
        """
        Generate the dataset
        corresponding to the given dataset specification.
        """

        # Ensure that the number of images per subset 
        # is a multiple of the number of classes
        self.check_subset_numbers()

        # Get base dir
        path = Path(self._base_dir)
        path = path.expanduser() # Expand ~ if given

        # Ensure that the base directory does not exist yet
        if self._base_dir.exists():
            msg = '\nERROR The dataset base directory already exists: {}\n'.format(self._base_dir)
            print(msg, file=sys.stderr)
            sys.exit(-1)

        # Make the base directory
        self._base_dir.mkdir(parents=True)

        # Generate subsets
        for subset, number in self._subsets_spec.items():
            self.generate_subset(subset, number)

        # Print the testset labels 
        # when in debug mode
        if self._debug:
            testset_labels = self.load_testset_labels()
            print("DEBUG testset_labels:", testset_labels)

## =========================================================
## Dataset command
## ---------------------------------------------------------

def collagen_dataset(dataset_spec):
    """Generate a dataset conformimg to the given dataset specification
    DATASET_SPEC.

    """

    # Generate the dataset
    gen = DatasetGenerator(dataset_spec)
    gen.generate()

    # done
    print("done.")

## =========================================================
## =========================================================

## fin.
