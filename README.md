# Medicine Recommendation System

## Introduction
The Medicine Recommendation System is designed to assist in recommending appropriate medications based on user input of symptpmys that are being experienced. The system utilizes machine learning algorithms and a dataset to provide recommendations for the diagnosis along with medication, precautions, diet and workout. 
The project is made completely with modular code approach and follows the production grade code writing principles.
It is trained on multiple machine learning models and the best out of them is chosen up for the predictions based on the accuracy, precision, recall and F1-score. 

## Direct link to app
Click [here](https://medicine-recommender.streamlit.app/) to give it up a try and let your inner doctor found some dignosis for quirky diseses. Altough the accuracy scores are quite good, but I recommend not taking this as any sort of medical advise, your doctor should be the first person whom you should be consulting. But for having fun and experimenting you can try this out.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Dependencies](#dependencies)
6. [Configuration](#configuration)
7. [Documentation](#documentation)
8. [Examples](#examples)
9. [Troubleshooting](#troubleshooting)
10. [Contributors](#contributors)
11. [License](#license)

## Installation
To install and run the Medicine Recommendation System, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/akshatbindal/Medicine-Recommendation-System.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Medicine-Recommendation-System
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To use the Medicine Recommendation System:

1. Run the application using Streamlit:
    ```sh
    streamlit run streamlit_app.py
    ```
2. Follow the on-screen instructions to input the necessary data for medicine recommendations.
3. There's another way for running the application through flask:
    ```sh
    python app.py
    ```
## Features
- Machine learning-based medicine recommendation
- User-friendly interface with Streamlit
- Data processing and analysis

## Dependencies
The project requires the following Python packages:
- Streamlit
- Pandas
- Scikit-learn
- NumPy
- Jupyter Notebook

## Configuration
Ensure that all dependencies are installed. Configuration can be managed through environment variables or configuration files as needed.

## Documentation
Detailed documentation is available within the repository in the form of Jupyter Notebooks located in the `research` directory. 

## Examples
Example usage and data processing steps can be found in the Jupyter Notebooks within the `research` directory.

## Troubleshooting
- Ensure all dependencies are installed correctly.
- Verify the data input format matches the expected format.
- Check the console for error messages and stack traces.

## Contributors
- Akshat Bindal (https://github.com/akshatbindal)

## License
This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.
