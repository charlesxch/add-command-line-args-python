import pandas as pd
import click


@click.command()
@click.option('--filepath')
@click.option('--class_col')
@click.option('--output_file')
def main(filepath, class_col, output_file):
    # read in wisconsin breast cancer data
    data = pd.read_csv(filepath)

    result = data.groupby(class_col).size().reset_index(name='Count')
    result = result.rename(columns={class_col: 'Class'})

    result.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()
