from os import listdir
#from PIL import Image
import os, os.path
import tensorflow as tf, sys

patharg = sys.argv[1]
#path = "E:/project/test/output/"
valid_images = [".jpg",".gif",".png",".jpeg"]

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
    in tf.gfile.GFile("E:/project/test/output_labels.txt")]
# Unpersists graph from file
with tf.gfile.GFile("E:/project/test/output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')


def score_warn(a):
            categ = label_lines[a]
            if categ == 'road' or categ == 'sky':
                print('\nSAFE TO MOVE')
            else:
                print('\nWARNING TO USER')


def test_image(image_path,img_name):
    # Read in the image_data
    image_data = tf.gfile.GFile(image_path, 'rb').read()
    
    # Feed the image_data as input to the graph and get first prediction
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, 
         {'DecodeJpeg/contents:0': image_data})        
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        print('\n TEST RESULTS :  ' + str(img_name) + '\n')
        lst = top_k[0]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
        score_warn(lst)

def loadImages(path):
    # return array of images
    imagesList = listdir(path)
    #loadedImages = []
    for image in imagesList:
        ext = os.path.splitext(image)[1]
        if ext.lower() not in valid_images:
               continue
        img = (os.path.join(path,image))
        #img = Image.open(os.path.join(path,image))
        #loadedImages.append(img)
        test_image(img,image)

def main():
    loadImages(patharg)

if __name__ == "__main__": 
    main() 



