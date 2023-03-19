Percobaan dockerfile menjalankan streamlit (folder tutorial/exercise.py)

Untuk melakukan create image 
docker build -t my-streamliti-app .

Untuk menjalankan image
docker run -p 8501:8501 my-fastapi-app

Untuk melihat hasilnya di local
http://localhost:8501