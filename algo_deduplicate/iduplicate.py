import numpy as np
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50, preprocess_input

model_default = ResNet50(weights='imagenet', include_top=False, pooling='avg')

class Duplicate(object):
    def __init__(self, model = model_default):
        """
            Instanciation: using a ResNet50 pretrained model by default (test with other if need)
        """

        self.model_feature_extractor = model

    def prepare(self, img_path):
        """
        Preprocessing: load , resize ...etc

        :param img_path:
        :return: preprocessed data, ready for model.predict
        """

        # load image and resize to 224 x 224
        img = image.load_img(img_path, target_size=(224, 224))
        # image to numpy array
        x = image.img_to_array(img)
        # the image is now in an array of shape (3, 224, 224)
        # expand from (3, 224, 224) to (1, 3, 224, 224) to have
        x = np.expand_dims(x, axis=0)
        # preprocess_input to subtract the mean RGB channels of the imagenet dataset because pre-trained model (like normalisation)
        x = preprocess_input(x)  # images = np.vstack(images)
        return x

    def image_augmentation(self, img):
        """
        Apply some image augmentation methods (Blur, Rotate, Symetric) to increase robustness

        :param img: input image
        :return: list of augmented images
        """

        pass

    def represent(self, x_image):
        """
        Build the representation using deep features in an embeddings space from pre-trained nnets

        :param x_image: input image
        :return: deep features
        """
        return self.model_feature_extractor.predict(x_image)[0]

    def cosinus_similarity_score(self, x1, x2):
        """
        Similarity measure betwen 2 vectors (cosinus is used here)
                    # Next - Go beyond with: Locality Sensitive Hashing, T-SNE, ...

        :param x1: vector 1, list of float value
        :param x2: vector 2, list of float value
        :return: cosinus similarity score
        """

        cos_sim = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))
        return cos_sim

    def duplication_check(self, img1_path, img2_path, sim_threshold=95):
        """
        Check if the 2 input images are the same

        :param img1_path: image of item 1
        :param img2_path: image of item 2
        :param sim_threshold: similarity threshold to detect duplicate
        :return: True or False
        """

        # represent image 1
        x1 = self.prepare(img1_path)
        x1_features = self.represent(x1)
        # represent image 2
        x2 = self.prepare(img2_path)
        x2_features = self.represent(x2)
        # ===> compute cosim
        sim_score = 100*self.cosinus_similarity_score(x1_features, x2_features)
        if sim_score > sim_threshold:
            print("===> Detect Duplicated items with score:{} >= {}".format(sim_score, sim_threshold))
            return True
        return False