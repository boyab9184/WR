# WR

This is my solution for the coding assessment.

There are three different options how to run the program listed below.
Open a terminal and run one of the code blocks below.

1. Use Docker. You will need docker as a prerequisite. Run the docker image from my public dockerhub repo and follow the prompt:
```
docker run -ti najsladkoto/web-republic
```

2. If you do not trust what is in the image pushed to my dockerhub repo, you can build a docker image from the Dockerfile in that github repo and than run it:
```
docker build -t assessment https://github.com/boyab9184/WR.git#main
docker run -ti assessment
```

3. You will need git, python3 and pip as prerequisites. Clone that github repo, install requirements and run assessment.py
```
mkdir assessment-bbenev
cd assessment-bbenev
git clone https://github.com/boyab9184/WR.git
cd WR
pip install -r requirements.txt
python3 assessment.py
```