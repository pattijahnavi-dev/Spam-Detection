SPAM DETECTION WEBSITE
======================

1. Open this folder in VS Code.
2. Open the VS Code terminal.
3. Install packages:

   python -m pip install -r requirements.txt

4. Run the website:

   python app.py

5. Open the address shown in the terminal, normally:

   http://127.0.0.1:5000

6. Enter a message and click "Detect Spam".

IMPORTANT:
- The website works with the included fallback training data.
- You can later replace the training data in train_model.py with your Kaggle SMS Spam Collection dataset.
- To train the saved model, run:

   python train_model.py

- Then run:

   python app.py
