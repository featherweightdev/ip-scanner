from typing import List
import typer
import urllib.request

cli = typer.Typer()

# nginx:
# http://158.69.28.24


@cli.command()
def analyze(ips: List[str]):
    """
    Analyze given list of ip addresses
    """
    # list errors for each ip
    errors = {}
    # list servers for each ip
    servers = {}
    # loop and check each listing
    # handle errors - try except
    for ip in ips:
        try:
            with urllib.request.urlopen(f'http://{ip}') as response:
                server = response.info()["server"]
                servers[ip] = server
        except Exception as e:
            errors[ip] = e
    typer.echo(servers)
    typer.echo(errors)
    return(servers, errors)


if __name__ == "__main__":
    typer.run(analyze)
