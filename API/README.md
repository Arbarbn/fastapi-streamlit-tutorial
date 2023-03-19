Untuk melakukan create image 
docker build -t my-fastapi-app .

Untuk menjalankan image
docker run -p 8000:8000 my-fastapi-app

Untuk melihat hasilnya di local
http://localhost:8000

seraching for IP Address fastapi in localhost -> dilihat yg bagian gateway
docker network inspect bridge
