import streamlit as st
import pika
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
import csv

# Load the trained model
model = joblib.load('modelMNB.pkl') 

def preprocess_data(X):
    # Scale the features using MinMaxScaler
    scaler = MinMaxScaler()
    scaled_X = scaler.fit_transform(X)
    return scaled_X

# Callback function to handle incoming messages
def callback(ch, method, properties, body):
    # Assuming body contains the data for a single row in CSV format
    data = body.decode('utf-8').strip().split(',')
    # Convert data to DataFrame with appropriate column names
    df = pd.DataFrame([data])
    # Preprocess data
    processed_data = preprocess_data(df)
    # Make predictions
    prediction = model.predict(df)
    st.write("Prediction:", prediction)

# Streamlit UI
st.title('Real-time Prediction App')
st.write("## Make predictions in real-time from streaming data")

# Function to publish CSV data to RabbitMQ queue
def publish_csv_data():
    with st.spinner('Publishing CSV Data...'):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='csv_data')

        with open('RTPData.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                st.write(f"Sending record: {file.name} - {row}")
                channel.basic_publish(exchange='',
                                      routing_key='csv_data',
                                      body=','.join(row))
        connection.close()

# Button to start processing CSV data
if st.button('Start Processing CSV Data'):
    with st.spinner('Processing CSV Data...'):
        publish_csv_data()

        # Connect to RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='csv_data')

        # Set up consumer to receive messages from the queue
        channel.basic_consume(queue='csv_data',
                              on_message_callback=callback,
                              auto_ack=True)
        st.write('Waiting for messages...')
        channel.start_consuming()

# Display a message to indicate that the app is running
st.write('App is running...')
