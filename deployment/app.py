from fastai.vision.all import *
import gradio as gr

#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

sportballs_labels = (
    'American Football',
    'Base Ball', 
    'Basket Ball', 
    'Beach Ball', 
    'Bowling Ball', 
    'Cricket Ball',
    'Golf Ball', 
    'Hockey Puck',
    'Lawn Bowls', 
    'Pool Ball', 
    'Sepak Takraw', 
    'Shuttlecock', 
    'Soccer Ball', 
    'Squash Ball', 
    'Table Tennis Ball', 
    'Tennis Ball', 
    'Volley Ball', 
    'Waterpolo Ball',
    'Wiffle Ball'
)

model = load_learner('sportballs-recognizer-v2.pkl')

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(sportballs_labels, map(float, probs)))

image = gr.Image(width=224,height=224)
label = gr.Label(num_top_classes=5)
examples = [
    'unknown_00.jpg',
    'unknown_01.jpg',
    'unknown_02.jpg',
    'unknown_03.jpg',
    'unknown_04.jpg',
    'unknown_05.jpg'

    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)