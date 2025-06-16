import click
from whitespace_stego.encoder import embed_message
from whitespace_stego.decoder import decode_message

@click.group()
def cli():
    pass

@cli.command()
@click.option('--message', '-m', required=True)
@click.option('--carrier', '-c', default="")
def encode(message, carrier):
    result = embed_message(carrier, message)
    click.echo(result)

@cli.command()
@click.option('--input', '-i', required=True)
def decode(input):
    result = decode_message(input)
    click.echo(result)

if __name__ == '__main__':
    cli()
