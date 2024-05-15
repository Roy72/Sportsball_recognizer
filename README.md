# Sports Ball Recognizer
An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The goal of this project is to classify 19 different types of Sports Ball are played in different sports all over the world. <br/>
The types are following: <br/>
1. Soccer Ball
2. American Football
3. Tennis Ball
4. Base Ball
5. Volleyball
6. Bowling Ball
7. Golf Ball
8. Beach Ball
9. Pool Ball
10. Hockey Puck
11. Badminton
12. Water Polo
13. Squash
14. Wiffleball
15. Cricket Ball
16. Sepak Takraw
17. Table Tennis Ball
18. taqiyah cap
19. Basket Ball
20. Lawn Bowls

# Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `notebooks/data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (1 time) & 2 epochs (2 times) and got upto ~98% accuracy. <br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/anikroy72/sportsball_recognizer?logs=build). <br/>
<img src = "deployment/gradio_app.png" width="700" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](https://roy72.github.io/Sportsball_recognizer/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
