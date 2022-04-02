# WR

This the solution for conding assessment sent to me by ... - the repo is public so I will not provide company name and the task.

You have couple options how to run the program:

1. You will need docker isntalled. Run the docker image from my public dockerhub repo:

`docker run -ti najsladkoto/web-republic` 

2. Build a docker image from the Dockerfile in that repo and than run it:
```
docker build -t assessment https://github.com/boyab9184/WR.git#main
docker run -ti assessment
```

3. You will need pytho3 and pip insyalled. Clone that repo, install requerments and run assessment.py
```
git clone https://github.com/boyab9184/WR.git
pip install -r requirements.txt
python3 assessment.py
```
