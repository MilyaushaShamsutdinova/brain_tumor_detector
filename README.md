# Brain Tumor Detection

Brain Tumor detection model deployed and integrated into a web application using Docker, FastAPI and Streamlit.


## How to Run


1. **Clone the Repository**
   ```bash
   git clone https://github.com/MilyaushaShamsutdinova/brain_tumor_detector.git
   ```

2. **Build Docker Images**
    ```bash
    cd code
    cd deployment
    docker-compose build
    ```
3. **Run the Containers**
    ```
    docker-compose up
    ```

4. **Access the Web Application**: 
    
    Once the containers are up and running, you can access the web application in your browser. Navigate to the web application at **http://localhost:8501.** Upload a brain MRI image file in .jpg format. Click the "Predict" button to run the model and receive the prediction.


5. **Stopping the Containers**

    To stop the containers, press Ctrl+C in the terminal where docker-compose up is running, or run the following command in a new terminal:
    ```bash
    docker-compose down
    ```
