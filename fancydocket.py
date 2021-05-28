import click
from iterfzf import iterfzf
import re
from os import listdir, mkdir
from pathlib import Path

@click.command()
@click.option('-p', '--path', help="The path where to search for the models", show_default='~/fancydocket', type=click.Path(exists=True))
def fancydocket(path, *args, **kwargs):
    '''
    Command to use the files in your given folder to fill up your models.
    '''
    file_path = get_path(path)

    with click.open_file(file_path, 'r') as filereader:
        model = filereader.read()
    
    all_variables = set(re.findall(r'(?:\{)(.*?)(?:\})', model))

    if not all_variables:
        click.echo('This is not a model file!')
        exit(127)

    input_variables = {variable: click.prompt(variable) for variable in all_variables}

    click.echo(model.format(**input_variables))

def get_path(path):
    if not path:
        path = Path.joinpath(Path.home(), 'fancydocket')
    else:
        path = Path(path)
    if not Path.exists(path):
        mkdir(path)
    if Path.is_dir(path):
        selected_file = iterfzf(listdir(path))
        if not selected_file:
            click.echo("There are no files in the path '" + str(path) + "'!")
            exit(127)    
        selected_file_path = Path.joinpath(path, selected_file)
    elif path:
        selected_file_path = path
    return selected_file_path