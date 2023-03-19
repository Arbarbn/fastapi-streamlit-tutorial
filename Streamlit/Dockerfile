# Base image
FROM python:3.9.12

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port for Streamlit
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "src/app.py"]
