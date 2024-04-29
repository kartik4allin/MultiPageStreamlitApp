# Use the official Python image
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install ffmpeg
RUN apt-get update

# Install required Python packages
RUN pip install -r requirements.txt --default-timeout=100 future

#RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

# Copy the rest of the application files to the container's working directory
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run your Streamlit application
CMD ["streamlit", "run", "main.py"]
