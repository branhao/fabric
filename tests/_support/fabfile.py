from invoke import task


@task
def build(c):
    pass


@task
def deploy(c):
    pass


@task
def basic_run(c):
    c.run("nope")
