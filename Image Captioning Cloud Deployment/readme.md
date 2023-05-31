here we use local model dependencies instead of downloading dependencies in the cloud , we keep downloaded
hugging face model inside model folder.

download model folder from - https://drive.google.com/drive/folders/1sXLy44mkk0BD60WyweccoSt2yRN-I-O7?usp=sharing
and create an empyty folder img to store photos got from api

Commands to run to create gcp cloud , where kalesh1  is the cloud run app name

docker build -t gcr.io/boreal-logic-379107/kalesh1 .
docker push gcr.io/boreal-logic-379107/kalesh1

[gcr.io/boreal-logic-379107/kalesh1]
