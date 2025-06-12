import typer

app = typer.Typer()

@app.command()
def encode():
    print("Encoding message...")

@app.command()
def decode():
    print("Decoding message...")

if __name__ == "__main__":
    app()
