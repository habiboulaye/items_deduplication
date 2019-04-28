Simple Guide for Items Deduplication
================================

GetStart with a short overview
-----------------------------
The items deduplication is an important challenge  in marketplace. It helps improving customer experience, avoiding fraud, .... However, the deduplication algorithms are facing to many challenges causing confusions and poor performance for practical usage (false alarms, non-detection). 
Main challenges are related to the image context variances (position, luminosity, environment, ...)

A rapid review of the state of the art tools and research papers shows the use of several approaches for items deduplication. We can highlight the hashing-based techniques that aims to create an image fingerprint and more modern deep neural networks techniques that extract deep features by creating an embedding space for context-free representation ... Afterward, downstream of their representations, duplicated items are detected using a suitable similarity measure or a nearest neighbour method.

In this short-term task, we propose an algorithm v0.1 for image deduplication (package algo_deduplicate) using deep learning models. Deep neural architectures have good capabilities to be robust to context variations and to capture hidden patterns and correlations.
In summary, our algorithm is build in 3 main stages (cf. class Duplicate in iduplicate file):
* Selection of a pre-trained deep learning model from large image dataset (eg. ResNet on imagenet). Skip the top layers (fc) to get a model for deep features extraction thanks to transfer leaning. 
    * We use this deep learning pre-trained model to instanciate the class Duplicate
* Pre-processing and representation: This stage is use to build a good representation of the images in a suitable features space (a key success factor).
    * Image preparation (cf. method Duplicate.prepare): this stage applies all the image transformations need to create a suitable input for deep features extraction in good conditions. resizing, normalisation, ... An optional image augmentation (bluring, rotation, ...) can help to increase the algorithm performance.
    * Deep features extraction (cf. method Duplicate.represent): Get a good representation of the image in an embedding features space.  
* Duplication detection (cf. method Duplicate.duplication_check). This method takes two images and compares how much they are similar using a similarity scoring method (eg. cosim). A threshold is tuned to have a good balance between false alerts and true positive rates.

#### Improvement perspectives:
* Study the capabilities and limitations of hashing techniques, and other methods like visual vocabulary and tfidf for visual features ...
* Compare ResNet with some other deep learning pre-trained models (eg. VGG, AlexNet, ...). Combine them with the method Locality Sensitive Hashing to detect duplication.
* Regarding deep learning architectures, the autoencoders (and ) setting seems more suitable to learn good representation for deduplication purpose. 
    * In fact, autoencoders are designed to learn "identity-function-like" with free context whereas pre-trained networks are usually trained for classification purposes.
    * However, transfer learning takes advantage of large databases, and is more easy/simple to use compare to the training of new deep learning models from scratch.
* Depending to the availability of labelled data, the model could be improve with additional training with specialisation/personalisation (eg. locatisation, region, ...)

(TODO: The description above could be more elaborated and moved in the sphinx documentation docs/build/html: Description of the methodology)

Using algo_deduplicate - Entry points
-------------------------------------
### Dependencies
    + python (3.6)
    + tensorflow (1.12)
    + keras (2.2.4)
    
    
### Run 
1. Go to the project directory:
PRJ_PATH=/path/to/items_deduplication/
cd PRJ_PATH

2. Put the input images folders in PRJ_PATH/images/:
- new_images_dir (eg. duplicate_ads)
- ref_images_dir (eg. non_duplicate_ads)

3. run algo_deduplicate using the command:

```bash
    python run_deduplication.py PRJ_PATH/images/new_images_dir PRJ_PATH/images/ref_images_dir --thres=85
```
  
- thres (from 0 to 100: default:95) is the  threshold on similary to detect duplicate 
        Test with provided data: thres = 85 (similar objects) vs. 95 (only duplicated objects)
- thres is optional, to use the default value, run just:

- Pairs of duplicated items name are printed in console. Other option: add an output_file argument to store the results


```bash
    python run_deduplication.py PRJ_PATH/images/new_images_dir PRJ_PATH/images/ref_images_dir
```


### Testing

Run unittests

```bash
    iduplicate_tests.py
```

- Feel free to add more unittest cases for more checking

Documentation (API To be completed)
-------------
The documentation is generated using sphinx.
cd PRJ_PATH/docs/

```bash
    make html
```

see index.html PRJ_PATH/docs/build/html

Integration - Deploy (To be completed)
-------------------

algo_deduplication will require Python 3.5 or newer.

#### Source code on git (TBD)

You can check the latest sources with the command::

```bash
    git clone git@<ip>:REPO/algo_deduplication.git
```

#### User installation (not required)

Use `pip` from the root directory to install the package algo_deduplication
```bash 
    pip install .
```

#### Deploy using docker (To Be Define)

For better isolation and easy transfer (without os/packages dependencies) for example in pre-production stage (validation).


#### Changelog

To be Done


#### Contact
email: habiboulaye@gmail.com

