# evalMe

A quasi-anonymous team evaluation app, that allows to grade any amount of users on 
any amount of criteria. 

The state is in-memory, and is not stored in logs, files, or a database. The state
is lost when the server shuts down.

![evalMe](https://github.com/vvihorev/evalMe/assets/33204359/1fbd6197-26f2-4065-bf38-a58c586cef34)


# Principles

- Every team member gets a **random link to their evaluation form**
- Distribute a set number of points among all team members except for yourself
- The **evaluation can be submitted only once**
- **Only when all evaluations are submitted** the results page becomes available
- Restart the server to reset the evaluation


# Deployment

The app is supposed to be ran while the evaluation is taking place. The easiest way
is to run the default server `python3 main.py` and point nginx to it. 

> If served from a subdirectory of a website, edit the `base_dir` parameter in `config.json`
to the name of the subdirectory, e.g. `"base_dir": "/eval"`
